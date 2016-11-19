'''
Created on Nov 13, 2016

@author: twff
'''

from interval import *
import unittest

#$ python -m unittest discover
class IntervalTest(unittest.TestCase):

    def test_class(self):
        i = Interval(3, 4)  # success
        j = Interval(4, 4)  
            
    def test_eq(self):
        self.assertEqual(Interval(1, 5), Interval(1, 5))
        self.assertEqual(len(mergeOverlapping([])), 0)

    def test_stringRep(self):
        #correct input
        i = Interval.stringRep('[-5,-3]')
        self.assertEqual(i._lower, -5)
        self.assertEqual(i._upper, -3)
        self.assertEqual(Interval.stringRep('[-5,-3)')._upper, -4)
        i = Interval.stringRep('[1,010]')
        self.assertEqual(i._lower, 1)
        self.assertEqual(i._upper, 10)
        self.assertEqual(Interval.stringRep('(1,010]')._lower, 2 )
        i = Interval.stringRep('(010,100)')
        self.assertEqual(i._lower, 11)
        self.assertEqual(i._upper, 99)
        
        # Errors
        def assertValueError(s):
            with self.assertRaises(ValueError):
                Interval.stringRep(s)
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
        target = [Interval(-10, 4)]
        merged = mergeOverlapping(testset)
        for i, j in zip(target, merged):
            self.assertEqual(i, j)

    def test_insert(self):
        intervals = [Interval(1, 3), Interval(6, 9)]
        newint = Interval(2, 5)
        target = [Interval(1, 9)]
        inserted = insert(intervals, newint)
        self.assertEqual(target, inserted)
        
if __name__ == '__main__':
    unittest.main()