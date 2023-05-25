from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    teste1 = fields.Char(string='Etiqueta')
