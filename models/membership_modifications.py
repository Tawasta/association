# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: 
#    Copyright 2015 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html.
#
##############################################################################

from openerp import api, fields, models

class MembershipModifications(models.Model):
	
	_inherit = 'res.partner'

	member_membership = fields.Char('Memberships', compute='compute_member_membership')	

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



class MembershipProductModifications(models.Model):
	_inherit = 'product.template'

	members_paid = fields.Integer('Number of members', default=0, compute='compute_members_paid')

	members_invoiced = fields.Integer('Invoiced members', default=0, compute='compute_members_invoiced')

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