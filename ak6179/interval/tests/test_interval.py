"""
Unit tests for interval module.
For running the unit test use the command 'python -m unittest discover' in the netid (ak6179) directory.
The command will automatically discover unit tests and will run them.
"""
import unittest
from ..interval import *


class IntervalTest(unittest.TestCase):
    def test_interval_constructor(self):
        """Unit Tests for Interval class."""
        # test valid input interval strings
        interval1 = Interval("[1,4]")
        self.assertEqual(str(interval1), "[1,4]")
        interval2 = Interval("(2,5]")
        self.assertEqual(str(interval2), "(2,5]")
        interval3 = Interval("[4,8)")
        self.assertEqual(str(interval3), "[4,8)")

        # test where input interval has whitespace
        interval4 = Interval(" ( -3 , 9  ) ")
        self.assertEqual(str(interval4), "(-3,9)")
        interval5 = Interval(" (100, 200)  ")
        self.assertEqual(str(interval5), "(100,200)")

        # testing invalid input formats
        with self.assertRaises(ValueError):
            _ = Interval("foo")
        with self.assertRaises(ValueError):
            _ = Interval("(3,1]")
        with self.assertRaises(ValueError):
            _ = Interval("something from nothing")
        with self.assertRaises(ValueError):
            _ = Interval("")
        with self.assertRaises(ValueError):
            _ = Interval("[-5,-9]")
        with self.assertRaises(ValueError):
            _ = Interval("(101,102)")

    def test_merge_intervals(self):
        """Unit tests for merge_intervals function."""
        # testing closed intervals
        interval1 = Interval("[3,5]")
        interval2 = Interval("[4,10]")
        self.assertEqual(str(merge_intervals(interval1, interval2)), "[3,10]")
        self.assertEqual(str(merge_intervals(interval2, interval1)), "[3,10]")

        # testing combination of closed and open intervals
        interval3 = Interval("(5,10]")
        interval4 = Interval("(8,25)")
        self.assertEqual(str(merge_intervals(interval3, interval4)), "(5,25)")
        self.assertEqual(str(merge_intervals(interval4, interval3)), "(5,25)")

        # testing open intervals
        interval5 = Interval("(100,200)")
        interval6 = Interval("(150,500)")
        self.assertEqual(str(merge_intervals(interval5, interval6)), "(100,500)")
        self.assertEqual(str(merge_intervals(interval6, interval5)), "(100,500)")

        # testing merging of adjacent interval
        interval7 = Interval("[100,105]")
        interval8 = Interval("[105,108]")
        self.assertEqual(str(merge_intervals(interval7, interval8)), "[100,108]")

        # testing where the second interval occurs inside the first interval
        interval_a = Interval("[100,110)")
        interval_b = Interval("[105,106)")
        self.assertEqual(str(merge_intervals(interval_a, interval_b)), "[100,110)")

        # testing merging of non-intersecting and non-overlapping intervals
        with self.assertRaises(Exception):
            interval_c = Interval("[5, 99)")
            interval_d = Interval("[100, 500)")
            _ = merge_intervals(interval_c, interval_d)
        with self.assertRaises(Exception):
            interval_e = Interval("[-50, 50)")
            interval_f = Interval("[51, 100]")
            _ = merge_intervals(interval_e, interval_f)

    def test_get_intervals_list(self):
        """Unit tests for get_intervals_list function."""
        # testing the get_intervals list method
        interval_list = get_intervals_list("[1,5], [2,6), (8,10], [8,18]")
        self.assertEqual(str(interval_list), "[[1,5], [2,6), (8,10], [8,18]]")

        interval_list = get_intervals_list("[-10,-7], (-4,1], [3,6), (8,12), [15,23]")
        self.assertEqual(str(interval_list), "[[-10,-7], (-4,1], [3,6), (8,12), [15,23]]")

        interval_list = get_intervals_list("[1,2], (3,5), [6,7), (8,10], [12,20]")
        self.assertEqual(str(interval_list), "[[1,2], (3,5), [6,7), (8,10], [12,20]]")

        # using a different separator.
        interval_list = get_intervals_list("[1,2]#(3,5)#[6,7)#(8,10]#[12,20]", sep="#")
        self.assertEqual(str(interval_list), "[[1,2], (3,5), [6,7), (8,10], [12,20]]")

        # testing for empty list
        interval_list = get_intervals_list("")
        self.assertEqual(interval_list, [])

    def test_merge_overlapping(self):
        """Unit tests for merge_overlapping function."""
        # testing when overlapping intervals are merged
        interval_list = get_intervals_list("[1,5], [2,6), (8,10], [8,18]")
        merged_list = merge_overlapping(interval_list)
        self.assertEqual(str(merged_list), "[[1,5], [8,18]]")

        interval_list = get_intervals_list("[25,30], [50,55], [45,60], [55,100]")
        merged_list = merge_overlapping(interval_list)
        self.assertEqual(str(merged_list), "[[25,30], [45,100]]")

        interval_list = get_intervals_list("(1,100), (50,250), (200,505]")
        merged_list = merge_overlapping(interval_list)
        self.assertEqual(str(merged_list),"[(1,505]]")

        # testing when there are no overlapping intervals
        interval_list = get_intervals_list("[1,10], [20,30], (100,500), (800,1000]")
        merged_list = merge_overlapping(interval_list)
        self.assertEqual(str(merged_list), "[[1,10], [20,30], (100,500), (800,1000]]")

        interval_list = get_intervals_list("[50,100], [102,500), [505,800]")
        merged_list = merge_overlapping(interval_list)
        self.assertEqual(str(merged_list),"[[50,100], [102,500), [505,800]]")

    def test_insert(self):
        """Unit tests for insert function."""
        list1 = get_intervals_list("[-10,-7], (-4,1], [3,6), (8,12), [15,23]")
        updated_list = insert(list1, Interval("[4,8]"))
        self.assertEqual(str(updated_list), "[[-10,-7], (-4,1], [3,12), [15,23]]")
        updated_list = insert(updated_list, Interval("[24,24]"))
        self.assertEqual(str(updated_list), "[[-10,-7], (-4,1], [3,12), [15,24]]")
        updated_list = insert(updated_list, Interval("[12,13)"))
        self.assertEqual(str(updated_list), "[[-10,-7], (-4,1], [3,13), [15,24]]")
        updated_list = insert(updated_list, Interval("(2,12)"))
        self.assertEqual(str(updated_list), "[[-10,-7], (-4,1], (2,13), [15,24]]")
        updated_list = insert(updated_list, Interval("(-7,-2]"))
        self.assertEqual(str(updated_list), "[[-10,1], (2,13), [15,24]]")
        updated_list = insert(updated_list, Interval("[-2,5]"))
        self.assertEqual(str(updated_list), "[[-10,13), [15,24]]")

        list2 = get_intervals_list("[1,3], [6,9]")
        updated_list = insert(list2, Interval("[2,5]"))
        self.assertEqual(str(updated_list), "[[1,9]]")
        updated_list = insert(updated_list, Interval("[100,500]"))
        self.assertEqual(str(updated_list), "[[1,9], [100,500]]")
        # testing the case when there are no overlapping intervals
        updated_list = insert(updated_list, Interval("[150, 1005]"))
        self.assertEqual(str(updated_list), "[[1,9], [100,1005]]")

        list3 = get_intervals_list("[1,2], (3,5), [6,7), (8,10], [12,16]")
        updated_list = insert(list3, Interval("[4,9]"))
        self.assertEqual(str(updated_list), "[[1,2], (3,10], [12,16]]")
        # Testing inserting adjacent interval
        updated_list = insert(updated_list, Interval("[17,17]"))
        self.assertEqual(str(updated_list), "[[1,2], (3,10], [12,17]]")
        updated_list = insert(updated_list, Interval("[9, 15]"))
        self.assertEqual(str(updated_list), "[[1,2], (3,17]]")
