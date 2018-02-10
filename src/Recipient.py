#!/usr/bin/env python3
from heapq import *
from math import ceil

class Contribution_History(object):
	def __init__(self, percentile):
		self.percentile = percentile

		self.lower = []
		self.upper = []
		
		self.count = 0
		self.total_amount = 0

	def add_amount(self, amount):
		"""
		Add the amount to the current recipient's current year heap, return the percentile amount
		"""
		
		last_count = self.count
		last_index = self.get_perc_index(last_count)

		# add count
		self.count += 1
		curr_count = self.count
		curr_index = self.get_perc_index(curr_count)

		# add total amount
		self.total_amount += amount

		# update lower & upper heap for getting percentile
		if self.heapempty_lower():
			self.heappush_lower(amount)
		
		else:
			if curr_index > last_index:
				if self.heapempty_upper():
					self.heappush_lower(amount)
				elif amount > self.heaptop_upper():
					self.heappush_upper(amount)
					self.heappush_lower(self.heappop_upper())
				else:
					self.heappush_lower(amount)
			elif curr_index == last_index:
				if amount < self.heaptop_lower():
					self.heappush_lower(amount)
					self.heappush_upper(self.heappop_lower())
				else:
					self.heappush_upper(amount)

		perc_amount = self.heaptop_lower()
		return perc_amount

	def get_count(self):
		return self.count

	def get_total_amount(self):
		return self.total_amount

	def get_total_count(self):
		return self.count	

	def get_perc_index(self, count):
		return ceil(self.percentile/100*count)

	def heapempty_upper(self):
		return len(self.upper) == 0

	def heaptop_upper(self):
		return self.upper[0]

	def heappop_upper(self):
		return heappop(self.upper)

	def heappush_upper(self, amount):
		heappush(self.upper, amount)

	def heapempty_lower(self):
		return len(self.lower) == 0

	def heaptop_lower(self):
		return -self.lower[0]

	def heappop_lower(self):
		return -heappop(self.lower)

	def heappush_lower(self, amount):
		heappush(self.lower, -amount)

class Recipients(object):
	def __init__(self, percentile):
		self.recipient_dict = {}
		self.percentile = percentile


	def add_recipient(self, contrib):
		"""
		Add the recipient info to the recipients' list, and return the output 
		"""
		uniqueid = contrib.get_recipientid()
		amount = contrib.get_amount_num()
		year = contrib.get_year()

		if not self.exist_recipient(uniqueid):
			self.recipient_dict[uniqueid] = Contribution_History(self.percentile)

		contrib_history = self.recipient_dict[uniqueid]
		perc_amount = contrib_history.add_amount(amount)
		total_amount = contrib_history.get_total_amount()
		total_count = contrib_history.get_total_count()

		printout = []
		printout.append(contrib.get_recipient())
		printout.append(contrib.get_zipcode())
		printout.append(year)
		printout.append(perc_amount)
		printout.append(total_amount)
		printout.append(total_count)

		return self.print_to_format(printout)

	def exist_recipient(self, recipient):
		return recipient in self.recipient_dict

	def print_to_format(self, lst):
		lst[0] = str(lst[0])
		lst[1] = str(lst[1])
		lst[2] = str(lst[2])
		lst[5] = str(lst[5])

		val = lst[3]
		if (float(val) % 1) >= 0.5:
		    x = math.ceil(val)
		else:
		    x = round(val)
		lst[3] = str(x)

		val = lst[4]
		rem = val%1
		if rem:
			x = val
		else:
			x = int(val)
		lst[4] = str(x)

		return '|'.join(lst)