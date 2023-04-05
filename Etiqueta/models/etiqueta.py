from odoo import api, fields, models


class EtiquetaGeral(models.Model):
    _name = "etiqueta.geral"
    _description = "Etiqueta Geral"

    numero_nfe = fields.Integer(string='NF', required=True)
    cliente = fields.Char(string='Cliente')
    produto = fields.Char(string='Produto')
    codigo = fields.Char(string='Código')
    qtt = fields.Char(string='QT Total')
    qtc = fields.Char(string='QT Caixa')
    volumes = fields.Char(string='Volumes')

