# -*- coding: utf-8 -*-
from odoo import http

# class Challange(http.Controller):
#     @http.route('/challange/challange/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/challange/challange/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('challange.listing', {
#             'root': '/challange/challange',
#             'objects': http.request.env['challange.challange'].search([]),
#         })

#     @http.route('/challange/challange/objects/<model("challange.challange"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('challange.object', {
#             'object': obj
#         })