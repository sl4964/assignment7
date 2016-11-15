'''
Created on Nov 14, 2016

@author: muriel820
'''
import unittest
from interval_assignment7 import interval

class Interval_Test(unittest.TestCase):


    def testInterval(self):
        validintervals = ['[1,2]', '(2,5)', '[2,4)','(5,7]','[-2,-1]', '[-4,-2)', '(-5,-2]', '(-6, -2)', '[1,  2]', '  [ 2,  3 ]   ']
        intervals=[]
        for item in validintervals:
             intervals.append(item)
        
        self.assertEqual(len(validintervals), len(intervals))  
        
        for item in intervals:
            item.__repr__()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()