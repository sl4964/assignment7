
# coding: utf-8

# In[ ]:
#Test class 
from interval1 import *
import unittest
class Test(unittest.TestCase):
    def testinterval(self):
        test_data = '[1,7]'
        interval_data = interval(test_data)
        self.assertEqual(str(test_data), str(interval_data))

    def testmergeinterval(self):
        test_data1 = "[2,6]"
        test_data2 = "[3,8)"
        self.assertEqual(str(mergeIntervals(interval(test_data1),interval(test_data2))), "[2,8)")

    def testmergeoverlapping(self):
        test_data4 = interval("(3,5)")
        test_data5 = interval("[4,7)")
        test_data6 = interval("(6,9]")
        test_data7 = mergeOverlapping([test_data4,test_data5,test_data6])
        self.assertEqual(str(test_data7), "[(3,9]]")

    def testinsert(self):
        test_data8 = interval("(3,5)")
        test_data9 = interval("[4,7)")
        test_data10 = interval("(6,9]")
        test_data11 = insert([test_data8,test_data9], test_data10)
        self.assertEqual(str(test_data11), "[(3,9]]")
    
        
if __name__ =="__main__":
    unittest.main()     

