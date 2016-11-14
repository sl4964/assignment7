import unittest

from question_1 import interval
from question_2 import mergeIntervals
from question_3 import mergeOverlapping
from question_4 import insert
#The test for question 1,2,3 and 4

class Question_1_Test(unittest.TestCase): 
    
    def test_question_1(self): 
        self.assertEqual(str(interval('[]')),"The interval is not valid"); 
        self.assertEqual(str(interval('[a,b]')),"The interval is not valid");   
        self.assertEqual(str(interval('[1,,5]')),"The interval is not valid");   
        self.assertEqual(str(interval('(11)')),"The interval is not valid");  
        self.assertEqual(str(interval('[1,1)')),"The interval is not valid"); 
        self.assertEqual(str(interval('[-2,5]')),"[-2,5] represents the numbers -2 to 5");  
        self.assertEqual(str(interval('[-2,5)')),"[-2,5) represents the numbers -2 to 4"); 
        self.assertEqual(str(interval('(-2,5)')),"(-2,5) represents the numbers -1 to 4"); 
        self.assertEqual(str(interval('(-2,5]')),"(-2,5] represents the numbers -1 to 5");    
    
    
class Question_2_Test(unittest.TestCase): 
    
    def test_question_2(self): 
        self.assertEqual(mergeIntervals('[-1,3]', '(10,15)'),"No overlap for the intervals");
        self.assertEqual(mergeIntervals('[-1,3]', '(4,15)'),"No overlap for the intervals"); 
        self.assertEqual(str(mergeIntervals('[-1,3]', '(3,15)')),"[-1, 14]");
        self.assertEqual(str(mergeIntervals('[-1,3)', '(-2,15]')),"[-1, 15]");
        self.assertEqual(str(mergeIntervals('(-1,3]', '[0,15]')),"[0, 15]");
        self.assertEqual(str(mergeIntervals('(-1,3)', '[3,15)')),"[0, 14]");
    
    #If the input interval is not valid, error will raise. Here we do not justify the incorrect input, and it will be handled together in question 5  
    def test_question_2_Error(self):
        with self.assertRaises(ValueError):
            value=mergeIntervals('()', '[0,15]')   
        with self.assertRaises(ValueError):
            value=mergeIntervals('(1,-1)', '[a,b]')


class Question_3_Test(unittest.TestCase): 
    
    def test_question_3(self): 
        self.assertEqual(str(mergeOverlapping(['[-1,3]', '(10,15)'])),"[[-1, 3], [11, 14]]");
        self.assertEqual(str(mergeOverlapping(['[-1,3)', '(4,15]'])),"[[-1, 2], [5, 15]]");
        self.assertEqual(str(mergeOverlapping(['[-1,3)', '(4,15]', '[2,5]'])),"[[-1, 15]]");
        self.assertEqual(str(mergeOverlapping(['(-10,3)', '[4,15]', '(-16,-10]'])),"[[-15, 2], [4, 15]]");
        self.assertEqual(str(mergeOverlapping(['(-10,3)', '[4,15]', '(-16,-10]','[-20,-8)'])),"[[-20, 2], [4, 15]]");
        
    #If the input interval is not valid, error will raise. Here we do not justify the incorrect input, and it will be handled together in question 5  
    def test_question_3_Error(self):
        with self.assertRaises(ValueError):
            value=mergeOverlapping(['()', '[0,15]'])   
        with self.assertRaises(ValueError):
            value=mergeOverlapping(['(1,-1)', '[a,b]','(c,2]'])


class Question_4_Test(unittest.TestCase):
    
    def test_question_4(self): 
        self.assertEqual(str(insert(['[-1,3]', '(10,15)'],'[5,10]')),"[[-1, 3], [5, 14]]");
        self.assertEqual(str(insert(['[-1,3]', '(10,15)'],'[20,30)')),"[[-1, 3], [11, 14], [20, 29]]"); 
        self.assertEqual(str(insert(['(-1,3]', '(10,15)', '[16,20]', '[22,31)'],'(2,15]')),"[[0, 20], [22, 30]]"); 
        self.assertEqual(str(insert(['(-1,3]', '(10,15)', '[16,20]', '[22,31)'],'[-2,23)')),"[[-2, 30]]");
        self.assertEqual(str(insert(['(-1,3]', '(10,15)', '[16,20]', '[-15,-1)'],'[-2,9)')),"[[-15, 8], [11, 14], [16, 20]]");
    
    #If the input interval is not valid, error will raise. Here we do not justify the incorrect input, and it will be handled together in question 5  
    def test_question_4_Error(self):
        with self.assertRaises(ValueError):
            value=insert(['()', '[s,n]'], '(1,2)')   
        with self.assertRaises(ValueError):
            value=insert(['()', '[3,4]'], '(1,6)')   
              
   
if __name__ == '__main__':     
    unittest.main() 