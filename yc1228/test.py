import unittest
from interval import *
'''
Test class interval, function mergeIntervals, function mergeOverlapping, 
function insert
'''
class Test(unittest.TestCase):
    def test_interval(self):
        self.assertEqual('(1,5]', str(interval('(1, 5]')))
        self.assertEqual('[-10,-5]', str(interval('[-10, -5]' )))
        self.assertEqual('[0,15)', str(interval('[0, 15)')))
        self.assertEqual('(9,11)', str(interval('(9,11)')))
        
    def test_mergeintervals(self):
        int1 = interval("[1,5]")
        int2 = interval("[2,6]")
        int3 =  mergeIntervals(int1, int2)
        self.assertEqual(str(int3), "[1,6]")
        
    def test_mergeOverlapping(self):
        intervals = []
        intervals.append(interval("[1,5]"))
        intervals.append(interval("[2,6]"))
        intervals.append(interval("[9,10]"))
        self.assertEqual(str(intervals), "[[1,6], [9,10]]")
   
    def test_insert(self):
        intervals = []
        intervals.append(interval("[1,5]"))
        intervals.append(interval("[2,6]"))
        intervals.append(interval("[9,10]"))
        newint = interval("[8,11]")
        insert(intervals, newint)
        self.assertEqual(str(intervals), "[[1,6], [8,11]]")

if __name__ == "__main__":
    unittest.main()