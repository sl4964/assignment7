import unittest
import MyPackage.interval as interval

# This is the TestInterval class containing unit tests for the constructor and other methods and functions.
class TestInterval(unittest.TestCase):

    def test_init(self):
        """
        Unit test for the constructor (including possible exceptions and invalid user inputs).
        """
        int1 = interval.interval('[1,3]')
        self.assertEqual(int1.lower_number, 1)
        self.assertEqual(int1.upper_number, 3)
        self.assertEqual(int1.lower_symbol, '[')
        self.assertEqual(int1.upper_symbol, ']')
        self.assertEqual(int1.interval, '[1,3]')
        self.assertEqual(int1.interval_to_list, ['[1','3]'])
        with self.assertRaises(ValueError):
            interval.interval(' ')
        with self.assertRaises(ValueError):
            interval.interval('[3 4]')
        with self.assertRaises(ValueError):
            interval.interval('foo')

    def test_eq(self):
        """
        Unit test for the __eq__ function.
        """
        self.assertTrue(interval.interval('[1,3]') == interval.interval('[1,3]'))
        self.assertFalse(interval.interval('(2,4]') == interval.interval('[1,9)'))

    def test_mergeIntervals(self):
        """
        Unit test for the mergeIntervals function and exception thrown (UnboundLocalError) when
        intervals cannot be merged.
        """
        int1, int2 = interval.interval('(8,10)'), interval.interval('[10,18)')
        int3, int4 = interval.interval('(7,10]'), interval.interval('(11,18]')
        merge_outcome = interval.mergeIntervals(int1, int2)
        self.assertEqual(merge_outcome, interval.interval('(8,18)'))
        with self.assertRaises(UnboundLocalError):
            interval.mergeIntervals(int3, int4)

    def test_mergeOverlapping(self):
        """
        Unit test for the mergeOverlapping function.
        """
        int1, int2, int3 = interval.interval('(1,3)'), interval.interval('[2,5)'), interval.interval('[5,8]')
        int4, int5, int6 = interval.interval('[1,2]'), interval.interval('(3,7]'), interval.interval('(7,8]')
        merge_outcome1 = interval.mergeOverlapping([int1, int2, int3])
        merge_outcome2 = interval.mergeOverlapping([int4, int5, int6])
        self.assertEqual(merge_outcome1, [interval.interval('(1,8]')])
        self.assertEqual(merge_outcome2, [interval.interval('[1,2]'), interval.interval('(3,8]')])

    def test_insert(self):
        """
        Unit test for the insert function.
        """
        interval_list1, int1 = [interval.interval('(4,7)'), interval.interval('[8,10)')], interval.interval('(11,13)')
        interval_list2, int2 = [interval.interval('[5,6]')], interval.interval('(6,10]')
        outcome1 = interval.insert(interval_list1, int1)
        outcome2 = interval.insert(interval_list2, int2)
        self.assertEqual(outcome1, [interval.interval('(4,7)'), interval.interval('[8,10)'), interval.interval('(11,13)')])
        self.assertEqual(outcome2, [interval.interval('[5,10]')])

if __name__ == '__main__':
    unittest.main()