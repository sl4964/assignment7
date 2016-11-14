'''
Created on Nov 14, 2016

@author: ChuanYa Hsu
'''

from Interval.Interval import *
import unittest
from pkg_resources import invalid_marker

class Test_interval(unittest.TestCase):
    
    """
    Unit-testing class that lets us to run tests with expected
    outcomes.
    """
    
    def test_validinterval(self):
        
        """
        unit tests for the interval constructor
        Test the creation of valid inputs to the Interval constructor.
        """
        
        validinterval = ['[1,2]', '(2,5)', '[1,3)','(5,7]', #intervals with [],(),[),(]
                         '[-3,-1]','[-4,-1)','(-5,-2]','(-6,-3)', #intervals with negative numbers 
                         '[1,1]','[-1,-1]', 
                         '[ 0,    1]','[1,   2]','   [ 3,  4  ]  ', #intervals with spaces
                         '[00,+11]' #intervals leading with 0 or symbol
                         ]
        intervals = [interval(item) for item in validinterval]
        
        self.assertEqual(len(validinterval), len(intervals))
    
    def test_invalidinterval(self):
        
        """
        unit tests for the interval constructor
        Test the creation of invalid inputs to the Interval constructor.
        """
        
        invalid_interval = ['[a,1]', 'b', '[1,2][', '', '()', '(1,1)', '(3,4)']
        intervals = []
        for item in intervals:
            with self.assertRaises(InvalidIntervals):
                self.interval = interval(item)
                
    def test_mergeIntervals_success(self):
        
        """
        unit tests for mergeIntervals function
        Test function mergeIntervals could merge correctly when two input 
        overlap or adjacent
        """
        
        int1 = interval('[1,2]')
        int2 = interval('[2,3]')
        int3 = interval('(2,4]')
        int4 = interval('[0,4]')
        int5 = interval('[3,7]')
        
        int12 = interval('[1,3]')
        merge12 = mergeIntervals(int1, int2)
        self.assertEqual(int12, merge12)
        
        int13 = interval('[1,4]')
        merge13 = mergeIntervals(int1, int3)
        self.assertEqual(int13, merge13)
        
        int14 = interval('[0,4]')
        merge14 = mergeIntervals(int1, int4)
        self.assertEqual(int14, merge14)
        
        int45 = interval('(2,7]')
        merge45 = mergeIntervals(int4, int5)
        self.assertEqual(int45, merge45)
        
    def test_mergeIntervals_fail(self):
        
        """
        unit tests for mergeIntervals function
        Test function mergeIntervals could not be merged
        """
        
        int1 = interval('[1,2)')
        int2 = interval('[-2,-1]')
        int3 = interval('(2,5]')
        
        with self.assertRaises(IntervalsNotOverlap):
            self.interval = mergeIntervals(int1, int2)
            
        with self.assertRaises(IntervalsNotOverlap):
            self.interval = mergeIntervals(int1, int3)
            
        with self.assertRaises(IntervalsNotOverlap):
            self.interval = mergeIntervals(int2, int3)
    
    def test_mergeOverlapping(self):
        
        """
        unit tests for mergeOverlapping function
        Test function mergeOverlapping could merge correctly
        """
        
        intlist = [interval('[1,2]'), interval('[2,3]'), interval('[-1,-2]'), interval('(4,8]'), interval('[10,20]')]
        
        #expected return list of intervals after calling mergeOverlapping function
        mergelist = [interval('[-1,3]'), interval('(4,8]'), interval('[10,20]')]
        
        self.assertEqual(mergeOverlapping(intlist), mergelist)
    
    def test_Insert(self):
        
        """
        unit tests for insert function that insert an interval to an insert list successfully
        """
        
        intlist = [interval('[-1,2]'), interval('(3, 7]'), interval('[10,20]')]
        newint = interval('(4, 10]')
        insertlist = [interval('[-1,20]')]
        self.assertEqual(insert(intlist, newint), insertlist)
        
if __name__ == '__main__':
    unittest.main()
            
        