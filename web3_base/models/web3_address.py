from odoo import models, fields, api

class Web3Address(models.Model):
    _inherit = "web3.blockchain"

    display_name = fields.Char(string="Display Name", required=True)

    public_key = fields.Char(string="Public Key", required=True)

    private_key = fields.Char(string="Private Key")

    type = fields.Selection([
        ('eoa', 'Externally Owned Account')
        ('contract', 'Contract')
    ], string='Type')

    network_id = fields.Many2one('web3.network', string='Network')

    partner_id = fields.Many2one('res.partner', string='partner')

    currency_id = fields.Many2one('res.currency', string='currency')

    # TODO: Different address status methods