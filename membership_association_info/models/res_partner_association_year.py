# -*- coding: utf-8 -*-

# 1. Standard library imports:
import re

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp import _
from openerp.exceptions import ValidationError

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartnerAssociationYear(models.Model):

    # 1. Private attributes
    _name = 'res.partner.association.year'
    _order = 'name DESC'

    # 2. Fields declaration
    name = fields.Char("Year")

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges
    @api.constrains('name')
    def _validate_year(self):
        if not re.match(r'^[1,2][0-9]{3}$', self.name):
            msg = _("Please enter a valid year")
            raise ValidationError(msg)

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
