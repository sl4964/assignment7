'''
Created on 2016.11.14

@author: xulei
'''

import unittest
from assignment7 import Interval
from Merge import *
from exceptionClass import *


class Test(unittest.TestCase):
    def setUp(self):
        #define several cases for testing intervals #four different types (other error type???)
        self.to_Intervals=['[-2,2]','(1,3)','[1,2)','(4,6]']
        self.Answer_Interval=['[-2,2]','(1,3)','[1,2)','(4,6]']       
        #for testing intervals
        self.to_merge=[[Interval('[-1,5]'),Interval('(5,10]')],[Interval('(2,4)'),Interval('[3,6)')],[Interval('[15,20)'),Interval('[18,25)')]]
        self.Answer_merge=['[-1,10]','(2,6)','[15,25)']       
        #for testing mergeOverlapping
        self.to_merge_list1=[Interval('[1,3]')]
        self.to_merge_list2=[Interval('[1,3]'),Interval('(7,19]'),Interval('[5,8]'),Interval('[20,190)')]
        self.to_merge_list3=[Interval('[1,2]'),Interval('[12,14]'),Interval('(9,10]')]
        self.to_merge_list=[self.to_merge_list1,self.to_merge_list2,self.to_merge_list3]
        self.Answer_merge_list=[['[1,3]'],['[1,3]','[5,190)'],['[1,2]','(9,10]','[12,14]']]        
        #for testing inserting new elemments
        self.insert_list1=[Interval('[1,3]'),Interval('(7,19]'),Interval('[45,77]')]
        self.insert_list2=[Interval('[1,3]'),Interval('(7,19]'),Interval('[45,77]')]
        self.insert_list3=[Interval('[1,3]'),Interval('(7,19]'),Interval('[45,77]')]
        self.insert_list4=[Interval('[1,3]'),Interval('(7,19]'),Interval('[45,77]')]
        self.insert_list5=[Interval('[1,3]'),Interval('(7,19]'),Interval('[45,77]')]
        self.int_list=[Interval('[24,30)'),Interval('(66,80]'),Interval('[35,56)'),Interval('[200,210]'),Interval('(17,99]')]
        self.Answer_insert_list=[['[1,3]','(7,19]','[24,30)','[45,77]'],['[1,3]','(7,19]','[45,80]'],['[1,3]','(7,19]','[35,77]'],['[1,3]','(7,19]','[45,77]','[200,210]'],['[1,3]','(7,99]']]

    
    def test_Interval(self):
        self.assertSequenceEqual([Interval(i).name for i in self.to_Intervals],self.Answer_Interval)
        
        with self.assertRaises(intervalException):
            Interval('[9,0]')
        with self.assertRaises(intervalException):
           Interval('[9,9)')
        with self.assertRaises(intervalException):
           Interval('(9,10]\\')
        with self.assertRaises(intervalException):
           Interval('(,khd')
        with self.assertRaises(intervalException):
           Interval('foo')
        with self.assertRaises(intervalException):
           Interval('(9,10]\\')
        with self.assertRaises(intervalException):
           Interval('(9,10)\\')
        

    def test_mergeIntervals(self):
        self.assertSequenceEqual([mergeIntervals(i[0], i[1]).name for i in self.to_merge],self.Answer_merge)
        
        with self.assertRaises(mergeException):
            mergeIntervals(Interval('[3,5]'),Interval('(6,9]'))
        with self.assertRaises(mergeException):
            mergeIntervals(Interval('(6,9]'),Interval('[3,5]'))
               
    def test_mergeOverlapping(self):
        for i in range(3):
            lists=[j.name for j in mergeOverlapping(self.to_merge_list[i])]
            self.assertEqual(lists,self.Answer_merge_list[i])

         
    def test_insert(self):
        self.assertSequenceEqual([j.name for j in insert(self.insert_list1,self.int_list[0])],self.Answer_insert_list[0])
        self.assertSequenceEqual([j.name for j in insert(self.insert_list2,self.int_list[1])],self.Answer_insert_list[1])
        self.assertSequenceEqual([j.name for j in insert(self.insert_list3,self.int_list[2])],self.Answer_insert_list[2])
        self.assertSequenceEqual([j.name for j in insert(self.insert_list4,self.int_list[3])],self.Answer_insert_list[3])
        self.assertSequenceEqual([j.name for j in insert(self.insert_list5,self.int_list[4])],self.Answer_insert_list[4])
        
'''  
  #data setup for test_mergeIntervals
              
        for Ints in self.merge_False:
            with self.assertRaises(MergeError):
                mergeIntervals(Ints[0], Ints[1])                   
    
        
 '''       

if __name__ =='__main__':
    unittest.main()