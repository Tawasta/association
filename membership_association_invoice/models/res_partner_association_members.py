# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartnerAssociationMembers(models.Model):

    # 1. Private attributes
    _inherit = 'res.partner.association.members'

    # 2. Fields declaration
    invoice = fields.Many2one('account.invoice', 'Invoice')
    invoice_state = fields.Char('Invoice state', compute='compute_invoice_state')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def compute_invoice_state(self):
        for record in self:
            if record.invoice and record.invoice.state:
                record.invoice_state = record.invoice.state

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
