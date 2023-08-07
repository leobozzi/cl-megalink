# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _


class AccountMove(models.Model):
    _inherit = "account.move"
    _description = 'account.move'
    
    partner_ref = fields.Char(
        string="Partner Ref",
        related='partner_id.ref',
    )