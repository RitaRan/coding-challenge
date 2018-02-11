#!/usr/bin/env python3
import re
import time
from datetime import date

class Contribution(object):
	""" Process Each contribution"""


	def __init__(self, line):
		data = line.strip().split("|")

		self.recipient = data[0]
		self.donor = data[7]
		self.amount = data[14]
		self.otherid = data[15]

		self.zipcode = data[10]
		self.date= data[13]
		
		self.valid = True
		if self.otherid != '' or self.recipient == '' or self.donor == '' or self.amount == '' or (not self.valid_date()) or (not self.valid_zipcode()):
			self.valid = False
		if self.valid:
			self.zipcode = self.zipcode[:5]
			self.date= self.parse_date(data[13])

	def valid_date(self):
		valid = True
		try:
			time.strptime(self.date,"%m%d%Y")
		except:
			valid = False
		return valid

	def valid_zipcode(self):
		return len(self.zipcode) >= 5

	def parse_date(self, datestr):
		time_struct = time.strptime(datestr,"%m%d%Y")
		return date.fromtimestamp(time.mktime(time_struct))

	def get_recipientid(self):
		return self.recipient + self.zipcode + str(self.get_year())

	def get_recipient(self):
		return self.recipient

	def get_donorid(self):
		return self.donor + self.zipcode

	def get_donor(self):
		return self.donor

	def get_amount_num(self):
		return float(self.amount)

	def get_year(self):
		return self.date.year

	def get_zipcode(self):
		return self.zipcode

	def is_valid(self):
		return self.valid


