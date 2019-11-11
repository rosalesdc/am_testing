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

{
    'name': 'TELEMATEL | Invoice Format',
    'author': 'TELEMATEL ©',
    'category': 'Extra Tools',
    'sequence': 50,
    'summary': "Invoice Format for AM ROMA Y CIA S.A. DE C.V.",
    'website': 'https://www.telematel.com',
    'version': '1.0',
    'description': """
Invoice Format
==============
For AM ROMA Y CIA S.A. DE C.V, formats his invoice.
    """,
    'depends': [
        'base', 'web', 'account', 'l10n_mx_edi',
        'sale', 'sale_management', 'stock'
    ],
    'installable': True,
    'data': [
        'data/res_config_settings.xml',
        'views/l10n_mx_edi_report_invoice.xml',
        'views/inherited_invoice_form.xml'
    ],
    'demo': [],
    'qweb': [],
    'application': False,
}
