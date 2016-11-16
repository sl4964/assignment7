# Unit tests for the class interval and the functions mergeIntervals(), mergeOverlapping(), and insert()
import unittest

from assignment7 import *


class Test(unittest.TestCase):
    def testInterval(self):
        self.assertEqual('(2,6]', str(interval('(2,6]')))
        self.assertEqual('[-5,3]', str(interval('[-5,3]')))
        self.assertEqual('(9,22)', str(interval('(9,22)')))
        
    def testMergeInterval(self):
        test_int1 = "[1,10)"
        test_int2 = "(3,21]"
        self.assertEqual(str(mergeIntervals(test_int1,test_int2)), "[1,21]")

    def testMergeOverlapping(self):
        test_int1 = interval("(2,5)")
        test_int2 = interval("[5,8)")
        test_int3 = interval("(-2,3]")
        test_int4 = mergeOverlapping([test_int1,test_int2,test_int3])
        self.assertEqual(str(test_int4), "[(-2,3], [5,8)]")

    def testInsert(self):
        test_int1 = interval("(2,6)")
        test_int2 = interval("[5,9)")
        test_int3 = interval("(7,23]")
        newInt = insert([test_int1,test_int2], test_int3)
        self.assertEqual(str(newInt), "[(2,6), (7,23]]")
    
        
if __name__ =="__main__":
    unittest.main() 
