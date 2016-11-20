import unittest
from sy1253.interval import interval, insert, mergeIntervals, mergeOverlapping


class Test(unittest.TestCase):
    
 

    
    def setup(self):
        pass
    
    def test_interval(self):
        self.assertEqual(interval("[3,8]").lowerBegin, 3)
        self.assertEqual(interval("[3,8]").upperEnd, 8)
        
        self.assertEqual(interval("(3,8]").lowerBegin, 4)
        self.assertEqual(interval("(3,8]").upperEnd, 8)
               
        self.assertEqual(interval("[3,8)").lowerBegin, 3)
        self.assertEqual(interval("[3,8)").upperEnd, 7)
        
        self.assertEqual(interval("(3,8)").lowerBegin, 4)
        self.assertEqual(interval("(3,8)").upperEnd, 7)
       
                              
                              
    def test_mergeIntervals(self):
              
        self.assertEqual(str(mergeIntervals(interval("(1,7]"), interval("[2,9]"))), "(1,9]")
        self.assertEqual(str(mergeIntervals(interval("[8,9)"), interval("[1,15]"))), "[1,15]")
        self.assertEqual(str(mergeIntervals(interval("[3,8)"), interval("(6,23)"))), "[3,23)")
        self.assertEqual(str(mergeIntervals(interval("(1,19)"), interval("[2,6]"))), "(1,19)")
        
     
     
        
    def test_mergeOverlapping(self):
        self.assertEqual(str(mergeOverlapping([interval("[2,5]"),interval("(1,4)"),interval("(3,10]"),interval("[12,20)")])), "[(1,10], [12,20)]")
        self.assertEqual(str(mergeOverlapping([interval("(1,3)"),interval("(4,5]"),interval("(10,20]")])), "[(1,3), (4,5], (10,20]]")  
    
        
    
    def test_insert(self):
        self.assertEqual(str(insert([interval("(2,5)"),interval("(10,20]")], interval("[3,6]"))), "[(2,6], (10,20]]")
        self.assertEqual(str(insert([interval("(9,15]")], interval("[2,5]"))), "[[2,5], (9,15]]")


if __name__ == "__main__":
    unittest.main()
