# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import ValidationError


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """ Function to find the selected partner's due amount and check the condition whether the customer has pending credit limit, sends a warning if yes """

        current_partners_sales = self.partner_id.sale_order_ids.filtered(
            lambda x: x.state == 'sent')
        due_amount = sum(current_partners_sales.mapped('amount_total'))

        print('due amount', due_amount)
        if self.partner_id.is_active_credit_limit:
            if self.partner_id.warning_amount < due_amount < self.partner_id.blocking_amount:
                self.partner_id.write({'sale_warn_msg': f'Customer has pending {due_amount} to be paid'})

    def action_confirm(self):
        """ Function to block the user from creating if the customer crosses the blocking amount limit, salesman cannot make sale order with that customer."""
        current_partners_sales = self.partner_id.sale_order_ids.filtered(
            lambda x: x.state == 'sent')

        due_amount = sum(current_partners_sales.mapped('amount_total'))

        if self.partner_id.is_active_credit_limit:
            if self.partner_id.blocking_amount < due_amount:
                raise ValidationError("This customer has been blocked")
        return super().action_quotation_send()
