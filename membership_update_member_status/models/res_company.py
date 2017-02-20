# -*- coding: utf-8 -*-

# 1. Standard library imports:
import logging

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp.exceptions import ValidationError

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:
_logger = logging.getLogger()

class ResCompany(models.Model):
    
    # 1. Private attributes
    _inherit = 'res.company'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.one
    def membership_update_member_status(self):
        # Updates partner membership lines from invoices

        invoices = self.env['account.invoice'].search([
            ('state', 'not in', ['draft']),
            ('invoice_line.product_id.membership', '=', True),
        ])

        for invoice in invoices:
            # Go through all invoices that aren't in draft state

            for line in invoice.invoice_line:
                # Pass lines without membership products
                if not line.product_id.membership:
                    continue

                # Check if there already is a line for this product
                membership_line = self.env['membership.membership_line'].search(
                    [('account_invoice_line', '=', line.id)]
                )

                if membership_line:
                    # The membership is created. Nothing to do
                    continue

                # Create a membership line
                date_from = line.product_id.membership_date_from
                date_to = line.product_id.membership_date_to

                values = {
                    'partner': invoice.partner_id.id,
                    'membership_id': line.product_id.id,
                    'member_price': line.price_unit,
                    'date': fields.Date.today(),
                    'date_from': date_from,
                    'date_to': date_to,
                    'account_invoice_line': line.id,
                }

                partner = invoice.partner_id
                membership_state = partner._get_membership_state()[partner.id]

                try:
                    membership_line = self.env['membership.membership_line'].create(values)
                    membership_line.state = membership_state

                except ValidationError, e:
                    msg = "Did not update %s: %s" % (values, e)
                    _logger.warning(msg)

                invoice.partner_id.membership_state = membership_state

class ResPartner(models.Model):

    # 1. Private attributes
    _inherit = 'res.partner'

    # A helper to use the _membership_state-method from new api
    @api.model
    def _get_membership_state(self):
        return super(ResPartner, self)._membership_state(args={}, name=False, context=self._context)