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


class AccountTaxGroup(models.Model):

    _inherit = "account.tax.group"

    show_in_report = fields.Boolean(string = 'Imprimir en reporte', default=False)

class AccountTax(models.Model):
    _inherit = 'account.tax'


    is_ieps = fields.Boolean(
        string='¿The tax is IEPS?')
    ieps_to = fields.Selection(
        selection=[
            ('6', '6%'),
            ('7', '7%'),
            ('9', '9%')],
        string='IEPS to')

