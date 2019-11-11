# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2017 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Luis Ernesto Garcia Medina
#               (ernesto.garcia@telematel.com)
#               Sergio Ernesto Tostado Sánchez
#               (sergio.tostado@telematel.com)
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

# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2017 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Sergio Ernesto Tostado Sánchez
#               (sergio.tostado@telematel.com)
#               Luis Ernesto García Medina
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


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    stock_expedition_place = fields.Many2one(
        'res.partner',
        string = 'Almacén (Lugar de Expedición)',
        help = 'Almacén, además del Lugar de Expedición, es un \
                para generar el CFDI 3.3'
    )

    @api.one
    @api.constrains('stock_expedition_place')
    def _checkstock_expedition_place(self):
        obj_stock_warehouse = self.env['stock.warehouse']
        partner_has_warehouse = obj_stock_warehouse.search([
            ('partner_id', '=', self.stock_expedition_place.id)
        ])
        if len(partner_has_warehouse) == 0:
            raise ValidationError(
                "Tu Lugar de Expedición no es un almacén existente.\
                 Por favor seleccione uno que se encuentre en:\
                 Inventario > Configuración > Almacenes\
                 (campo Dirección).")
