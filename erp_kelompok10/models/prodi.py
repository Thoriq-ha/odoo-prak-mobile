
from odoo import models, fields, api

class Prodi(models.Model):
    _name = 'prodi.uin'
    _description = 'Data prodi di UIN MALANG'

    name = fields.Text(String = "Nama Prodi", required=True, help ='Input Nama Prodi')