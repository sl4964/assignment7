'''
Created on 2016年11月10日

@author: bz866
'''

from Interval_assignment.interval import *
import unittest

class Test(unittest.TestCase):
    def test_valid(self):
        """ test for interval function, test the range of integers it represents"""
        int1 = interval("[-8,-6]")
        int2 = interval("(-4,1]")
        int3 = interval("[4,8)")
        int4 = interval("(3,6)")

        self.assertEqual(int1.comma_interval, [-8,-7,-6])
        self.assertEqual(int2.comma_interval, [-3, -2, -1, 0, 1])
        self.assertEqual(int3.comma_interval, [4, 5, 6, 7])
        self.assertEqual(int4.comma_interval, [4, 5])

    def test_invalidsample(self):
        """ test for invalid interval input"""

        with self.assertRaises(ValueError):
            interval("1234")
        with self.assertRaises(ValueError):
            interval("(2,2)")
        with self.assertRaises(ValueError):
            interval("[4,1)")

    def test_mergeable(self):
        """test the mergeInterval function which successfully processed """

        int1 = interval("(1,5]")
        int2 = interval("(3,5]")
        int3 = interval("[4,9]")
        int4 = interval("(8,10]")
        int5 = interval("[10,18]")

        self.assertEqual(str(interval("(1,5]")), str(mergeIntervals(int1, int2)))
        self.assertEqual(str(interval("(3,9]")), str(mergeIntervals(int2, int3)))
        self.assertEqual(str(interval("[4,10]")), str(mergeIntervals(int3, int4)))
        self.assertEqual(str(interval("(8,18]")), str(mergeIntervals(int4, int5)))

    def test_merge_fail(self):
        """test the mergeInterval function which can't be merged """

        int1 = interval("(1,2]")
        int2 = interval("(3,5]")
        int3 = interval("[7,9]")
        int4 = interval("(10,12]")
        int5 = interval("[18,18]")

        with self.assertRaises(ValueError):
            self.interval = mergeIntervals(int1, int2)

        with self.assertRaises(ValueError):
            self.interval = mergeIntervals(int2, int3)

        with self.assertRaises(ValueError):
            self.interval = mergeIntervals(int3, int4)

        with self.assertRaises(ValueError):
            self.interval = mergeIntervals(int4, int5)

    def test_mergeOverlapping(self):
        """test the mergeOverlapping function"""
        int1 = interval("[1,6)")
        int2 = interval("[2,6)")
        int3 = interval("(8,10]")
        int4 = interval("[8,18]")
        interval_for_merge = [int1, int2, int3, int4]

        merged_list = [interval("[1,6)"), interval("[8,18]")]
        self.assertEqual(str(mergeOverlapping(interval_for_merge)), str(merged_list))

    def test_insert(self):
        """test the insert function"""
        int1 = interval('[1,2]')
        int2 = interval("(3,5)")
        int3 = interval("[6,7)")
        int4 = interval("(8,10]")
        int5 = interval("[12,16]")

        intervals_l = [int1, int2, int3, int4, int5]
        newint = interval("[4,9]")

        self.assertEqual(str(insert(intervals_l, newint)), str([interval("[1,2]"), interval("(3,10]"), interval("[12,16]")]))


if __name__ == "__main__":
    unittest.main() 