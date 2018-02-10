#!/usr/bin/env python3
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
		if self.otherid != '' or self.recipient == '' or self.donor == '' or self.amount == '' or self.date == '' or (not self.valid_date()):
			self.valid = False
		if self.valid:
			self.zipcode = self.parse_zipcode(data[10])
			self.date= self.parse_date(data[13])

	def valid_date(self):
		valid = True
		try:
			time.strptime(self.date,"%m%d%Y")
		except:
			valid = False
		return valid

	def parse_zipcode(self, zipcodestr):
		if len(zipcodestr)<5:
			self.valid = False
			return ""
		return zipcodestr[:5]

	def parse_date(self, datestr):
		if len(datestr)!=8:
			self.valid = False
			return ""
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


