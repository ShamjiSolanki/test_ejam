# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class EjamTestProductApi(http.Controller):

    @http.route('/ejam_test_product_api/product/<prod_id>/', type='http', auth="public", website=False)
    def list(self, prod_id, **post):
        values = {}
        Product = request.env['product.product']
        domain = [('id', '=', prod_id)]
        products = Product.sudo().search(domain)
        values.update({
            'name' : products.name,
            'sale_price': products.list_price,
            'cost_price': products.standard_price,
            'onhand_quantity': products.qty_available,
            'category': products.categ_id.name
        })
        return http.Response(
            json.dumps(values),
            status=200,
            mimetype='application/json'
        )

