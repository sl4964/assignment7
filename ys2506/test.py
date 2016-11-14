#unit tests
import unittest
import exceptions
from interval import *

class IntervalTest(unittest.TestCase):
    def test_class_interval(self):
        int1 = interval('(11,22)')
        self.assertEqual('(11,22)', str(int1))
        int2 = interval('[1,2)')
        self.assertEqual('[1,2)', str(int2))
        int3 = interval('(-1,2)')
        self.assertEqual('(-1,2)', str(int3))  
        # test case from Assignment7
        int7 = interval('[1,4]')
        self.assertEqual('[1,4]', str(int7))
        int8 = interval('(2,5]')
        self.assertEqual('(2,5]', str(int8))
        int9 = interval('[4,8)'  )
        self.assertEqual('[4,8)' , str(int9))
        int10 = interval('(3,9)')
        self.assertEqual('(3,9)' , str(int10))
        
        with self.assertRaises(InvalidException):
            int11 = interval('foo')
        with self.assertRaises(InvalidException):
            int12 = interval('[0, -1]')
        with self.assertRaises(InvalidException):
            int13 = interval('(2,3)')
        
    def test_mergeIntervals(self):
        int1 = interval('[1,4]')
        int2 = interval('(2,5]')
        int3 = mergeIntervals(int1, int2)
        self.assertEqual(str(int3),'[1,5]')
        
        int4 = interval('[3,12)')
        int5 = interval('[12,13]')
        int6 = mergeIntervals(int4, int5)
        self.assertEqual(str(int6),'[3,13]')
        
        int7 = interval('[1,4]')
        int8 = interval('(5,8]')
        
        with self.assertRaises(MergeException):
            int9 = mergeIntervals(int7, int8)
        

    def test_mergeOverlapping(self):
        intervals = []
        int1 = interval('[1,2]')
        intervals.append(int1)
        int2 = interval('(3,5]')
        intervals.append(int2)
        int13 = mergeOverlapping(intervals)
        self.assertEqual('[[1,2], (3,5]]', str(int13))
        int4 = interval('[1,13]')
        intervals.append(int4)
        int14 = mergeOverlapping(intervals)
        self.assertEqual('[[1,13]]', str(int14))
        
        int5 = interval('[12,13]')
        int6 = interval('[3,13]')
        int7 = interval('[1,4]')
        int8 = interval('(5,8]')
        '''
        int9 = mergeOverlapping([int1, int2])
        self.assertEqual('[[1,5]]', str(int9))
        int10 = mergeOverlapping([int1, int2, int3])
        self.assertEqual('[[1,5]]', str(int10))
        int11 = mergeOverlapping([int1, int2, int4, int9])
        self.assertEqual('[[1,12)]', str(int11))
        int12 = mergeOverlapping([int4, int5])
        self.assertEqual('[[3,13]]', str(int12))
        '''
        
        with self.assertRaises(InvalidException):
            int10 = interval('foo')
            int9 = mergeOverlapping([int7, int8, int10])
    
          
    def test_insert(self):
        intervals = []
        int1 = interval('[1,4]')
        intervals.append(int1)
        int2 = interval('(2,5]')
        intervals.append(int2)
        int3 = interval('[1,5]')
        int4 = interval('[3,12)')
        int5 = interval('[12,13]')
        int6 = interval('[3,13]')
        int7 = interval('[1,4]')
        
        
        int9 = insert(intervals, int3)
        self.assertEqual('[[1,5]]',str(int9))
        '''
        intervals.append(int9)
        int10 = insert(intervals, int9)
        self.assertEqual('[[1,5]]', str(int10))
        int11 = insert([int1, int2, int4, int9, int10])
        self.assertEqual('[[1,5]]', str(int11))
        '''
        with self.assertRaises(InvalidException):
            int8 = interval('(5,5)')
            int9 = mergeIntervals([int7, int8, int9])
        

if __name__ == '__main__':
    unittest.main()

