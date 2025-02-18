from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):

    _inherit = "res.partner"

    web3_address_ids = fields.One2many('web3.address', 'partner_id', string='Wallet Addresses')