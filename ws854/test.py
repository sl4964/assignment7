'''
Created on Nov 13, 2016

@author: sunevan
'''
import unittest

from interval import * 



class MyTest(unittest.TestCase):


    def test_intervalclass(self):      
        self.assertEqual(str(interval("[2,4]")), "[2,4]")
        self.assertEqual(str(interval("(2,4]")), "(2,4]")
        self.assertEqual(str(interval("[2,4)")), "[2,4)")
        self.assertEqual(str(interval("(2,4)")), "(2,4)")
        with self.assertRaises(ValueError):
            interval("[10,5)")
        with self.assertRaises(ValueError):
            interval("{,5)")
        with self.assertRaises(ValueError):
            interval("[10,,5)")
        with self.assertRaises(ValueError):
            interval("[a,5)")
                                
        pass
    
    def test_mergeinterval(self):
        self.assertEqual(str(mergeIntervals("[2,4]", "(0,10)")),"(0,10)")
        self.assertEqual(str(mergeIntervals("(-1,7]", "[7,10]")),"(-1,10]")
        with self.assertRaises(ValueError):
            mergeIntervals("[2,4]", "(9,10)") # validate the gap will throw error 
            
    def test_mergeoverlapping(self):
        self.assertEqual(mergeOverlapping(["[1,5]","[2,6)","(8,10]","[8,18]"]), ['[1,5]', '[8,18]'])
        self.assertEqual(mergeOverlapping(["[1,5]","[2,7)","(8,10]","[8,18]"]), ['[1,7)', '[8,18]'])
            
        pass 
    
    def test_insert(self):
        self.assertEqual(insert(["[1,3]","[6,9]"],"[2,5]"),['[1,9]'])
        self.assertEqual(insert(["[1,2]", "(3,5)", "[6,7)", "(8,10]", "[12,16]"],"[4,9]"),['[1,2]', '[4,10]', '[12,16]'])
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()