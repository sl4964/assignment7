from interval_functions import *
import unittest
'''This module is used for testing the four functions in interval_functions'''

class Interval_Functions_Test(unittest.TestCase):
    def test_interval1(self):
        int1='[10,25)'
        int2='[12,37)'
        int3='[41,59)'
        self.assertEqual(int1, str(interval(int1)))
        self.assertEqual(int2, str(interval(int2)))
        self.assertEqual(int3, str(interval(int3)))
    #test interval generating function by testing whether the string of interval is correct
    def test_interval2(self):
        with self.assertRaises(ValueError):
             interval('[1, a)')
        with self.assertRaises(ValueError):
             interval('[, a)')
        with self.assertRaises(ValueError):
             interval('[1,1 )')
    #test incorrect interval input
    print('interval function is good')

    

    def test_merge1(self):
        int1=interval('[10,25)')
        int2=interval('[12,37)')
        int3=interval('[24,59)')
        self.assertEqual('[10,37)', str(mergeInterval(int1,int2)))
        self.assertEqual('[12,59)', str(mergeInterval(int2,int3)))
        self.assertEqual('[10,59)', str(mergeInterval(int1,int3)))
    #test interval merging function by testing whether merging intervals is equal to calculated result
    def test_merge2(self):
        int1=interval('[10,25)')
        int2=interval('[12,37)')
        int3=interval('[41,59)')
        with self.assertRaises(MergeError):
             mergeInterval(int2,int3)
        with self.assertRaises(MergeError):
             mergeInterval(int1,int3)
    #test two unadjacent intervals
    print('merge function is good')
    
    def test_mergeOverlapping(self):
        int1=interval('[10,25)')
        int2=interval('[12,37)')
        int3=interval('[24,59)')
        int4=interval('[60,65]')
        merge_list1=[int1,int2,int3]
        merge_list2=[int1,int2,int4]
        self.assertEqual('[[10,59)]', str(mergeOverlapping(merge_list1)))
        self.assertEqual(str([interval('[10,37)'),interval('[60,65]')]), str(mergeOverlapping(merge_list2)))
    #test whether the result of merging a list of intervals is equal to the calculated results by hand.
    print('mergeOverlapping function is good')
    
    def test_insert(self):
        int1=interval('[1,3]') 
        int2=interval('[6,9]')
        int3=interval('[2,5]')
        int4=interval('[1,2]')
        int5=interval('(3,5)')
        int6=interval('[6,7)')
        int7=interval('(8,10]')
        int8=interval('[12,16]')
        int9=interval('[4,9]')
        intervals1=[int1,int2]
        intervals2=[int4,int5,int6,int7,int8]
        self.assertEqual(str(insert(intervals1,int3)),str([interval('[1,9]')]))
        self.assertEqual(str(insert(intervals2,int9)),str([interval('[1,2]'),interval('(3,10]'),interval('[12,16]')]))
    #test whether the result of inserting a new interval to a list of intervals is equal to the calculated results by hand.
    print('Insert function is good')      
        

if __name__ == '__main__':
    unittest.main()