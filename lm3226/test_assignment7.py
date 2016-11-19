import unittest
from assignment7 import *

class test_interval(unittest.TestCase):
    def test_interval_class(self):
        with self.assertRaises(InvalidUserInputException):
            interval(3)
        with self.assertRaises(InvalidUserInputException):
            interval("asdfg")

        with self.assertRaises(InvalidIntervalException):
            interval('[5, 4]')
        with self.assertRaises(InvalidIntervalException):
            interval('(2, 3)')

        paren_int = interval('(0, 5)')
        self.assertEqual(paren_int.left, 1, 'Error: interval() does not correctly handle left parens')
        self.assertEqual(paren_int.right, 4, 'Error: interval() does not correctly handle right parens')

        bracket_int = interval('[0, 5]')
        self.assertEqual(bracket_int.left, 0, 'Error: interval() does not correctly handle left brackets')
        self.assertEqual(bracket_int.right, 5, 'Error: interval() does not correctly handle right brackets')

        test_interval = interval('(6,15]')
        self.assertEqual(repr(test_interval), '(6,15]', 'Error: interval does not print with same form as input')
        self.assertEqual(test_interval.string_represenation, '(6,15]', 'Error: string_represenation is not same as input')

        self.assertTrue(interval('[7, 10]') == interval('(6, 11)'), 'Error: __eq__ does not treat equal intervals as equal')
        self.assertFalse(interval('[7, 10]') == interval('[8, 9]'), 'Error: __eq__ treats unequal intervals as equal')

        self.assertFalse(interval('[7, 10]') != interval('(6, 11)'), 'Error: __ne__ does not treat equal intervals as equal')
        self.assertTrue(interval('[7, 10]') != interval('[8, 9]'), 'Error: __ne__ treats unequal intervals as equal')


    def test_mergeIntervals(self):
        test_result = mergeIntervals(interval('[1,5]'), interval('[2,6]'))
        expected_result = interval('[1,6]')
        self.assertEqual(test_result, expected_result, 'Error: mergeIntervals() does not merge overlapping intervals')

        test_result = mergeIntervals(interval('[1, 2]'), interval('[3, 4]'))
        expected_result = interval('[1,4]')
        self.assertEqual(test_result, expected_result, 'Error: mergeIntervals() does not merge adjacent intervals')

        test_result = mergeIntervals(interval('[1, 2]'), interval('[4, 5]'))
        self.assertEqual(test_result, None, 'Error: mergeIntervals() does not return None when there is no merge')


    def test_mergeOverlapping(self):
        intervals = [interval('[1,5]'), interval('[2,6)'), interval('(8,10]'), interval('[8,18]')]
        test_result = mergeOverlapping(intervals)
        expected_result = [interval('[1,6)'), interval('[8,18]')]
        self.assertEqual(test_result, expected_result, 'Error: mergeOverlapping() does not merge overlapping intervals correctly when there is overlapping.')

        intervals = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
        test_result = mergeOverlapping(intervals)
        expected_result = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
        self.assertEqual(test_result, expected_result, 'Error: mergeOverlapping() does not merge overlapping correctly when there is no overlappig.')

    def test_insert(self):
        intervals_list = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
        test_result = insert(intervals_list, interval('[4,9]'))
        expected_result = [interval('[1,2]'), interval('(3,10]'), interval('[12,16]')]
        self.assertEqual(test_result, expected_result, 'Error: insert() does not insert interval correctly when there is overlapping.')

        intervals_list = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
        test_result = insert(intervals_list, interval('[19,20]'))
        expected_result = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]'), interval('[19,20]')]
        self.assertEqual(test_result, expected_result, 'Error: insert() does not insert correctly when there is no overlapping.')

if __name__ == '__main__':
    unittest.main()
