# -*- coding: utf-8 -*-
{
    'name': "erp_kelompok10",

    'summary': """
        Program Aplikasi Praktikum Rekayasa Perangkat Lunak""",

    'description': """
        Kelompok 10 : [Thoriq Harizul Ahsan],
        [Alfin Rizky Amartya],
        [Jose Andriyanto Wibowo]
        Asisten Praktikum RPL : Febrina
    """,

    'author': "Kelompok 10 - F",

    'website': "https://www.uin-malang.ac.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/prodi.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}