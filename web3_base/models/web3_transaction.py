from odoo import models, fields, api

class Web3Transaction(models.Model):
    _name = "web3.transaction"

    name = fields.Char(string="Name", required=True, readonly=True, default='Draft transaction')

    network_id = fields.Many2one('web3.network', string='Network')

    origin_address_id = fields.Many2one('web3.adress', string='Origin Address')
    destination_address_id = fields.Many2one('web3.adress', string='Destination Address')

    currency_id = fields.Many2one('web3.currency', string='Token')

    amount = fields.Float(string="Amount", required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ], string='State', default='draft')

    # Can I add metadata to the transaction?

    # TODO: probably some configurable field through a wizard
    # metadata = fields.Text('Metadata')