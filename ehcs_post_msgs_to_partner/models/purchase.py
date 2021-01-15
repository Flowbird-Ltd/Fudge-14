# -*- coding: utf-8 -*-
from odoo import models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _message_create(self, values_list):
        msg = super(PurchaseOrder, self)._message_create(values_list)
        if self.env['ir.config_parameter'].sudo().get_param('purchase.post_msgs_to_partner'):
            link_url = """Purchase Order: <a data-oe-id="%s" data-oe-model="purchase.order" href="/mail/view?message_id=%s">%s</a>""" %(self.id, msg.id, self.name)
            part_msg_body = link_url + '<br/> ' +  msg.body
            partner_msg = msg.copy(default={'res_id': self.partner_id.id, 'model': 'res.partner', 'body': part_msg_body})
            flag = False
    #         When Message contains multiple lines, below code will add [PurchaseOrder Ref] to first line only.
    #         other line is not being affected and that will print as it is.
            for line in msg.tracking_value_ids:
                default_vals = {'mail_message_id': partner_msg.id}
                line.copy(default=default_vals)
        return msg
