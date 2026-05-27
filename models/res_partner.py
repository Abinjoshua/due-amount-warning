# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_active_credit_limit = fields.Boolean("Active Credit Limit")
    warning_amount = fields.Float("Amount Warning")
    blocking_amount = fields.Float("Blocking Amount")


