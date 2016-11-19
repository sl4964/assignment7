"""Unittest for class interval and merge functions""" 

#Question 6 of HW7
import unittest
from class_interval import interval
from merge_func import mergeIntervals, mergeOverlapping, insert

class Test(unittest.TestCase):

    ######   Test for class interval()
    #Test whether the outputs are the same as our expected  
    def test_equal_class_interval(self):
        self.assertEqual(str(interval('a')), "Invalid interval")
        self.assertEqual(str(interval('!*')),"Invalid interval")
        self.assertEqual(str(interval('(1,')),"Invalid interval")
        self.assertEqual(str(interval('(1,2)')),"Invalid interval")
        self.assertEqual(str(interval('(1,3)')),"(1,3) represents the numbers 2 through 2")
        self.assertEqual(str(interval('[1,3)')),"[1,3) represents the numbers 1 through 2")
        self.assertEqual(str(interval('(1,3]')),"(1,3] represents the numbers 2 through 3")
        self.assertEqual(str(interval('[1,3]')),"[1,3] represents the numbers 1 through 3")
    
    
    
    
    ######   Test for function mergeIntervals()
    #Test whether the outputs are the same as our expected    
    def test_equal_mergeIntervals(self):
        self.assertEqual(mergeIntervals('(-1,10)', '(-11,100]'), "(-11,100]")
        self.assertEqual(mergeIntervals('(-1,10)', '[20,100)'), "No overlap between two intervals")
    
    #Test raise error
    #Since checking whether input is correct is relied on class interval,
    #I did not handle the input error in this function, so we can expect some errors due to incorrect input
    #Most Errors will be solved in Question 5 when we make the functions and the class intervals() together 
    def test_ValueError_mergeIntervals(self):
        with self.assertRaises(ValueError):
            value = mergeIntervals('()', '[20,100)')
    
    def test_TypeError_mergeIntervals(self):
        with self.assertRaises(TypeError):
            value = mergeIntervals(1, '[20,100)') #If input is not a string, may have TypeError
                                                  #However, due to bound symbols, we should expect to input interval in a string representation
            
    
    
    
    ######   Test for function mergeOverlapping()
    #Test whether the outputs are the same as our expected
    def test_equal_mergeOverlapping(self):
        self.assertEqual(mergeOverlapping(['(1,14)','(11,12]']), [[2, 13]])
        self.assertEqual(mergeOverlapping(['(1,10)','(11,13]']), [[2, 9], [12, 13]])
        self.assertEqual(mergeOverlapping(['(-2,1)','[3,6]','(7,8]','[9,19)']), [[-1, 0], [3, 6], [8, 18]])
    
    #Test raise error
    #Again, not handle the input error in this function, so we can expect ValueError due to incorrect input
    def test_ValueError_mergeOverlapping(self):
        with self.assertRaises(ValueError):
            value = mergeOverlapping(['(a,1)','[3,6]','(9,11)'])
    
    
    
    
    ######   Test for function insert()
    #Test whether the outputs are the same as our expected
    def test_equal_insert(self):
        self.assertEqual(insert(['(1,14)','(11,12]'],'(14,19)'), [[2, 13], [15, 18]])
        self.assertEqual(insert(['(1,10)','(11,13]'], '[9,12]'), [[2, 13]])
        self.assertEqual(insert(['[1,2]', '(3,5)', '[6,7)', '(8,10]','[12,16]'], '[4,9]'), [[1, 2], [4, 10], [12, 16]])
    
    #Test raise error
    #Again, not handle the input error in this function, so we can expect ValueError due to incorrect input
    def test_ValueError_insert(self):
        with self.assertRaises(ValueError):
            value = insert(['(a,1)','[3,6]'],'(7,10)')

       
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()