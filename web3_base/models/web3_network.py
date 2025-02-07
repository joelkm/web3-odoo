from odoo import models, fields, api

class Web3Network(models.Model):
    _inherit = "web3.blockchain"

    name = fields.Char(string="Name", required=True)

    main_currency_id = fields.Many2one("web3.currency", string="Main Currency")

    # TODO: This needs a sequence to check which is the main one for the network rpc
    node_ids = fields.One2many('web3.node', 'network_id', string='Node')

    # TODO: Different Network status methods