import unittest
from interval import *

class Test(unittest.TestCase):

    def setUp(self):
        pass 

    def test_interval_1(self):
        int1 = interval('[2,5]')
        self.assertEqual(int1.lower_bracket, '[')
        self.assertEqual(int1.lower, 2)
        self.assertEqual(int1.upper, 5)
        self.assertEqual(int1.upper_bracket, ']')

    def test_interval_2(self):
        int2 = interval('(-3,5)')
        self.assertEqual(int2.lower_bracket, '(')
        self.assertEqual(int2.lower, -3)
        self.assertEqual(int2.upper, 5)
        self.assertEqual(int2.upper_bracket, ')')

    def test_interval_3(self):
        with self.assertRaises(ValueError) as cm:
            interval('[3,2]')
        self.assertTrue('Input is not a valid interval' in str(cm.exception))
        #The function should raise an exception if the first number
        #is higher than the second number.

    def test_interval_4(self):
        with self.assertRaises(ValueError) as cm:
            interval('{5,8]')
        self.assertTrue('Input is not a valid interval' in str(cm.exception))
    
        #The function should raise an exception if the brackets do not adhere to
        #one of the following formats: '()', '[]', '[)', or '(]'

    def test_mergeIntervals_1(self):
        int1 = interval('[2,4]')
        int2 = interval('[5,6]')
        self.assertEqual(str(mergeIntervals(int1, int2)), '[2, 6]')

    def test_mergeIntervals_2(self):
        int1 = interval('[2,4]')
        int2 = interval('(5,6]')
        self.assertRaises(ValueError, mergeIntervals, int1, int2)
        # The function should raise an exception if the intervals are disjoint.

    def test_mergeIntervals_3(self):
        int1 = interval('(3,9)')
        int2 = interval('(0,12)')
        self.assertEqual(str(mergeIntervals(int1,int2)), str(int2))

    def test_mergeOverlapping_1(self):
        int1 = interval('[1,3]')
        int2 = interval('[6,9]')
        int3 = interval('[2,5]')
        intervals = [int1,int2,int3]
        self.assertEqual(str(mergeOverlapping(intervals)), '[[1, 9]]')
    
    def test_mergeOverlapping_2(self):
        int1 = interval('[1,2]')
        int2 = interval('[3,5)')
        int3 = interval('[10,12)')
        int4 = interval('[12,15]')
        intervals = [int1,int2,int3,int4]
        self.assertEqual(str(mergeOverlapping(intervals)), '[[1, 5), [10, 15]]')
                             
    def test_mergeOverlapping_3(self):
        int1 = interval('[1,2]')
        int2 = interval('[6,9)')
        int3 = interval('[10,12)')
        intervals = [int1,int2,int3]
        self.assertEqual(str(mergeOverlapping(intervals)), '[[1, 2], [6, 9), [10, 12)]')        

    def test_insert_1(self):
        int1 = interval('[1,2]')
        int2 = interval('[4,5)')
        int3 = interval('[10,12)')
        int4 = interval('[5,9]')
        intervals = [int1, int2, int3]
        self.assertEqual(str(insert(intervals,int4)), '[[1, 2], [4, 12)]')
        
    def test_insert_2(self):
        int1 = interval('(-1,3)')
        int2 = interval('[4,8]')
        int3 = interval('[9,9]')
        intervals = [int1,int2]
        self.assertEqual(str(insert(intervals,int3)), '[(-1, 3), [4, 9]]')

    def test_insert_3(self):
        int1 = interval('(-1,3)')
        int2 = interval('[6,8]')
        int3 = interval('(3,4]')
        intervals = [int1,int2]
        self.assertEqual(str(insert(intervals,int3)), '[(-1, 3), (3, 4], [6, 8]]')

if __name__ == '__main__':
    unittest.main()
    

