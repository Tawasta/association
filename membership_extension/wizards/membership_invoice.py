# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:
import logging
_logger = logging.getLogger(__name__)


class MembershipInvoice(models.Model):
    # 1. Private attributes
    _inherit = 'membership.invoice'

    # 2. Fields declaration
    payment_term = fields.Many2one('account.payment.term')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.multi
    def membership_invoice(self):
        # Override this instead of res.partner.create_membership_invoice()
        # so we don't have to overwrite the whole method
        res = super(MembershipInvoice, self).membership_invoice()

        try:
            invoices = res['domain'][0][2]
        except Exception, e:
            invoices = False
            _logger.error('Could not parse membership invoice ids: %s', e)

        if self.payment_term:
            for invoice in invoices:
                self.env['account.invoice'].browse([invoice]).payment_term = self.payment_term

        return res
