'''
Created on Nov 8, 2016

@author: apple
'''
import unittest
from interval import Interval,mergeOverlapping,insert,InputError,MergeError,mergeIntervals

class Test(unittest.TestCase):
    def setUp(self):
        #data setup for test_Interval
        self.Intervals_True=[' [2,2]','(1,3) ','[1, 2)','( 1,2]','[-2,-2]','(-3,-1)','[-2,-1)','(-2,-1]']
        self.Answer_Test_Interval=['[2,2]','(1,3)','[1,2)','(1,2]','[-2,-2]','(-3,-1)','[-2,-1)','(-2,-1]']
        self.Intervals_False=['[3,2]','[2,2)','(2,2]','(1,2)','[2,,7)','(2,2.2]','[]','[,]','foo']
        
        #data setup for test_mergeIntervals
        self.merge_True=[[Interval('[2,4]'),Interval('[3,10]')],[Interval('(2,4)'),Interval('[4,6)')]]
        self.Answer_merge=['[2,10]','[3,5]']
        self.merge_False=[[Interval('(2,4)'),Interval('(4,10)')],[Interval('[100,103)'),Interval('[10,12]')]]
        
        #data setup for test_mergeOverlapping
        self.test_Overlapping=[[Interval('(2,4)'),Interval('(4,10)'),Interval('[100,103)'),Interval('[10,12]')],[Interval('(93,400)'),Interval('(-4,10)'),Interval('[100,103)'),Interval('[10,12]')],[Interval('[1,10]')]]
        self.answer_Overlapping="[[(2,4), [5,12], [100,103)], [[-3,12], [94,399]], [[1,10]]]"    
        
        #data setup for test_insert
        self.insertList=[[Interval('(2,4)'),Interval('(4,10)'),Interval('[100,103)')],[Interval('(2,4)'),Interval('(4,10)'),Interval('[100,103)')],[Interval('[1,10]')],[Interval('[1,10]')],[]]
        self.insertInt=[Interval('[6,102)'),Interval('[-6,102)'),Interval('[-2,0)'),Interval('[100,200]'),Interval('[1,10]')]
        self.answer_insert='[[(2,4), [5,102]], [[-6,102]], [[-2,0), [1,10]], [[1,10], [100,200]], [[1,10]]]'    
    def test_Interval(self):
        self.assertSequenceEqual(list(map(lambda x: str(Interval(x)),self.Intervals_True)),self.Answer_Test_Interval)
        for stringInt in self.Intervals_False:
            with self.assertRaises(InputError):
                Interval(stringInt)
                     
    def test_mergeIntervals(self):
        self.assertSequenceEqual(list(map(lambda x: str(mergeIntervals(x[0], x[1])),self.merge_True)),self.Answer_merge)
        for Ints in self.merge_False:
            with self.assertRaises(MergeError):
                mergeIntervals(Ints[0], Ints[1])
                
    def test_mergeOverlapping(self):
        self.assertEqual(str(list(map(lambda x: mergeOverlapping(x),self.test_Overlapping))),self.answer_Overlapping)
        
    def test_insert(self):
        self.assertEqual(str(list(map(lambda x,y: insert(x,y),self.insertList,self.insertInt))),self.answer_insert)
        
        
if __name__ == "__main__":
    unittest.main()