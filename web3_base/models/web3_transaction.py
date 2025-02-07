from odoo import models, fields, api

class Web3Transaction(models.Model):
    _inherit = "web3.transaction"

    network_id = fields.Many2one('web3.network', string='Network')

    origin_address_id = fields.Many2one('web3.adress', string='Origin Address')
    destination_address_id = fields.Many2one('web3.adress', string='Destination Address')