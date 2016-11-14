'''
Created on Nov 11, 2016

@author: Fanglin Chen
'''
import unittest
from interval import *
from merge import *

class TestInterval(unittest.TestCase):  
    '''
    The TestInterval class provides unit tests for the class interval.
    '''
    def testintervals(self):
        
        self.assertEqual(interval('[1, 4]').lower, 1)
        self.assertEqual(interval('[1, 4]').upper, 4)
        self.assertEqual(interval('[1, 4]').lower_integer, 1)
        self.assertEqual(interval('[1, 4]').upper_integer, 4)
        self.assertEqual(interval('[1, 4]').lower_inclusive, True)
        self.assertEqual(interval('[1, 4]').upper_inclusive, True)
        
        self.assertEqual(interval('(2, 5]').lower, 2)
        self.assertEqual(interval('(2, 5]').upper, 5)
        self.assertEqual(interval('(2, 5]').lower_integer, 3)
        self.assertEqual(interval('(2, 5]').upper_integer, 5)
        self.assertEqual(interval('(2, 5]').lower_inclusive, False)
        self.assertEqual(interval('(2, 5]').upper_inclusive, True)
        
        self.assertEqual(interval('[4, 8)').lower, 4)
        self.assertEqual(interval('[4, 8)').upper, 8)
        self.assertEqual(interval('[4, 8)').lower_integer, 4)
        self.assertEqual(interval('[4, 8)').upper_integer, 7)
        self.assertEqual(interval('[4, 8)').lower_inclusive, True)
        self.assertEqual(interval('[4, 8)').upper_inclusive, False)
        
        self.assertEqual(interval('(3, 9)').lower, 3)
        self.assertEqual(interval('(3, 9)').upper, 9)
        self.assertEqual(interval('(3, 9)').lower_integer, 4)
        self.assertEqual(interval('(3, 9)').upper_integer, 8)
        self.assertEqual(interval('(3, 9)').lower_inclusive, False)
        self.assertEqual(interval('(3, 9)').upper_inclusive, False)


class TestMerge(unittest.TestCase): 
    '''
    The TestInterval class provides unit tests for the functions mergeIntervals(), mergeOverlapping(), and insert().
    '''
    def testmergeIntervals(self):
        self.assertEqual(mergeIntervals(interval('[1, 4]'), interval('(2, 5]')), interval('[1, 5]'))
        self.assertEqual(mergeIntervals(interval('[2, 5]'), interval('[6, 9]')), interval('[2, 9]'))
        self.assertEqual(mergeIntervals(interval('(8, 10]'), interval('[8, 18]')), interval('[8, 18]'))
        self.assertEqual(mergeIntervals(interval('(1, 12]'), interval('(-4, 3)')), interval('(-4, 12]'))
        with self.assertRaises(Exception) as context:  # Reference: http://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
            mergeIntervals(interval('(3, 5)'), interval('[6, 9]'))
        self.assertTrue('The intervals cannot be merged' in str(context.exception))
        with self.assertRaises(Exception) as context:
            mergeIntervals(interval('(8, 10]'), interval('[6, 7)'))
        self.assertTrue('The intervals cannot be merged' in str(context.exception))
                          
    def testmergeOverlapping(self):
        self.assertEqual(mergeOverlapping([interval('[1, 5]'), interval('[2, 6)'), interval('(8, 10]'), interval('[8, 18]')]), [interval('[1, 6)'), interval('[8, 18]')]) 
        self.assertEqual(mergeOverlapping([interval('[-10, -7]'), interval('[15, 23]'), interval('(8, 12)'), interval('(-4, 1]'), interval('[3, 6)')]), [interval('[-10, -7]'), interval('(-4, 1]'), interval('[3, 6)'), interval('(8, 12)'), interval('[15, 23]')])
        self.assertEqual(mergeOverlapping([interval('(8, 12)'), interval('[3, 6)'), interval('[4, 8]')]), [interval('[3, 12)')]) 
        
    def testinsert(self):
        self.assertEqual(insert([interval('[1, 3]'), interval('[6, 9]')], interval('[2, 5]')), [interval('[1, 9]')])
        self.assertEqual(insert([interval('[1, 2]'), interval('(3, 5)'), interval('[6, 7)'), interval('(8, 10]'), interval('[12, 16]')], interval('[4, 9]')), [interval('[1, 2]'), interval('(3, 10]'), interval('[12, 16]')])
        self.assertEqual(insert([interval('[-10, -7]'), interval('[15, 23]'), interval('[3, 12)')], interval('[24, 24]')), [interval('[-10, -7]'), interval('[3, 12)'), interval('[15, 24]')])
        self.assertEqual(insert([interval('(-4, 1]'), interval('[3, 12)')], interval('[12, 13)')), [interval('(-4, 1]'), interval('[3, 13)')])
        self.assertEqual(insert([interval('[3, 13)')], interval('(2, 12)')), [interval('(2, 13)')])

if __name__ == "__main__":
    unittest.main()
    
