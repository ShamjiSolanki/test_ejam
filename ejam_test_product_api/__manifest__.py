# -*- coding: utf-8 -*-
{
    'name': "ejam_test_product_api",

    'summary': """API module return product data as per requested.""",

    'description': """ 
        Created module which return product data as below.
        1. Product name.
        2. Sale Price.
        3. Cost Price.
        4. Onhand Quantity.
        5. Category.
        Return above data for requested product id using api.
    """,

    'author': "Ejam",
    'website': "http://www.ejam.com",

    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
