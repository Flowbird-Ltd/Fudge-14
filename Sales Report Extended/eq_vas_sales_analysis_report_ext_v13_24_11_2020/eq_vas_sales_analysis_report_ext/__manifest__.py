# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################
{
    'name': "Extend Sale Analysis Report",
    'category': 'Sales',
    'version': '13.0.1.0',
    'author': 'Equick ERP',
    'description': """
        Extend Sale Analysis Report.
        * Ref no: Fudge-Kitchen
    """,
    'summary': """Extend Sale Analysis Report""",
    'depends': ['sale', 'sale_management'],
    'license': 'OPL-1',
    'website': "",
    'data': [
            'views/sale_view.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
