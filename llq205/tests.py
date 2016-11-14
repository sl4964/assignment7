import unittest
from assignment7 import *

# $ python -m unittest -v test.py

class Tests(unittest.TestCase):
    def testInterval(self):
        int1 = '(6,10)'
        self.assertEqual(str(int1), str(interval(int1)))
        int2 = '[-1,-1]'
        self.assertEqual(str(int2), str(interval(int2)))
        int3 = '(2,3]'
        self.assertEqual(str(int3), str(interval(int3)))
        
        with self.assertRaises(ValueError):
            int1 = interval('[a, b]')
        with self.assertRaises(ValueError):
            int2 = interval('10, 11')
        with self.assertRaises(ValueError):
            int3 = interval('[6, 2)')
            
    def testMergeable(self):
        int1 = interval('[7, 100]')
        int2 = interval('(5, 7]')
        self.assertEqual(mergeable(int1, int2), True)
        
        int1 = interval('[14, 16)')
        int2 = interval('[17, 19]')
        self.assertEqual(mergeable(int1, int2), False)
        
    def testMergeIntervals(self):
        int1 = interval('[4,8)')
        int2 = interval('[8,16)')
        ans = mergeIntervals(int1, int2)
        self.assertEqual('[4,16)', str(ans))
        
        int1 = interval('[5,10]')
        int2 = interval('[2,8]')
        ans = mergeIntervals(int1, int2)
        self.assertEqual('[2,10]', str(ans))
             
    def testMergeOverlapping(self):
        one = '[1,5]'
        two = '[6,8]'
        three = '(8, 10)'
        four = '[10, 11]'
        intervals = []
        intervals.append(interval(one))
        intervals.append(interval(two))
        intervals.append(interval(three))
        intervals.append(interval(four))
        self.assertEqual('[[1,11]]', str(mergeOverlapping(intervals)))
        
        one = '[-10,-7]'
        two = '(-4,1]'
        three = '[3,12)'
        four = '[15,23]'
        intervals = []
        intervals.append(interval(one))
        intervals.append(interval(two))
        intervals.append(interval(three))
        intervals.append(interval(four))
        self.assertEqual('[[-10,-7], (-4,1], [3,12), [15,23]]', str(mergeOverlapping(intervals)))
        
    def testInsert(self):
        intervals = []
        intervals.append(interval('[1,3]'))
        intervals.append(interval('[6,9]'))
        newint = interval('[2,5]')
        self.assertEqual(str(insert(intervals, newint)), '[[1,9]]')
        
        intervals = []
        intervals.append(interval('[1,10]'))
        intervals.append(interval('[10,11]'))
        newint = interval('(15,19)')
        self.assertEqual(str(insert(intervals, newint)), '[[1,11], (15,19)]')
        
if __name__ == "__main__":
    unittest.main()
