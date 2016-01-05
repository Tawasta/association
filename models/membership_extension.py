# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports (One per line sorted and splitted in python stdlib):

# 3. Odoo imports (openerp):
from openerp import api, fields, models, _

# 4. Imports from Odoo modules (rarely, and only if necessary):

# 5. Local imports in the relative form:

# 6. Unknown third party imports (One per line sorted and splitted in python stdlib):


class MembershipModifications(models.Model):
	
	# 1. Private attributes
	_inherit = 'res.partner'

	# 2. Fields declaration
	member_membership = fields.Char(_("Memberships"), compute='compute_member_membership')	

	# 3. Default methods

	# 4. Compute and search fields, in the same order that fields declaration
	@api.one
	def compute_member_membership(self):
		
		lines = self.member_lines
		membership = ""
		state = ""
		for i in range(0, len(lines)):

			membership += lines[i].membership_id.name + " ("
			state = lines[i].state if lines[i].state else "-"
			membership += state + ")"

			if i + 1 < len(lines):
				membership += "\n"

		self.member_membership = membership

	# 5. Constraints and onchanges

	# 6. CRUD methods

	# 7. Action methods

	# 8. Business methods


class MembershipProductModifications(models.Model):

	# 1. Private attributes
	_inherit = 'product.template'

	# 2. Fields declaration
	members_paid = fields.Integer('Number of members', default=0, compute='compute_members_paid')
	members_invoiced = fields.Integer('Invoiced members', default=0, compute='compute_members_invoiced')
	membership_product_id = fields.Integer('Id of membership product', compute='compute_membership_product_id')
	
	# 3. Default methods	

	# 4. Compute and search fields, in the same order that fields declaration
	@api.one
	def compute_members_paid(self):

		count_paid = self.env['membership.membership_line'].search_count([('membership_id',
			'=', self.name), ('state', '=', 'paid')])
		
		self.members_paid = count_paid
		

	@api.one
	def compute_members_invoiced(self):

		count_invoiced = self.env['membership.membership_line'].search_count([('membership_id',
			'=', self.name), ('state', '=', 'invoiced')])

		self.members_invoiced = count_invoiced


	@api.one
	def compute_membership_product_id(self):

		line = self.env['membership.membership_line'].search([('membership_id',
			'=', self.name)])
		if len(line) > 1:
			self.membership_product_id = line[0].membership_id.id
		else:
			self.membership_product_id = line.membership_id.id

	# 5. Constraints and onchanges

	# 6. CRUD methods

	# 7. Action methods

	# 8. Business methods