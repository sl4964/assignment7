'''
Created on Fri Nov 11 12:51:28 2016

@author: wxy
'''
import unittest
from class_interval import interval


class Test(unittest.TestCase):


    def setUp(self):
        pass
    
    def test_interval(self):
        self.assertEqual(interval("[1,4]").lower,1)
        self.assertEqual(interval("[1,4]").upper,4)
        self.assertEqual(interval("(2,5]").lower,3)
        self.assertEqual(interval("(2,5]").upper,5)
        self.assertEqual(interval("[4,8)").lower,4)
        self.assertEqual(interval("[4,8)").upper,7)
        self.assertEqual(interval("(3,9)").lower,4)
        self.assertEqual(interval("(3,9)").upper,8)
        
    
    def test_merge(self):
        self.assertEqual(interval.mergeIntervals(interval("[1,3]"), interval("[3,5]")),"[1,5]")
        self.assertEqual(interval.mergeIntervals(interval("[-1,4]"), interval("[2,3]")),"[-1,4]")
        self.assertEqual(interval.mergeIntervals(interval("[1,5]"), interval("[6,9]")),"[1,9]")
        
    
    def test_merge_overlap(self):
        self.assertEqual(interval.mergeOverlapping([interval("[1,5]"),interval("[2,6)"),interval("(8,10]"),interval("[8,18]")]), "[1,5], [8,18]") 
    
    def test_insert(self):
        self.assertEqual(interval.insert([interval("[1,3]"),interval("[6,9]")], interval("[2,5]")), "[1,9]")
        self.assertEqual(interval.insert([interval("[1,2]"),interval("(3,5)"),interval("[6,7)"),interval("(8,10]"),interval("[12,16]")], interval("[4,9]")), "[1,2], (3,10], [12,16]")

if __name__ == "__main__":
    unittest.main()