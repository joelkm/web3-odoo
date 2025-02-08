from odoo import models, fields, api

class Web3Node(models.Model):
    _name = "web3.node"

    name = fields.Char(string='Name')

    network_id = fields.Many2one('web3.network', string='Network')

    url = fields.Char(string='URL')

    # TODO: idek if it makes sense to separe between rpc and validation nodes. mmmm


    # TODO: more status methods and fields