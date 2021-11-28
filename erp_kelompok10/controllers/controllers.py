# -*- coding: utf-8 -*-
from odoo import http

# class ErpKelompok10(http.Controller):
#     @http.route('/erp_kelompok10/erp_kelompok10/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/erp_kelompok10/erp_kelompok10/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('erp_kelompok10.listing', {
#             'root': '/erp_kelompok10/erp_kelompok10',
#             'objects': http.request.env['erp_kelompok10.erp_kelompok10'].search([]),
#         })

#     @http.route('/erp_kelompok10/erp_kelompok10/objects/<model("erp_kelompok10.erp_kelompok10"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('erp_kelompok10.object', {
#             'object': obj
#         })