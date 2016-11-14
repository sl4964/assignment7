import unittest
import Utils as ut
import numpy as np

class myTestsforInterval(unittest.TestCase):
    
    def test_interval(self):
        self.assertEqual(ut.interval('(2,5)').lowLimit, 2)
        self.assertEqual(ut.interval('(2,5)').lowType, "(")
        self.assertEqual(ut.interval('(1,5)').highType, ")")
        self.assertRaises(ut.invalidArrayException, ut.interval, '(0,-1)')
        self.assertRaises(ut.invalidArrayException, ut.interval, 'foo')
        self.assertTrue(ut.interval('(1,5]').isHighInclusive)
        self.assertTrue(ut.interval('[1,5)').isLowInclusive)
        self.assertIsInstance(ut.interval('(3,8)').sequenceArray, np.ndarray)

        
class myTestsforMerge(unittest.TestCase):
    
    def test_mergeIntervals(self):
        self.assertEqual(ut.mergeIntervals(ut.interval('(2,5)'), ut.interval('[3,8)')).lowType, "[")
        self.assertEqual(ut.mergeIntervals(ut.interval('(2,5)'), ut.interval('[3,8)')).highType, ")")
        self.assertEqual(ut.mergeIntervals(ut.interval('(2,5)'), ut.interval('[3,8)')).lowLimit, 3)
        self.assertEqual(ut.mergeIntervals(ut.interval('(2,5)'), ut.interval('[3,8)')).highLimit, 5)
        self.assertEqual(ut.mergeIntervals(ut.interval('(2,5)'), ut.interval('[3,8)')).sequenceArray[0], 3)
        self.assertEqual(ut.mergeIntervals(ut.interval('(2,5)'), ut.interval('[3,8)')).sequenceArray[1], 4)
        self.assertEqual(ut.mergeIntervals(ut.interval('(2,5)'), ut.interval('[5,9)')).lowLimit, 5)
        self.assertEqual(ut.mergeIntervals(ut.interval('(2,5)'), ut.interval('[5,9)')).highLimit, 5)
        self.assertEqual(ut.mergeIntervals(ut.interval('(2,24)'), ut.interval('[24,26)')).highLimit, 24)
        
    def test_mergeIntervalsExceptions(self):
        self.assertRaises(ut.mergeIntervalsException, ut.mergeIntervals, ut.interval('(2,5)'), ut.interval('[7,9)'))
        self.assertRaises(ut.mergeIntervalsException, ut.mergeIntervals, ut.interval('[2,7)'), ut.interval('[10,12)'))

class myTestsforOverlapping(unittest.TestCase):
    
    def test_mergeOverlapping(self):
        int1 = ut.interval("[1,5]")
        int2 = ut.interval("[2,6)")
        int3 = ut.interval("(8,10]")
        int4 = ut.interval("[8,18]")
        intervalList = [int1, int2, int3, int4]
        self.assertEqual(len(ut.mergeOverlapping(intervalList)), 2)
        self.assertEqual(ut.mergeOverlapping(intervalList)[0].lowLimit, 1)
        self.assertEqual(ut.mergeOverlapping(intervalList)[0].highLimit, 6)
        self.assertEqual(ut.mergeOverlapping(intervalList)[1].lowLimit, 8)
        self.assertEqual(ut.mergeOverlapping(intervalList)[1].highLimit, 18)
        self.assertEqual(ut.mergeOverlapping(intervalList)[0].highType, ")")
        self.assertEqual(ut.mergeOverlapping(intervalList)[1].highType, "]")


class myTestsforInsert(unittest.TestCase):
    
    def test_insert1(self):   
        int1 = ut.interval("[1,3]")     
        int2 = ut.interval("[6,9]")
        int3 = ut.interval("[2,5]")
        intervalList = [int1, int2]
        self.assertEqual(ut.insert(intervalList, int3)[0].lowLimit, 1)
        self.assertEqual(ut.insert(intervalList, int3)[0].highLimit, 9)
        self.assertEqual(ut.insert(intervalList, int3)[0].lowType, "[")
        self.assertEqual(ut.insert(intervalList, int3)[0].highType, "]")
        self.assertIsInstance(ut.insert(intervalList, int3)[0].sequenceArray, np.ndarray)
        self.assertEqual(ut.insert(intervalList, int3)[0].sequenceArray[0], 1)
        self.assertEqual(ut.insert(intervalList, int3)[0].sequenceArray[len(ut.insert(intervalList, int3)[0].sequenceArray) - 1], 9)
        
    def test_insert2(self):
        int1 = ut.interval("[1,2]")     
        int2 = ut.interval("(3,5)")
        int3 = ut.interval("[6,7)")
        int4 = ut.interval("(8,10]")
        int5 = ut.interval("[12,16]")
        int6 = ut.interval("[4,9]") 
        intervalList = [int1, int2, int3, int4, int5]
        self.assertEqual(len(ut.insert(intervalList, int6)), 2) # See note below the code. 
        self.assertEqual(ut.insert(intervalList, int6)[0].lowLimit, 1)
        self.assertEqual(ut.insert(intervalList, int6)[1].lowLimit, 12)
        self.assertEqual(ut.insert(intervalList, int6)[1].highLimit, 16)
        self.assertEqual(ut.insert(intervalList, int6)[0].highLimit, 10)

""" A note: 
 The instructions for the homework were unclear and contradictory. 
 When ask to define the "insert()" functions, the instructions state that "[[1,2], (3,5), [6,7), (8,10], [12,16]" inserted with "[4,9]" should yield "[[1,2], (3,10], [12,16]]"
 But in the example below, when "[12,13)" is insterted into "[-10,-7], (-4,1], [3,12), [15,24]", it binds into "[-10,-7], (-4,1], [3,13), [15,24]"
 
 So, in one part of the instructions, it is said that we should treat (_,X) join [X,_) as separate, in other, as if we should join them. ([1,2] - (3,10] VS [3,12) - [12,13)
 
 This code joins those intervals into a single one. 
"""

        
if __name__ == '__main__':
    unittest.main()
    
