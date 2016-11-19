'''
Created on Nov 14, 2016

@author: muriel820
'''
import unittest
from interval_assignment7.interval import *

class Interval_Test(unittest.TestCase):

    def test_Interval(self):
        validintervals = ['[1,2]', '(2,5)', '[2,4)','(5,7]','[-2,-1]', '[-4,-2)', '(-5,-2]', '(-6, -2)', '[1,  2]', '  [ 2,  3 ]   ']
        intervals=[]
        for item in validintervals:
             intervals.append(item)
        
        self.assertEqual(len(validintervals), len(intervals))  
        self.assertEqual(Interval('(9,10]'), Interval('[10,11)'))
        self.assertEqual(Interval('[01,3)'), Interval('(000000,002]'))
        with self.assertRaises(InputNotString):
            Interval(1)
        with self.assertRaises(InputNotString):
            Interval(1.872)
        with self.assertRaises(MissingBracket):
            Interval('1')
        with self.assertRaises(MissingBracket):
            Interval('<1,4>')
        with self.assertRaises(CommaError):
            Interval('(1,,2)')
        with self.assertRaises(CommaError):
            Interval('(1,,,)')
        with self.assertRaises(IntervalNoExistence):
            Interval('(1,2)')
        with self.assertRaises(IntervalNoExistence):
            Interval('[2,2)')
        with self.assertRaises(IntervalNoExistence):
            Interval('(1,-2)')    
    
    def test_mergeIntervals(self):
        a = Interval('(01,  4]')
        b = Interval('[5,7]')
        c = Interval('[2,  8)')
        d = Interval('(15,  24]')
        e = Interval('(7,  11]')
        f = Interval('(1,  11]')  
        self.assertEqual(mergeIntervals(a,b), c)  
        self.assertEqual(mergeIntervals(c,d), (c,d))
        self.assertEqual(mergeIntervals(c,e), f) 
    
    def test_mergeOverlapping(self):
        a = Interval('(01,  4]')
        b = Interval('[5,7]')
        c = Interval('(10,  12]')
        d = Interval('[2,  8)')
        e = Interval('(7,  11]')
        f = Interval('[2,  13)')
        list1 = [a,b,c]
        self.assertEqual(mergeOverlapping(list1),[d,c])
        list2 = [a,b,c,d,e]
        self.assertEqual(mergeOverlapping(list2),f)
    
    def test_insert(self):
        a = Interval('(01,  4]')
        b = Interval('[5,7]')
        c = Interval('(10,  12]')
        d = Interval('(15,  24]')
        e = Interval('(7,  11]')
        f = Interval('(23,  24]')
        list1 = [a,b,c,d]
        list2 = insert(list1, e)
        self.assertEqual(list2,[Interval('[2,13)'), Interval('(15,24]')])
        list3 = insert(list2, f)
        self.assertEqual(list2,list3)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()