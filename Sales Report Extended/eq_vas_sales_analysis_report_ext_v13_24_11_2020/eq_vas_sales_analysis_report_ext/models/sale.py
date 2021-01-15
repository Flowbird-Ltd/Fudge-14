# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################

from odoo import api, fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    proposed_despatch = fields.Date(string="Proposed Despatch")
    dispatch_date = fields.Date(string="Confirmed Despatch")

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['proposed_despatch'] = ", s.x_studio_proposed_despatch as proposed_despatch"
        fields['dispatch_date'] = ", s.x_studio_dispatch_date as dispatch_date"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)