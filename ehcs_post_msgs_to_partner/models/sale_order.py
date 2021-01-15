# -*- coding: utf-8 -*-
from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _message_create(self, values_list):
        msg = super(SaleOrder, self)._message_create(values_list)
        if self.env['ir.config_parameter'].sudo().get_param('sale.post_msgs_to_partner'):
            link_url = """Sale Order: <a data-oe-id="%s" data-oe-model="sale.order" href="/mail/view?message_id=%s">%s</a>""" %(self.id, msg.id, self.name)
            part_msg_body = link_url + '<br/> ' + msg.body
            partner_msg = msg.copy(default={'res_id': self.partner_id.id, 'model': 'res.partner', 'body': part_msg_body})
#            When Message contains multiple lines, below code will add [Sale Order Ref] to first line only.
#            other line is not being affected and that will print as it is.
            default_vals = {'mail_message_id': partner_msg.id}
            for line in msg.tracking_value_ids:
                line.copy(default=default_vals)
        return msg
