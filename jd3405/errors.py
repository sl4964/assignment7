# Solution for DS-GA 1007 Assignment#7
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science

class IntervalException(Exception):
	def __str__(self):
		"""Return the error message"""
		return "interval input error\n"

class IntervalMergeException(Exception):
	def __str__(self):
		"""Return the error message"""
		return "interval merge error\n"
