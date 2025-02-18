from odoo import models, fields, api

class Web3Network(models.Model):
    _name = "web3.blockchain"

    name = fields.Char(string="Name", required=True)

    short_name = fields.Char(string="Short Name", required=True)

    main_currency_id = fields.Many2one("web3.currency", string="Main Currency")

    # TODO: This needs a sequence to check which is the main one for the network rpc
    node_ids = fields.One2many('web3.node', 'network_id', string='Node')

    rpc_url = fields.Char(string="RPC URL", compute='_compute_rpc_url')

    # TODO: SUBNET system as parent-childs??


    @api.depends('node_ids, node_ids.rpc_url, node_ids.sequence')
    def _compute_rpc_url(self):
        for rec in self:
            for node in rec.node_ids.sorted('sequence'):
                if node.rpc_url:
                    rec.rpc_url = node.url
                    break
    # TODO: Different Network status methods



from odoo import models, fields, api

class Web3NetworkNode(models.Model):
    _name = "web3.network.node"

    name = fields.Char(string='Name')

    network_id = fields.Many2one('web3.network', string='Network')

    url = fields.Char(string='URL')

    # TODO: idek if it makes sense to separe between rpc and validation nodes. mmmm


    # TODO: more status methods and fields