# -*- coding: utf-8 -*-
{
    'name': "Due Amount Warning",
    'version': "1.0",
    'license': "LGPL-3",
    'author': "Cybrosys",
    'website': "http://www.cybrosys.com",
    'sequence': 1,
    'application': True,
    'depends': ['base', 'sale_management', 'contacts'],
    'data': ['views/res_partner_view.xml',
             ],
    'auto_install': True,
}
