'''
Created on Nov 14, 2016
This module contains all the tests for class interval and the function mergeIntervals(), mergeOverlapping(), and insert().
Assignmnet7
DS-GA-1007
@author: Zahra kadkhodaie
All the tests run successfully 
'''
import unittest
from mergers import *
from interval import *

class Test(unittest.TestCase):
    '''Test interval Class'''
    def test_interval1(self):
        self.assertEqual(interval('[-2,9)').lower, -2 )
    
    def test_interval2(self):
        self.assertEqual(interval('[-2,9)').upper, 9 )
    
    def test_interval3(self):
        self.assertEqual(interval('[-2,9)').closing, ')' )
          
    def test_interval4(self):
        self.assertEqual(interval('[-2,9)').opening, '[' )
        
    def test_interval5(self):
        self.assertEqual(interval('[-2,9)').interval_instance, '[-2,9)' )
       
    def test_interval6(self):
        self.assertEqual(interval('[-2,9)').intervalNumbers(), [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8] )
    
    #Test an invalid interval
    def test_interval7(self):
        self.assertEqual(interval('[-2,-9)').intervalNumbers(), 'Invalid interval' )
    
    #Test an invalid interval
    def test_interval8(self):
        self.assertEqual(interval('(2,2)').intervalNumbers(), 'Invalid interval' )
       
    '''Test the mergeInterval Function'''
    #Test for when the two intervals have some overlap
    def test_mergeIntervals1(self):
        self.assertEqual(mergeIntervals('[1,30]', '(-9,21]'), '(-9,30]')

    #When one interval is the subset of the other one
    def test_mergeIntervals2(self):
        self.assertEqual(mergeIntervals('(2, 8)', '[1,10]'), '[1,10]')
    
    #When they are adjacent 
    def test_mergeIntervals3(self):
        self.assertEqual(mergeIntervals('(-3, 8)', '[8,11]'), '(-3,11]')
        
    #When there is no overlap
    def test_mergeIntervals4(self):
        self.assertEqual(mergeIntervals('(-10, -8]', '(2,9)'), 'Error: The two lists cannot be merged')
    
    #When the input is not meeting the requirement of an interval object
    def test_mergeIntervals5(self):
        self.assertEqual(mergeIntervals('(-10, -8]', '(2,1)'), 'Invalid interval')
    
    '''Test the mergeOverlapping function'''
    #Test for a bunch of intervals
    def test_mergeOverlapping1(self):
        self.assertEqual(mergeOverlapping([ '[-9,6]', '[7,9)', '(1,19]', '(20,100)']), ['[-9,19]', '(20,100)'])
    
    #For another group of intervals   
    def test_mergeOverlapping2(self):
        self.assertEqual(mergeOverlapping([ '[1,5]', '[-3,0]', '(9,10]']), ['[-3,5]', '(9,10]'])
    
    #For another group
    def test_mergeOverlapping3(self):
        self.assertEqual(mergeOverlapping([ '[-11,-7]', '[-3,100)', '(9,100]']), ['[-11,-7]', '[-3,100]'])
        
    '''Test the insert function'''
    def test_insert1(self):
        self.assertEqual(insert(['[-3,3]', '[6,9]'], '[2,19]'), ['[-3,19]'])
        
    def test_insert2(self):
        self.assertEqual(insert(['[-1,2]', '(-9,5)', '[6,7)', '(8,10]', '[12,16]'], '[4,9]'), ['(-9,10]', '[12,16]'])
      
    def test_insert3(self):
        self.assertEqual(insert(['[1,3]', '[6,9]'], '[2,5]'), ['[1,9]'])
      
    def test_insert4(self):
        self.assertEqual(insert(['[1,2]', '(3,5)', '[6,7)', '[8,10]', '[12,16]'], '[4,9]'), ['[1,2]', '(3,10]', '[12,16]'])
      
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(exit = False)