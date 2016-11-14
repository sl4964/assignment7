import unittest
from interval.interval import *

class MyTest(unittest.TestCase):
    
    def test_interval(self):
        self.assertEqual(interval('(1,10)').intervallist, [2,9])
        self.assertEqual(interval('[7,20]').intervallist, [7,20])
        self.assertEqual(interval('(-1,4)').intervallist, [0,3])
        self.assertRaises(ValueError, interval, '(0,-10)') #Exception test
        
    def test_mergeIntervals(self):
        self.assertEqual(mergeIntervals(interval('[1,10]'), interval('[3,12)')).intervallist, [1,11])
        self.assertEqual(mergeIntervals(interval('[1,2]'),interval('(-1,5)')).intervallist, [0, 4])
        self.assertRaises(ValueError, mergeIntervals, interval('[1,2]'), interval('(10,20)')) #Exception test
        
    def test_mergeOverlapping(self):
        ints = [interval(i) for i in ['(1,10)','[2,13)', '[3,5]']]
        a = mergeOverlapping(ints)
        self.assertEqual(len(a),1)
        self.assertEqual(a[0].intervallist, [2,12])
        
    def test_mergeOverlapping2(self):
        ints = [interval(i) for i in ['(1,10)','[2,13)', '[3,5]', '[14,16]']]
        a = mergeOverlapping(ints)
        self.assertEqual(len(a),2)
        self.assertEqual(a[0].intervallist, [2,12])
        self.assertEqual(a[1].intervallist, [14,16])
        
    def test_mergeOverlapping3(self):
        ints = [interval(i) for i in ['(1,10)','[2,13)', '[3,5]', '[14,16]', '[13,14]']]
        a = mergeOverlapping(ints)
        self.assertEqual(len(a),1)
        self.assertEqual(a[0].intervallist, [2,16])
        
    def test_insert(self):
        ints = [interval(i) for i in ['(1,10)','[2,13)', '[3,5]', '[14,16]']]
        newint = interval('[13,14]')
        self.assertEqual(insert(ints,newint)[0].intervallist, [2,16])
        
    def test_insert2(self):
        ints = [interval(i) for i in ['(1,10)','[2,13)', '[3,5]', '[14,16]']]
        newint = interval('[17,18]')
        inserted = insert(ints, newint)
        self.assertEqual(len(inserted), 2)
        self.assertEqual(inserted[0].intervallist, [2,12])
        self.assertEqual(inserted[1].intervallist, [14,18])
        
if __name__ == '__main__':
    unittest.main()
    