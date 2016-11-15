'''
Tests everything in interval module
'''
import unittest
from zl1271.interval import *

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
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()