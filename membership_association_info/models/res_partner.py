# -*- coding: utf-8 -*-

# 1. Standard library imports:
from datetime import datetime

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp import _
from openerp.exceptions import ValidationError

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):

    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration
    association_status = fields.Selection([
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('resigned', 'Resigned'),
        ],
        'Status',
        default='active'
    )
    association_status_date_change = fields.Date('Stage change')

    association_date_join = fields.Date('Join date')
    association_date_founding = fields.Date('Founding date')
    association_category = fields.Many2one('res.partner.association.category', 'Category')
    association_type = fields.Many2one('res.partner.association.type', 'Type')

    association_members = fields.One2many(
        'res.partner.association.members',
        'partner',
        'Members',
        domain=[('year.name', '=', datetime.today().year)],
    )
    association_members_history = fields.One2many(
        'res.partner.association.members',
        'partner',
        'Members history',
        domain=[('year.name', '!=', datetime.today().year)],
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.onchange('association_status')
    def onchange_association_status(self):
        self.association_status_date_change = fields.Date.today()

    @api.constrains('association_members')
    def _validate_association_members(self):
        for record in self:
            for line in record.association_members:
                existing = record.env['res.partner.association.members'].search([
                    ('year', '=', line.year.id),
                    ('name', '=', line.name.id),
                ], limit=1)

                if existing:
                    overlapping = "%s/%s" % (existing.name.name, existing.year.name)
                    msg = _("Please don't create overlapping records: %s") % overlapping
                    raise ValidationError(msg)

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
