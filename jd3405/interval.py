# Solution for DS-GA 1007 Assignment#7
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science
from errors import *

class interval:
	def __init__(self, s):
		"""Check whether the string is valid, and then create the class"""
		tokens = s.split(",")
		# conditions that not valid
		if len(tokens) != 2:
			raise IntervalException
		if len(tokens[0]) < 2 or len(tokens[1]) < 2:
			raise IntervalException
		if tokens[0][0] != '(' and tokens[0][0] != '[':
			raise IntervalException
		if tokens[1][-1] != ')' and tokens[1][-1] != ']':
			raise IntervalException
		# get out the parts for the class
		self.lower = int(tokens[0][1:])
		self.upper = int(tokens[1][:-1])
		self.lower_brac = tokens[0][0]
		self.upper_brac = tokens[1][-1]
		# use lower_bound and upper_bound to indicate the 
		if self.lower_brac == '[':
			lower_bound = self.lower
		else:
			lower_bound = self.lower + 0.1
		if self.upper_brac == ']':
			upper_bould = self.upper
		else:
			upper_bould = self.upper - 0.1
		if lower_bound > upper_bould:
			raise IntervalException

	def __repr__(self):
		"""Return the string representation"""
		return self.lower_brac + str(self.lower) + "," + str(self.upper) + self.upper_brac
