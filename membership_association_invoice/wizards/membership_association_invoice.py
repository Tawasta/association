# -*- coding: utf-8 -*-

# 1. Standard library imports:
import uuid

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class MembershipAssociationInvoice(models.TransientModel):

    # 1. Private attributes
    _name = 'membership.association.invoice'

    # 2. Fields declaration
    uuid = fields.Char("UUID", default=uuid.uuid4().hex)
    partner = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        default=lambda self: self._default_partner(),
    )
    invoice_lines = fields.One2many(
        comodel_name='account.invoice.line.transient',
        inverse_name='id',
        string='Invoice lines',
    )

    # 3. Default methods
    def _default_partner(self):
        return self.env['res.partner'].browse(self._context.get('active_id'))

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.onchange('partner')
    def onchange_partner_update_invoice_lines(self):
        line_model = self.env['account.invoice.line.transient']

        for association_member in self.partner.association_members:
            self.invoice_lines += line_model.create({
                'uuid': self.uuid,
                'name': association_member.name.name,
                'quantity': association_member.amount,
            })

    # 6. CRUD methods

    # 7. Action methods
    '''
    @api.multi
    def action_create_membership_invoice(self):
        res = self.env['account.invoice.mass.create'].mass_create_invoices()

        if 'invoices' in res:
            for association_member in self.partner.association_members:
                association_member.invoice = res['invoices'][self.partner.id]

        return res
    '''

    # 8. Business methods
