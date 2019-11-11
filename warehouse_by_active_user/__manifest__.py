# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2017 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Luis Ernesto Garcia Medina
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

{
    'name': 'TELEMATEL | Load warehouse by active user for sale order.',
    'author': 'TELEMATEL ©',
    'category': 'Extra Tools',
    'sequence': 50,
    'summary': "Load warehouse by active user for sale order",
    'website': 'https://www.telematel.com',
    'version': '1.0',
    'description': """
        Load warehouse by active user for sale order
        """,
    'depends': [
        'stock',
        'sale_management'
    ],
    'installable': True,
    'data': [
        'views/stock_warehouse_inherit_form_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'application': False,
}
