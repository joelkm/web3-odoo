from odoo import models, fields, api

class Web3Address(models.Model):
    """
    Network address
    """
    _name = "web3.blockchain"

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

    # TODO: Review widespread company usage
    owner_user_ids = fields.Many2many('res.users', string='Owners')

    note = fields.Text(string="Note")

    balance_line_ids = fields.One2many('web3.address.line', 'holder_address_id', string='Balance')

    # TODO: Different address status methods

class Web3AddressLine(models.Model):
    """
    Balance details
    """
    _name = "web3.address.line"

    amount = fields.Float(string="Amount")

    holder_address_id = fields.Many2one('web3.address', string='Holder Address')

    token_address_id = fields.Many2one('web3.address', string='Token Address')
    
    currency_id = fields.Many2one('res.currency', string='Token', related='address_id.currency_id')