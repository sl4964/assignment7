# Solution for DS-GA 1007 Assignment#7
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science

import unittest
from assignment7 import *

class SimpleTest(unittest.TestCase):

	def testIntervalInit(self):
		test_str = "[1,5]"
		int1 = interval(test_str)
		self.assertEqual(test_str, str(int1))

	def testIsMergeable1(self):
		int_str1 = "[1,5]"
		int_str2 = "[6,8]"
		int1 = interval(int_str1)
		int2 = interval(int_str2)
		self.assertEqual(False, isMergeable(int1, int2))

	def testIsMergeable2(self):
		int_str1 = "[1,5]"
		int_str2 = "[4,8]"
		int1 = interval(int_str1)
		int2 = interval(int_str2)
		self.assertEqual(True, isMergeable(int1, int2))

	def testMergeIntervals(self):
		int1 = interval("[1,5]")
		int2 = interval("[2,6]")
		int3 = mergeIntervals(int1, int2)
		self.assertEqual(str(int3), "[1,6]")

	def testMergeOverLapping(self):
		intervals = []
		intervals.append(interval("[1,5]"))
		intervals.append(interval("[2,6]"))
		intervals.append(interval("[9,10]"))
		mergeOverlapping(intervals)
		self.assertEqual(str(intervals), "[[1,6], [9,10]]")	

	def testInsert(self):
		intervals = []
		intervals.append(interval("[1,3]"))
		intervals.append(interval("[5,7]"))
		intervals.append(interval("[9,10]"))
		newint = interval("[2,6]")
		insert(intervals, newint)
		self.assertEqual(str(intervals), "[[1,7], [9,10]]")


if __name__ == "__main__":
	unittest.main()