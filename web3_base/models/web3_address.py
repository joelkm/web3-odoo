from odoo import models, fields, api

class Web3Address(models.Model):
    """
    Network address
    """
    _name = "web3.blockchain"

    display_name = fields.Char(string="Display Name", required=True, compute='_compute_display_name', store=True)

    description = fields.Char(string="Description", compute='_compute_description', store=True)

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
    # Rethink ownership model
    # Option 1:
    # Selection field for company owned or user owned and fields (m2m??)

    note = fields.Text(string="Note")

    ### Balance fields ###

    balance_line_ids = fields.One2many('web3.address.line', 'holder_address_id', string='Balance')

    total_balance = fields.Float(string="Total Balance", compute='_compute_total_balance')

    total_balance_currency_id = fields.Many2one('res.currency', string="Currency", compute='_compute_total_balance')

    # TODO: Support for ERC standards??

    @api.depends('network_id')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.public_key} - {rec.network_id.name}"

    @api.depends('currency_id', 'partner_id')
    def _compute_description(self):
        for rec in self:
            if rec.currency_id:
                rec.description = f"Address for {rec.partner_id.name}"
            else:
                rec.description = f"{rec.network_id.name} - {rec.partner_id.name}"

    @api.depends('balance_line_ids' ,'total_balance_currency_id')
    def _compute_total_balance(self):
        pass
    
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