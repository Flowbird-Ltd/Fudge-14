# -*- coding: utf-8 -*-
from odoo import api, fields, models


class BaseConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    post_msg_from_sales = fields.Boolean('Sales', config_parameter='sale.post_msgs_to_partner')
    post_msg_from_lead = fields.Boolean('Lead/Opportunity', config_parameter='lead.post_msgs_to_partner')
    post_msg_from_invoice = fields.Boolean('Invoice', config_parameter='invoice.post_msgs_to_partner')
    post_msg_from_purchase = fields.Boolean('Purchase', config_parameter='purchase.post_msgs_to_partner')
