import unittest
from interval import interval, insert,  mergeIntervals, mergeOverlapping


class Test(unittest.TestCase):
    
    def setup(self):
        pass
    
    #test for class interval 
    def test_init(self):
        self.assertEqual(interval("[1,4]").lower, 1)
        self.assertEqual(interval("[1,4]").upper, 4)
        self.assertTrue(interval("[1,4]").lower <= interval("[1,4]").upper)
        
        self.assertEqual(interval("(2,5]").lower, 2)
        self.assertEqual(interval("(2,5]").upper, 5)
        self.assertTrue(interval("(2,5]").lower < interval("(2,5]").upper)
        
        self.assertEqual(interval("[4,8)").lower, 4)
        self.assertEqual(interval("[4,8)").upper, 8)
        self.assertTrue(interval("[4,8)").lower < interval("[4,8)").upper)
        
        self.assertEqual(interval("(3,9)").lower, 3)
        self.assertEqual(interval("(3,9)").upper, 9)
        self.assertTrue(interval("(3,9)").lower < interval("(3,9)").upper-1)
                              
        with self.assertRaises(ValueError):
            interval("(3,4)")
        with self.assertRaises(ValueError):
            interval("(3,3]") 
        with self.assertRaises(ValueError):
            interval("[4,3]") 
    
    
    ##test for mergeIntervals method 
    def test_mergeIntervals(self):
        with self.assertRaises(ValueError):
            mergeIntervals(interval("[4,8)"),interval("[10,12]"))
        with self.assertRaises(ValueError):
            mergeIntervals(interval("[2,6)"),interval("(8,10]"))
        with self.assertRaises(ValueError):
            mergeIntervals(interval("[1,4)"),interval("(4,10]"))
        
        self.assertEqual(str(mergeIntervals(interval("[1,5]"),interval("[2,6)"))), "[1,6)")
        self.assertEqual(str(mergeIntervals(interval("(8,10]"),interval("[8,18]"))), "[8,18]")
        self.assertEqual(str(mergeIntervals(interval("[3,12)"),interval("[12,13]"))), "[3,13]")
        self.assertEqual(str(mergeIntervals(interval("[3,6)"),interval("(5,15]"))), "[3,15]") 
    
    
    #test for mergeOverlapping method 
    def test_mergeOverlapping(self):
        lst =  ["[1,5]","[2,6)" , "(8,10]" , "[8,18]"]
        interval_list =  [interval(i) for i in lst]
        str_re = [str(i) for i in mergeOverlapping(interval_list)] 
        join_str = ', '.join(str_re)
        self.assertEqual(join_str, "[1,6), [8,18]")  
    
    def test_mergeOverlapping_2(self):
        lst =  ["[1,3]","[2,6)" , "[5,7]" , "[10,12]"]
        interval_list =  [interval(i) for i in lst]
        str_re = [str(i) for i in mergeOverlapping(interval_list)] 
        join_str = ', '.join(str_re)
        self.assertEqual(join_str, "[1,7], [10,12]")
    
    def test_mergeOverlapping_3(self):
        lst =  ["[1,4]","(3,5)" , "[6,7)" , "(8,10]", "[12,16]"]
        interval_list =  [interval(i) for i in lst]
        str_re = [str(i) for i in mergeOverlapping(interval_list)] 
        join_str = ', '.join(str_re)
        self.assertEqual(join_str, "[1,5), [6,7), (8,10], [12,16]")

     
    #test for insert method 
    def test_insert(self): 
        lst = ["[1,3]", "[6,9]"]
        interval_list =  [interval(i) for i in lst]
        str_re = [str(i) for i in insert(interval_list, interval("[2,5]")) ]
        join_str = ', '.join(str_re)
        self.assertEqual(join_str, "[1,9]")
    
    def test_insert_2(self):
        lst = ["[1,2]", "(3,5)", "[6,7)", "(8,10]", "[12,16]"]
        interval_list =  [interval(i) for i in lst]
        str_re = [str(i) for i in insert(interval_list, interval("[4,9]")) ]
        join_str = ', '.join(str_re)
        self.assertEqual(join_str, "[1,2], (3,10], [12,16]") 



if __name__ == "__main__":
    unittest.main()