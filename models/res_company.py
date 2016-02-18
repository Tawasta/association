# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


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

        invoices = self.env['account.invoice'].search([('state', 'not in', ['draft'])])

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
                membership_state = invoice.partner_id.membership_state

                date_from = line.product_id.membership_date_from
                date_to = line.product_id.membership_date_to

                values = {
                    'partner': invoice.partner_id.id,
                    'membership_id': line.product_id.id,
                    'member_price': line.price_unit,
                    'date': fields.Date.today(),
                    'date_from': invoice.date_invoice,
                    'date_to': date_to,
                    'account_invoice_line': line.id,
                    'state': membership_state,
                }

                self.env['membership.membership_line'].create(values)

                invoice.partner_id.membership = membership_state
