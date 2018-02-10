#!/usr/bin/env python3

		
class Donors(object):
	"""docstring for Donors"""
	def __init__(self):
		self.donor_dict = {}
		
	def add_donor(self, contrib):
		"""add donor into the database and return if the donor is a repeat donor"""
		donor = contrib.get_donorid()
		year = contrib.get_year()

		if self.exist_donor(donor):
			is_repeat = self.add_donor_ifexist(donor,year)
		else:
			is_repeat = self.add_donor_ifnotexist(donor,year)

		return is_repeat

	def exist_donor(self, donor):
		return donor in self.donor_dict

	def add_donor_ifexist(self, donor, year):
		curr_year = self.donor_dict[donor]
		is_repeat = False

		if curr_year < year:
			is_repeat = True
		elif curr_year > year:
			self.donor_dict[donor] = year

		return is_repeat


	def add_donor_ifnotexist(self, donor, year):
		is_repeat = False
		self.donor_dict[donor] = year

		return is_repeat