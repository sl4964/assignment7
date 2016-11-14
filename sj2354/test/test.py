'''
Created on Nov 14, 2016

@author: sj238
'''
from interval import *
import unittest

class tests(unittest,TestCase):
    def testIntervalString(self):
        self.assertEqual('(3,8)', str(interval('(3, 8)')))
        self.assertEqual('(4,7]', str(interval('(4, 7]')))
        self.assertEqual('[-5,-2]', str(interval('[-5, -2]')))
        self.assertEqual('[7,9)', str(interval('[   7   ,   9   )')))
        self.assertEqual('[9,9]', str(interval('[9, 9]')))
        
    def test_mergeIntervals(self):
        a = interval('(5, 7)')
        b = interval('(4, 9)')
        c = interval('(-4, 1)')
        d = interval('(-4, 2)')
        e = interval('(3, 8)')
        self.assertEqual(mergeIntervals(a, b), c)
        self.assertEqual(mergeIntervals(a, c), c)
        self.assertEqual(mergeIntervals(d, a), d)
        with self.assertRaises(ValueError):
            mergeIntervals(a, e)
        
    def test_overlapping(self):
        a = ['[12,19)', '(50, 56)']
        b = ['(-10,-1)', '(0, 3)', '[2,4]']
        self.assertEqual(['[12,19)', '(50, 56)'], mergeOverlapping(a))
        self.assertEqual(['(3,4]'], mergeOverlapping(b))
    
    def test_insert(self):
        intervals = [
                interval(1, 3),
                interval(2, 4),
                interval(9, 11),
                ]
        newint = interval(4, 7)
        target = [interval(1, 11)]
        inserted = insert(intervals, newint)
        self.assertEqual(target, inserted)
        
            
        
    
