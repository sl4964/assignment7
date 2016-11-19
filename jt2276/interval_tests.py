'''
Tests for assignment7.py
@author: jonathanatoy
'''
import unittest
import assignment7
import interval
from interval_package.assignment7 import parseString_Interval, isMergeable,\
    mergeIntervals, mergeOverlapping

class Test(unittest.TestCase):


    def testIntervalClass(self):
        test_input = "[1,3)"
        param = parseString_Interval(test_input)
        myInt = interval(param[0], param[1], param[2], param[3])
        self.assertEqual(test_input, str(myInt))
    
    def testisMergeable1(self):
        test_input1 = "[1,3]"
        param = parseString_Interval(test_input1)
        myInt1 = interval(param[0], param[1], param[2], param[3])
        
        test_input2 = "[2,4]"
        param = parseString_Interval(test_input2)
        myInt2 = interval(param[0], param[1], param[2], param[3])
        
        self.assertEqual(True, isMergeable(myInt1, myInt2))
    
    def testisMergeable2(self):
        test_input1 = "[1,2]"
        param = parseString_Interval(test_input1)
        myInt1 = interval(param[0], param[1], param[2], param[3])
        
        test_input2 = "[3,4]"
        param = parseString_Interval(test_input2)
        myInt2 = interval(param[0], param[1], param[2], param[3])
        
        self.assertEqual(False, isMergeable(myInt1, myInt2))
    
    def testisMergeable3(self):
        #test if adjacency is flagged
        test_input1 = "[1,2)"
        param = parseString_Interval(test_input1)
        myInt1 = interval(param[0], param[1], param[2], param[3])
        
        test_input2 = "[2,4]"
        param = parseString_Interval(test_input2)
        myInt2 = interval(param[0], param[1], param[2], param[3])
        
        self.assertEqual(True, isMergeable(myInt1, myInt2))
        
    def testmergeintervals(self):
        test_input1 = "[1,3]"
        param = parseString_Interval(test_input1)
        myInt1 = interval(param[0], param[1], param[2], param[3])
        
        test_input2 = "[2,4]"
        param = parseString_Interval(test_input2)
        myInt2 = interval(param[0], param[1], param[2], param[3])
        
        answer = "[1,4]"
        self.assertEqual(answer, str(mergeIntervals(myInt1, myInt2)))
    
    def testmergeOverlapping(self):
        test_input1 = "[1,3]"
        param = parseString_Interval(test_input1)
        myInt1 = interval(param[0], param[1], param[2], param[3])
        
        test_input2 = "[2,4]"
        param = parseString_Interval(test_input2)
        myInt2 = interval(param[0], param[1], param[2], param[3])
        
        test_input3 = "[5,6]"
        param = parseString_Interval(test_input3)
        myInt3 = interval(param[0], param[1], param[2], param[3])
        
        intervals = [myInt1, myInt2, myInt3]
        answer = "[[1,4], [5,6]]"
        self.assertEqual(answer, str(mergeOverlapping(intervals)))
    
    def testinsert(self):
        
        test_input1 = "[1,3]"
        param = parseString_Interval(test_input1)
        myInt1 = interval(param[0], param[1], param[2], param[3])
        
        test_input2 = "[4,6]"
        param = parseString_Interval(test_input2)
        myInt2 = interval(param[0], param[1], param[2], param[3])
        
        test_input3 = "[7,8]"
        param = parseString_Interval(test_input3)
        myInt3 = interval(param[0], param[1], param[2], param[3])
        
        test_insert = "[2,5]"
        param = parseString_Interval(test_insert)
        newint = interval(param[0], param[1], param[2], param[3])
        
        intervals = [myInt1, myInt2, myInt3]
        new_intervals = insert(intervals, newint)
        answer = "[[1,6], [7,8]]"
        self.assertEqual(answer, str(new_intervals))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()