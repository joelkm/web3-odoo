from odoo import models, fields, api

class ResCurrency(models.Model):
    _name = 'res.currency'

    is_crypto = fields.Boolean('Cryptocurrency', default=False)

    address_ids = fields.One2many('web3.address', 'currency_id', string='Web3 Addresses')