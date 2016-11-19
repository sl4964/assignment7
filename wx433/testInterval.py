import unittest
from interval import Interval

class TestInterval(unittest.TestCase):
	
	def test_instance(self):
		int_1 = Interval("[2, 4)")
		self.assertTrue(int_1)
		self.assertEqual(int_1.lower, 2)
		self.assertEqual(int_1.upper, 4)
		self.assertEqual(int_1.lowerBound, "[")
		self.assertEqual(int_1.upperBound, ")")

	def test_mergeIntervals(self):
		int_1 = "[4, 9)"
		int_2 = "(5, 12]"
		result = Interval.mergeIntervals(int_1, int_2)
		self.assertTrue(result)
		self.assertEqual(result.lower, 4)
		self.assertEqual(result.upper, 12)
		self.assertEqual(result.lowerBound, "[")
		self.assertEqual(result.upperBound, "]")

	def test_mergeOverlapping(self):
		input_1 = '[1, 9), (-9, -6], [6, 12), [24, 36), [12, 16]'
		result = Interval.mergeOverlapping(input_1)
		int_1 = result[0]
		int_2 = result[1]
		int_3 = result[2]
		self.assertTrue(int_1)
		self.assertEqual(int_1.lower, -9)
		self.assertEqual(int_1.upper, -6)
		self.assertEqual(int_1.lowerBound, "(")
		self.assertEqual(int_1.upperBound, "]")
		self.assertTrue(int_2)
		self.assertEqual(int_2.lower, 1)
		self.assertEqual(int_2.upper, 16)
		self.assertEqual(int_2.lowerBound, "[")
		self.assertEqual(int_2.upperBound, "]")
		self.assertTrue(int_1)
		self.assertEqual(int_3.lower, 24)
		self.assertEqual(int_3.upper, 36)
		self.assertEqual(int_3.lowerBound, "[")
		self.assertEqual(int_3.upperBound, ")")

	def test_insert(self):
		input_1 = '(-9, -6], [1, 16], [24, 36)'
		input_2 = '(16, 24)'
		result = Interval.insert(input_1, input_2)
		int_1 = result[0]
		int_2 = result[1]
		self.assertTrue(int_1)
		self.assertEqual(int_1.lower, -9)
		self.assertEqual(int_1.upper, -6)
		self.assertEqual(int_1.lowerBound, "(")
		self.assertEqual(int_1.upperBound, "]")
		self.assertTrue(int_2)
		self.assertEqual(int_2.lower, 1)
		self.assertEqual(int_2.upper, 36)
		self.assertEqual(int_2.lowerBound, "[")
		self.assertEqual(int_2.upperBound, ")")




if __name__ == '__main__':
    unittest.main(exit=False)