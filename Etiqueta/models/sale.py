from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"


    venda_cliente = fields.Char(string='Cliente')


