'''
Created on Nov 13, 2016

@author: twff
'''
 '''
    Run the test in the project root directory from console by:
    $ python -m unittest discover
    '''
from Interval import *
import unittest

class IntervalTest(unittest.TestCase):

    def test_default_ctor(self):
        i = Interval(3, 4)  # success
        j = Interval(4, 4)  
        with self.assertRaises(ValueError):
            i = Interval(4, 3)
            
    def test_eq(self):
        self.assertEqual(Interval(1, 5), Interval(1, 5))
        self.assertEqual(len(mergeOverlapping([])), 0)

    def test_stringRep(self):
        #correct input
        i = Interval.stringRep('[1,010]')
        self.assertEqual(i._left, 1)
        self.assertEqual(i._right, 10)
        i = Interval.stringRep('[-5,-3]')
        self.assertEqual(i._left, -5)
        self.assertEqual(i._right, -3)
        self.assertEqual(Interval.stringRep('(1,010]')._left, 2)
        self.assertEqual(interval.stringRepg('[-5,-3)')._right, -2)
        
        # Errors
        def assertValueError(s):
            with self.assertRaises(ValueError):
                Interval.fromString(s)
        assertValueError('')
        assertValueError('(1,2)')
        assertValueError('[0]')
        assertValueError('[1,2,3]')
        assertValueError('3,4')
        assertValueError('[5,6')
        assertValueError('[5,,6')
        assertValueError('7,8)')
        assertValueError('[9,9)')
        assertValueError('(9,9]')
        assertValueError('[a,c]')
        assertValueError('   (  01 0  ,  101 0 ]')
        assertValueError('[,]')

    def test_mergeIntervals(self):
        l1 = Interval(1, 3)
        l2 = Interval(2, 4)
        l3 = Interval(1, 4)
        l4 = Interval(-1, 2)
        l5 = Interval(-10, -1)
        l6 = Interval(-10, 2)
        self.assertEqual(mergeIntervals(l1, l2), l3)
        self.assertEqual(mergeIntervals(l1, l3), l3)
        self.assertEqual(mergeIntervals(l4, l5), l6)
        with self.assertRaises(ValueError):
            mergeIntervals(l1, l5)

    def test_mergeOverlapping(self):
        testset = [Interval(1, 3), Interval(1, 4), Interval(-10, 0), Interval(-5, -1)]
        target = [Interval(1, 3), Interval(-10, 0)]
        merged = mergeOverlapping(raw)
        self.assertEqual(target, merged)

    def test_insert(self):
        intervals = [Interval(1, 3), Interval(6, 9)]
        newint = Interval(2, 5)
        target = [Interval(1, 9)]
        inserted = insert(intervals, newint)
        self.assertEqual(target, inserted)
if __name__ == '__main__':
    unittest.main()