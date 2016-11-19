import unittest
from Interval import Interval, IsMergeable, mergeIntervals, mergeOverlapping, insert, MergeError


class Test(unittest.TestCase):
    def setUp(self):
        #basic input
        self.Intervals_True=['(1,3) ','[1, 3)','[1,3]','[2,   3]','[-8,3)']
        self.Answer_Test_Interval=['(1,3)','[1,3)','[1,3]','[2,3]','[-8,3)']
        self.Intervals_False=['[]','[,]','foo']

        #merge
        self.merge_True=[[Interval('[1,5]'),Interval('[3,6]')],[Interval('(1,4)'),Interval('[4,6)')]]
        self.Answer_merge=['[1,6]','(1,6)']
        self.merge_False=[[Interval('(1,7)'),Interval('[2,8]')]]

        #overlapping
        self.test_Overlapping=[[Interval('(1,3)'),Interval('[3,5)'),Interval('[5,10)'),Interval('[10,12]')],[Interval('(10,20)'),Interval('(-5,-3)'),Interval('[4,9)'),Interval('[9,12]')],[Interval('[1,10]')]]
        self.answer_Overlapping="[ [5,12], [[1,20], (-5,-3)]]"    

        #insert
        self.insertList=[[Interval('(2,3]'),Interval('[3,10)'),Interval('[20,40)')],[Interval('(5,9)'),Interval('[4,10)'),Interval('[50,60)')]]
        self.insertInt=[Interval('[6,30)'),Interval('[7,20)')]
        self.answer_insert='[(2,40),[[4,20),[50,60) ]'    

 

if __name__ == "__main__":
    unittest.main() 
