# -*- coding: utf-8 -*-
from odoo import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def _message_create(self, values_list):
        msg = super(CrmLead, self)._message_create(values_list)
        if not self.partner_id:
            return msg
        if self.env['ir.config_parameter'].sudo().get_param('lead.post_msgs_to_partner'):
            link_url = """Lead Id: <a data-oe-id="%s" data-oe-model="crm.lead" href="/mail/view?message_id=%s">%s</a>""" %(self.id, msg.id, self.id)
            part_msg_body = link_url + '<br/> ' + msg.body
            partner_msg = msg.copy(default={'res_id': self.partner_id.id, 'model': 'res.partner', 'body': part_msg_body})
            parent = self.partner_id.parent_id
            parent_default_vals = {}
            if parent:
                parent_msg = msg.copy(default={'res_id': parent.id, 'model': 'res.partner', 'body': part_msg_body})
                if parent_msg:
                    parent_default_vals = {'mail_message_id': parent_msg.id}
#            When Message contains multiple lines, below code will add [Lead Ref] to first line only.
#            other line is not being affected and that will print as it is.
            default_vals = {'mail_message_id': partner_msg.id}
            for line in msg.tracking_value_ids:
                if parent_default_vals:
                    line.copy(default=parent_default_vals)
                line.copy(default=default_vals)
        return msg
