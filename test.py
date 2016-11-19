import unittest
from interval import *

"""Test class inveral and main program"""
class Test(unittest.TestCase):
    def test_interval(self):
        self.assertEqual("(4,6]", str(interval("(4, 6]")))
        self.assertEqual("[0,3)", str(interval("[0, 3)")))
        self.assertEqual("[-1,5]", str(interval("[-1, 5]" )))
        self.assertEqual("(11,14)", str(interval("(11,14)")))

    def test_mergeIntervals(self):
        int1 = interval("[-2,5]")
        int2 = interval("[4,8]")
        new =  mergeIntervals(int1, int2)
        self.assertEqual(str(new),"[-2,8]" )

    def test_MergeOverlapping(self):
        intervals = []
        intervals.append(interval("[1,3]"))
        intervals.append(interval("[2,9]"))
        intervals.append(interval("[11,14]"))
        self.assertEqual(str(intervals), "[[1,9], [11,14]]")

    def test_insert(self):
        intervals = []
        intervals.append(interval("[1,3]"))
        intervals.append(interval("[2,7]"))
        intervals.append(interval("[6,14]"))
        newint = interval("[18,20]")
        insert(intervals, newint)
        self.assertEqual(str(intervals,"[[1,14], [18,20]]" )

if __name__ == "__main__":
    unittest.main()
