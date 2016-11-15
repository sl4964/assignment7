'''
Tests everything in interval module
'''
import unittest
from interval import *

class Test(unittest.TestCase):


    def test_is_interval_format(self):
        corr_str_list = ['(1,-100)','(-9,-10]','[5,6]','[9,9)']        
        for this_str in corr_str_list:
            self.assertEqual(is_interval_format(this_str), True)
            
        wrong_str_list = ['dfksdaf','(9,fgk)','(9,0.8)']
        for this_str in wrong_str_list:
            self.assertEqual(is_interval_format(this_str), False)
            
    def test_is_interval_content(self):
        corr_str_list = ['[-10,-7]','(-4,1]','[3,6)','(8,12)','[100,100]']
        for this_str in corr_str_list:
            self.assertEqual(is_interval_content(this_str), True)       
        
        wrong_str_list = ['(1,-100)','(-9,-10]','[5,4]','[9,9)']
        for this_str in wrong_str_list:
            self.assertEqual(is_interval_content(this_str), False)
    
    def test_is_interval(self):
        corr_str_list = ['[-10,-7]','(-4,1]','[3,6)','(8,12)','[100,100]']
        for this_str in corr_str_list:
            self.assertEqual(is_interval(this_str), True) 
            
        wrong_str_list = ['(1,-100)','(-9,-10]','[5,4]','[9,9)','asfsdafa','(9,fgk)','(9,0.8)']
        for this_str in wrong_str_list:
            self.assertEqual(is_interval(this_str), False)
    
    def test_mergeIntervals(self):
        int1 = interval('[-10,-7]')
        int2 = interval('(-9,11]')
        self.assertEqual(mergeIntervals(int1, int2).str, interval('[-10,11]').str)
        
    def test_sort_intervals(self):
        list_of_intervals = [interval('[-1,3]'),interval('(3,5]'),interval('(-10,-3]'),interval('[100,105]'),interval('(0,1]')]
        list_of_correct_ordered_intervals_by_lowest_value = [interval('(-10,-3]'),interval('[-1,3]'),interval('(0,1]'),interval('(3,5]'),interval('[100,105]')]
        sorted_list = sort_intervals(list_of_intervals)
        for ii in range(0,len(list_of_intervals)):
            self.assertEqual(sorted_list[ii].str,list_of_correct_ordered_intervals_by_lowest_value[ii].str)
            self.assertEqual(sorted_list[ii].lower_value,list_of_correct_ordered_intervals_by_lowest_value[ii].lower_value)
            self.assertEqual(sorted_list[ii].higher_value,list_of_correct_ordered_intervals_by_lowest_value[ii].higher_value)
            self.assertEqual(sorted_list[ii].lower_brac,list_of_correct_ordered_intervals_by_lowest_value[ii].lower_brac)
            self.assertEqual(sorted_list[ii].higher_brac,list_of_correct_ordered_intervals_by_lowest_value[ii].higher_brac)
            self.assertEqual(sorted_list[ii].lowest_value,list_of_correct_ordered_intervals_by_lowest_value[ii].lowest_value)
            self.assertEqual(sorted_list[ii].highest_value,list_of_correct_ordered_intervals_by_lowest_value[ii].highest_value)
    
    def test_can_merge(self):
        int1 = interval('[-10,-7]')
        int2 = interval('(-9,11]')
        int3 = interval('(42,211]')
        self.assertEqual(can_merge(int1, int2), True)
        self.assertEqual(can_merge(int2, int3), False)
        
    def test_get_can_merge_list(self):
        list_of_intervals = [interval('(-10,-3]'),interval('[-1,3]'),interval('(0,1]'),interval('(4,5]'),interval('[100,105]')]
        correct_answer = [0, 1, 0, 0]
        self.assertEqual(get_can_merge_list(list_of_intervals),correct_answer)
    
    def test_mergeOverlapping(self):
        list_of_intervals = [interval('[-1,3]'),interval('(3,5]'),interval('(-10,-3]'),interval('[100,105]'),interval('(0,1]')]
        merged_list = mergeOverlapping(list_of_intervals)
        correct_ans_list = [interval('(-10,-3]'),interval('[-1,5]'),interval('[100,105]')]
        for ii in range(0,len(merged_list)):
            self.assertEqual(merged_list[ii].str,correct_ans_list[ii].str)
            self.assertEqual(merged_list[ii].lower_value,correct_ans_list[ii].lower_value)
            self.assertEqual(merged_list[ii].higher_value,correct_ans_list[ii].higher_value)
            self.assertEqual(merged_list[ii].lower_brac,correct_ans_list[ii].lower_brac)
            self.assertEqual(merged_list[ii].higher_brac,correct_ans_list[ii].higher_brac)
            self.assertEqual(merged_list[ii].lowest_value,correct_ans_list[ii].lowest_value)
            self.assertEqual(merged_list[ii].highest_value,correct_ans_list[ii].highest_value)
    
    def test_insert(self):
        list_of_intervals = [interval('(-10,-3]'),interval('[-1,3)')]
        int1 = interval('[-3,2]')
        inserted_list = insert(list_of_intervals,int1)
        corr_list = [interval('(-10,3)')]
        for ii in range(0,len(inserted_list)):
            self.assertEqual(inserted_list[ii].str,corr_list[ii].str)
            self.assertEqual(inserted_list[ii].lower_value,corr_list[ii].lower_value)
            self.assertEqual(inserted_list[ii].higher_value,corr_list[ii].higher_value)
            self.assertEqual(inserted_list[ii].lower_brac,corr_list[ii].lower_brac)
            self.assertEqual(inserted_list[ii].higher_brac,corr_list[ii].higher_brac)
            self.assertEqual(inserted_list[ii].lowest_value,corr_list[ii].lowest_value)
            self.assertEqual(inserted_list[ii].highest_value,corr_list[ii].highest_value) 
               
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()