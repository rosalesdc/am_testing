# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2017 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Luis Ernesto García Medina
#               (ernesto.garcia@telematel.com)
#
########################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################

from odoo import api, fields, models, tools
from odoo.exceptions import ValidationError
from functools import partial
from odoo.tools.misc import formatLang
import logging

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.one
    @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
                 'currency_id', 'company_id', 'date_invoice', 'type')
    def _compute_amount(self):
        super(AccountInvoice,self)._compute_amount()
        self.subtotal_not_show = sum(line.price_for_tax_incl for line in self.invoice_line_ids)

    show_tax_report = fields.Boolean(string = 'No desglosar IEPS', default=True, help="Para desglosar IEPS, desactive este campo")
    subtotal_not_show = fields.Float(compute=_compute_amount)
    ieps_6 = fields.Float(
        string='IEPS 6%',
        compute='get_ieps_amounts'
    )
    ieps_7 = fields.Float(
        string='IEPS 7%',
        compute='get_ieps_amounts'
    )
    ieps_9 = fields.Float(
        string='IEPS 9%',
        compute='get_ieps_amounts'
    )

    @api.multi
    @api.depends('tax_line_ids')
    def get_ieps_amounts(self):
        for invoice in self:
            total_ieps6 = sum([line.amount_total for line in invoice.tax_line_ids if line.tax_id.is_ieps and line.tax_id.ieps_to == '6'])
            total_ieps7 = sum([line.amount_total for line in invoice.tax_line_ids if line.tax_id.is_ieps and line.tax_id.ieps_to == '7'])
            total_ieps8 = sum([line.amount_total for line in invoice.tax_line_ids if line.tax_id.is_ieps and line.tax_id.ieps_to == '9'])
            invoice.ieps_6 = total_ieps6
            invoice.ieps_7 = total_ieps7
            invoice.ieps_9 = total_ieps8

    @api.multi
    def _amount_by_group(self):
        self.ensure_one()
        currency = self.currency_id or self.company_id.currency_id
        fmt = partial(formatLang, self.with_context(lang=self.partner_id.lang).env, currency_obj=currency)
        res = {}
        for line in self.tax_line_ids:
            if self.show_tax_report and line.tax_id.is_ieps:
                continue
            res.setdefault(line.tax_id.tax_group_id, {'base': 0.0, 'amount': 0.0})
            field_value = line.tax_id.tax_group_id.show_in_report
            res[line.tax_id.tax_group_id]['amount'] += line.amount
            res[line.tax_id.tax_group_id]['base'] += line.base
            res[line.tax_id.tax_group_id]['show'] = field_value
        res = sorted(res.items(), key=lambda l: l[0].sequence)
        res = [(
            r[0].name, r[1]['amount'], r[1]['base'],
            fmt(r[1]['amount']), fmt(r[1]['base']),r[1]['show']
        ) for r in res]
        return res
    
    def group_tax_show(self, tax):
        tax_obj = self.env["account.tax"].browse(tax.get("id"))
        return tax_obj.tax_group_id and tax_obj.tax_group_id.show_in_report

    @api.multi
    def _l10n_mx_edi_create_taxes_cfdi_values(self):
        '''Create the taxes values to fill the CFDI template.
        '''
        self.ensure_one()
        values = {
            'total_withhold': 0,
            'total_transferred': 0,
            'total_transferred_not_show': 0,
            'withholding': [],
            'transferred': [],
        }
        taxes = {}
        for line in self.invoice_line_ids.filtered('price_subtotal'):
            price_unit = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            line_taxes = line.invoice_line_tax_ids.filtered(
                lambda r: r.l10n_mx_cfdi_tax_type != 'Exento').compute_all(
                    price_unit, self.currency_id, line.quantity, line.product_id, self.partner_id)['taxes']
            for line_tax in line_taxes:
                amount = round(line_tax.get("amount", 0), 2)
                tax = self.env['account.tax'].browse(line_tax.get('id'))
                if line_tax.get('id') not in taxes:
                    taxes.update({line_tax.get('id'): {
                         'id': line_tax.get('id'),
                         'name': (tax.tag_ids[0].name
                                  if tax.tag_ids else tax.name).upper(),
                         'amount': amount,
                         'rate': round(abs(tax.amount), 2),
                         'type': tax.l10n_mx_cfdi_tax_type,
                         'tax_amount': amount,
                     }})
                else:
                    taxes[line_tax.get('id')].update({
                        'amount': taxes[line_tax.get('id')]['amount'] + amount
                    })
                if tax.amount >= 0:
                    values['total_transferred'] += amount
                    if line.invoice_id.show_tax_report and tax.tax_group_id.show_in_report:
                        values['total_transferred_not_show'] += amount
                else:
                    values['total_withhold'] += amount
        values['transferred'] = [tax for tax in taxes.values() if tax['tax_amount'] >= 0]
        values['withholding'] = [tax for tax in taxes.values() if tax['tax_amount'] < 0]
        return values


class AccountInvoiceLine(models.Model):

    _inherit = "account.invoice.line"

    @api.one
    @api.depends('price_unit', 'discount', 'invoice_line_tax_ids', 'quantity',
        'product_id', 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id',
        'invoice_id.date_invoice', 'invoice_id.date')
    def _compute_price_tax(self):
        price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
        self.price_for_tax_incl = self.quantity * price

    price_for_tax_incl = fields.Float(compute=_compute_price_tax)
