# Solution for DS-GA 1007 Assignment#7
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science

from errors import *
from interval import interval

def mergeIntervals(int1, int2):
	"""Merge two intervals and return the merged interval"""
	# first check whether they are mergeable
	if not isMergeable(int1, int2):
		raise IntervalMergeException
	# use a new string to create the new class
	new_interval_str = ""
	# when lower bounds are equal, if there exists '[', use '[', else use '('
	if int1.lower == int2.lower:
		if int1.lower_brac == '[' or int2.lower_brac == '[':
			new_interval_str += '['
		else:
			new_interval_str += '('
		new_interval_str += str(int1.lower)
	else:
		# when one is smaller than another, use the smaller one
		if int1.lower < int2.lower:
			new_interval_str += int1.lower_brac + str(int1.lower)
		else:
			new_interval_str += int2.lower_brac + str(int2.lower)
	new_interval_str += ','
	# when upper bound are equal, if there exists "]" use "]", else use ")"
	if int1.upper == int2.upper:
		new_interval_str += str(int1.upper)
		if int1.upper_brac == ']' or int2.upper_brac == ']':
			new_interval_str += ']'
		else:
			new_interval_str += ')'
	else:
		# when one is greater than another, use the greater one
		if int1.upper > int2.upper:
			new_interval_str += str(int1.upper) + int1.upper_brac
		else:
			new_interval_str += str(int2.upper) + int2.upper_brac
	return interval(new_interval_str)


def isMergeable(int1, int2):
	"""Check whether two intervals as mergeable"""
	# left or right
	if int1.upper < int2.lower or int2.upper < int1.lower:
		return False
	# one bound is equal
	if (int1.upper_brac == ')' and int2.lower_brac == '(') and int1.upper == int2.lower:
		return False
	if (int2.upper_brac == ')' and int1.lower_brac == '(') and int2.upper == int1.lower:
		return False
	return True


def mergeOverlapping(intervals):
	"""Merge the overlapping intervals in the array"""
	if len(intervals) == 0:
		return
	intervals.sort(key=lambda a: a.lower)
	l = 0
	# for each time, merge interval i with one interval j > i
	# until it can not be merged
	while l < len(intervals) - 1:
		merged = False
		for i in range(l + 1, len(intervals)):
			if isMergeable(intervals[l], intervals[i]):
				intervals[l] = mergeIntervals(intervals[l], intervals[l + 1])
				intervals.pop(l + 1)
				merged = True
				break
		if not merged:
			l += 1


def insert(intervals, newint):
	"""Insert one interval into the array and merge the overlapping ones"""
	merged = True
	# for each time, we merge the new interval and one of the intervals in the array
	# until it can not be merged
	while merged:
		merged = False
		for i in range(len(intervals)):
			if isMergeable(newint, intervals[i]):
				newint = mergeIntervals(newint, intervals[i])
				intervals.pop(i)
				merged = True
				break
	intervals.append(newint)
	intervals.sort(key=lambda a: a.lower)


def main():
	line = input("List of intervals? ")
	tokens = line.split(", ")
	intervals = []
	for token in tokens:
		intervals.append(interval(token))
	while True:
		input_str = input("Interval? ")
		if input_str == "quit":
			break
		try:
			newint = interval(input_str)
			insert(intervals, newint)
			result = ""
			for i in range(len(intervals)):
				if i > 0:
					result += ", "
				result += str(intervals[i])
			print(result)
		except IntervalException:
			print("Invalid interval")


if __name__ == "__main__":
	main()
