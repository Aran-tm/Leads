# -*- coding: utf-8 -*-
{
    'name': "Leads",

    'summary': """
        This is an important module created for opportunities and leads at any enterprises""",

    'description': """
        Module created for opportunities and leads at any enterprises
    """,

    'author': "Armando Roberto Travieso",
    'website': "https://github.com/Aran-tm/leads_form",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Leads/Leads',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'icon': 'leads/static/leads.png',
}
