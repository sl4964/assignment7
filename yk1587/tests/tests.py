import unittest
from interval import *

class SimpleTest(unittest.TestCase):
    def setUp(self):
        '''interval for test setup'''
        self.testInterval = interval
    
    def test_interval(self):
        '''unit test for class interval'''
        self.assertEqual(str(self.testInterval('(1,7]')), '(1,7]')
        with self.assertRaises(ValueError):
             self.testInterval('(3,4)')
    
    def test_mergeIntervals(self):
        '''unit test for function mergeIntervals()'''
        interval1 = self.testInterval('[1,5]')
        interval2 = self.testInterval('[2,6)')
        self.assertEqual(mergeIntervals(interval1, interval2), '[1,6)')
        
        interval3 = self.testInterval('(2,4)')
        interval4 = self.testInterval('[5,6]')
        with self.assertRaises(ValueError):
         mergeIntervals(interval3, interval4)
    
    def test_mergeOverlapping(self):
        '''unit test for function mergeOverlapping'''
        intervals = ['[1,5]', '[2,6)', '[8,18]', '(8,10]']
        self.assertEqual(mergeOverlapping(intervals), ['[1,6)', '[8,18]'])
    
    def test_insert(self):
        '''unit test for function insert'''
        intervals = ['[-10,-7]', '(-4,1]', '[3,6)', '(8,12)', '[15,23]']
        newint = '[4,8]'
        self.assertEqual(insert(intervals, newint), ['[-10,-7]', '(-4,1]', '[3,12)', '[15,23]'])

if __name__ == '__main__':
    unittest.main()
