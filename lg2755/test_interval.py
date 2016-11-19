import unittest
from Interval import InputTypeException, InputValueException, MergeException, Interval, mergeIntervals, mergeOverlapping, insert

class TestInterval(unittest.TestCase):

    def test_valid_interval(self):
        self.assertEqual(str(Interval('(2, 5)')),  '(2,5)')

    def test_invalid_interval(self):
        with self.assertRaises(InputTypeException):
            Interval(123)
    def test_mergeIntervals(self):
        self.assertEqual(str(mergeIntervals(Interval('(2, 5)'), Interval('[4, 6]'))), '[3,6]')

    def test_invalid_mergeInterval(self):
        with self.assertRaises(MergeException):
            mergeIntervals(Interval('(2, 4)'), Interval('(4, 6)'))

    def test_valid_insert(self):
        self.assertEqual(str(insert([Interval('[1,3]'), Interval('[6,9]')], Interval('[2,5]'))), '[[1,9]]')

if __name__ == '__main__':
    unittest.main()
