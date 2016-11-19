import unittest
from interval import interval,mergeIntervals,mergeOverlapping,insert

"""This is test function for the class interval and the functions 
mergeIntervals(), mergeOverlapping(), and insert()"""

class interval_test(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_interval1(self):
        testint = interval("[3,4]")
        self.assertEqual(testint.lower,3)
        self.assertEqual(testint.upper,4)
        self.assertEqual(testint.leftmost,"[")
        self.assertEqual(testint.rightmost,"]")
        
    def test_interval2(self):
        testint = interval("[-1,10)")
        self.assertEqual(testint.lower,-1)
        self.assertEqual(testint.upper,10)
        self.assertEqual(testint.leftmost,"[")
        self.assertEqual(testint.rightmost,")")
    
    def test_interval3(self):
        testint = interval("[7,7]")
        self.assertEqual(testint.lower,7)
        self.assertEqual(testint.upper,7)
        self.assertEqual(testint.leftmost,"[")
        self.assertEqual(testint.rightmost,"]")
    
    def test_interval4(self):
        with self.assertRaises(ValueError) as cm:
            interval("(3,4)")
        thisexception = cm.exception
        self.assertEquals(str(thisexception), "Invalid boundary values")
          
    def test_mergeIntervals_1(self):
        int1 = interval('(-1,9]')
        int2 = interval('[7,10]')
        int3 = mergeIntervals(int1,int2)
        self.assertEqual(str(int3), '(-1,10]')

    def test_mergeIntervals_2(self):
        int1 = interval('[1,3]')
        int2 = interval('[0,4]')
        int3 = mergeIntervals(int1,int2)
        self.assertEqual(str(int3), '[0,4]')


    def test_mergeIntervals_4(self):
        int1 = interval('[5,8)')
        int2 = interval('(8,10]')
        with self.assertRaises(ValueError) as cm:
            mergeIntervals(int1,int2)
        thisexception = cm.exception
        self.assertEquals(str(thisexception), "Invalid input: disjoint intervals")

    def test_mergeOverlapping_1(self):
        intlist = [interval('[-10,-7]'),interval('(-7,1]'),interval('[3,12)'),interval('[10,23]')]
        self.assertEqual(str(mergeOverlapping(intlist)), '[[-10,1], [3,23]]')

    def test_mergeOverlapping_2(self):
        intlist = [interval('(-1,3]'),interval('(5,9]'),interval('[11,12)')]
        self.assertEqual(str(mergeOverlapping(intlist)), '[(-1,3], (5,9], [11,12)]')

    def test_mergeOverlapping_3(self):
        intlist = [interval('[10,11]'),interval('(5,16]')]
        self.assertEqual(str(mergeOverlapping(intlist)), '[(5,16]]')

    def test_insert_1(self):
        intlist = [interval('[-10,-7]'),interval('(-4,1]'),interval('[3,12)'),interval('[15,23]')]
        self.assertEqual(str(insert(intlist,interval("[24,24]"))), '[[-10,-7], (-4,1], [3,12), [15,24]]')
        
    def test_insert_2(self):
        intlist = [interval('(-13,-5)'),interval('(-5,2]'),interval('(7,10]')]
        self.assertEqual(str(insert(intlist,interval("[20,24]"))), '[(-13,-5), (-5,2], (7,10], [20,24]]')
        
    def test_insert_3(self):
        intlist = [interval('[-10,1]'),interval('[3,13)'),interval('[15,24]')]
        self.assertEqual(str(insert(intlist,interval("[-2,5]"))), '[[-10,13), [15,24]]')

if __name__ == '__main__':
    unittest.main()
