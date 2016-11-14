import unittest
from interval import interval, IntervalError

class IntervalTest(unittest.TestCase):
    
    def test_initClosed(self):
        ## test lower bound
        int1 = interval("[2,6]")
        self.assertEqual(int1.lowerBound, 2) 
        ## test upper bound 
        self.assertEqual(int1.upperBound, 6)
        
    def test_initOpen(self):
        int1 = interval("(4,10)")
        ## test lower bound
        self.assertEqual(int1.lowerBound, 5)
        ## test upper bound
        self.assertEqual(int1.upperBound, 9)
        
    def test_mergeIntervals(self):
        ## testing intervals:
        int1 = interval('[2,6]')
        int2 = interval('[4,9]')
        int3 = interval('[7,12]')
        int4 = interval('[8,10]')
        mergedInt = interval('[2,9]')
        adjInt = interval('[2,12]')
        ## test overlap merge:
        self.assertEqual(interval.mergeIntervals(int1,int2), mergedInt)
        ## test adjacent merge:
        self.assertEqual(interval.mergeIntervals(int1,int3), adjInt)
        ## test interval that does not merge:
        with self.assertRaises(IntervalError):
            interval.mergeIntervals(int1,int4)
    
    def test_mergeOverlapping(self):
        ## testing examples:
        int1 = interval('[1,3]')
        int2 = interval('[2,4]')
        int3 = interval('[4,5]')
        int5 = interval('[7,10]')
        int6 = interval('[8,12]')
        int7 = interval('[11,13]')
        mergedInt123 = interval('[1,5]')
        mergedInt56 = interval('[7,12]')
        mergedInt57 = interval('[7,13]')
        mergedInts = [mergedInt123,mergedInt56]
        adjmergedInts = [mergedInt123,mergedInt57]
        nonmergedInts = [int1,int5]
        ## test merged lists:
        self.assertEqual(interval.mergeOverlapping([int1,int2,int3,int5,int6]), mergedInts)
        ## test adjacent merges:
        self.assertEqual(interval.mergeOverlapping([int1,int3,int5,int7]), adjmergedInts)
        ## test non-merge
        self.assertEqual(interval.mergeOverlapping([int1,int5]), nonmergedInts)
       
    def test_insert(self):
        int1 = interval('[1,3]')
        int2 = interval('[5,7]')
        int3 = interval('[9,14]')
        int4 = interval('[4,6]')
        mergedInt124 = interval('[1,7]')
        mergedInts = [mergedInt124]
        ## test basic insert:
        self.assertEqual(interval.insert([int1,int3],int2), [int1,int2,int3])
        ## test overlapping and adjacent merges:
        self.assertEqual(interval.insert([int1,int2],int4), mergedInts)

    
if __name__ == '__main__':
    unittest.main()