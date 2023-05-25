from odoo import api, fields, models


class EtiquetaGeral(models.Model):
    _name = "etiqueta.geral"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Etiqueta Geral"

    numero_nfe = fields.Char(string="NF", required=True, tracking=True)
    cliente = fields.Many2one('res.partner', string='Cliente', required=True, size=28, tracking=True)
    produto = fields.Many2one('product.template', string='Produto', required=True, size=28, tracking=True)
    codigo = fields.Char(string='Código', required=True, tracking=True)
    qtt = fields.Char(string='QT Total', tracking=True)
    qtc = fields.Char(string='QT Caixa', tracking=True)
    volumes = fields.Char(string='Volumes', tracking=True)
    state = fields.Selection(
        [('rascunho', 'Rascunho'), ('impresso', 'Impresso'), ('envio', 'Enviado')],
        string='Status', default='rascunho')

    def action_confirm(self):
        self.state = 'impresso'

    def action_draft(self):
        self.state = 'rascunho'

    def action_envio(self):
        self.state = 'envio'
