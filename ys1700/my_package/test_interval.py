'''
Created on Nov 14, 2016

@author: sunyifu
'''
import unittest
from interval import *


class Test(unittest.TestCase):


    def test_interval(self):
        self.assertEqual(str(interval('(2,4]')),'(2,4]')
        self.assertEqual(interval('[3,4)').actualupperbound,3)
        with self.assertRaises(InvalidIntervalError):
            interval('(3,3)')
            interval('[1,-1)')
    
    
    def test_mergeIntervals(self):
        self.assertEqual(str(mergeIntervals(interval('(2,10]'),interval('[10,18)'))),'(2,18)') 
        with self.assertRaises(IntervalMergeError):
            mergeIntervals(interval('(3,7]'),interval('[10,18)'))
            
    def test_mergeOverlapping(self):
        intervals = [interval('[1,2]'), interval('[2,3]'), interval('(3,5]'), interval('(7,8]')]
        testIntevals = [interval('[1,3]'), interval('(3,5]'), interval('(7,8]')]
        self.assertEqual(str(mergeOverlapping(intervals)),str(testIntevals))
        self.assertEqual(str(mergeOverlapping([interval('[1,2]'), interval('(2,3]')])),'[[1,2], (2,3]]') 
        
    def test_insert(self):
        intervals = [interval('[1,2]'), interval('[2,3]'), interval('(3,5]'), interval('(7,8]')]
        self.assertEqual(str(insert(intervals, interval('[3,8]'))), '[[1,8]]')   
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()