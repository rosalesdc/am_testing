# -*- encoding: utf-8 -*-
#
# Module written to Odoo, Open Source Management Solution
#
# Copyright (c) 2019 Telematel - http://www.telematel.com/
# All Rights Reserved.
#
# Developer(s): Randy La Rosa Alvarez
#               (randi.larosa@telematel.com)
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
    'name': 'TELEMATEL | AMROMA FIX LISTVIEW PRODUCT TEMPLATE',
    'author': 'TELEMATEL ©',
    'category': 'Extra Tools',
    'sequence': 50,
    'summary': "Fix error in list view of product template",
    'website': 'https://www.telematel.com',
    'version': '1.0',
    'description': """
FIX LISTVIEW PRODUCT TEMPLATE
=============================
Fix error in list view of product template.
    """,
    'depends': ['stock'],
    'installable': True,
    'data': [
        'views/inherited_product_template_tree.xml'
    ],
    'demo': [],
    'qweb': [],
    'application': False,
}
