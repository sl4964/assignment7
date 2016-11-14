import unittest
from interval import interval
from functions import *

class SimpleTest(unittest.TestCase):
	def setUp(self):
		self.testinterval = interval
	def test_ClassInterval(self):
		self.assertEqual(str(self.testinterval('[2,8)')), '[2,8)')

	def test_isOverlapping(self):
		int1 = interval('[1,6)')
		int2 = interval('(4,7]')
		int3 = interval('[1,4)')
		int4 = interval('(4,7]')
		self.assertTrue(isOverlapping(int1, int2))
		self.assertFalse(isOverlapping(int3, int4))

	def test_mergeIntervals(self):
		int1 = interval('[2,6)')
		int2 = interval('(4,7]')
		intm1 = mergeIntervals(int1,int2)
		int3 = interval('[5,11]')
		int4 = interval('[12,14]')
		intm2 = mergeIntervals(int3,int4)
		self.assertEqual(str(intm1), '[2,7]')
		self.assertEqual(str(intm2), '[5,14]')

	def test_mergeOverlapping(self):
		int1 = interval('[2,6)')
		int2 = interval('(4,7]')
		int3 = interval('[8,10)')
		intervals = [int1,int2,int3]
		self.assertEqual(str(mergeOverlapping(intervals)), "[[2,10)]")

	def test_insert(self):
		int1 = interval('[2,6)')
		int2 = interval('(4,7]')
		int3 = interval('[9,12)')
		intervals = [int1,int2,int3]
		newint = interval('(11,16)')
		self.assertEqual(str(insert(intervals,newint)),"[[2,7], [9,16)]")

if __name__=="__main__":
	unittest.main()

