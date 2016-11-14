import unittest
from assignment7 import *
from interval import interval

class solutionTest(unittest.TestCase):
    
    """ test for mergeIntervals() """
    def test_mergeIntervals(self):
        i = interval()
        int1 = interval('[',1,5,']')
        int2 = interval('[',2,6,']')
        int3 = interval('[',1,6,']')
        self.assertEqual(i.mergeIntervals(int1, int2).bra1, int3.bra1)
        self.assertEqual(i.mergeIntervals(int1, int2).bra2, int3.bra2)
        self.assertEqual(i.mergeIntervals(int1, int2).start, int3.start)
        self.assertEqual(i.mergeIntervals(int1, int2).end, int3.end)

    """ test for mergeOverlapping() """
    def test_mergeOverlapping(self):
        i = interval()
        int1 = interval('[',1,5,']')
        int2 = interval('[',2,6,')')
        int3 = interval('(',8,10,']')
        int4 = interval('[',8,18,']')
        int5 = interval('[',1,6,')')
        int6 = interval('[',8,18,']')
        list = [int1, int2, int3, int4]
        ans = [int5, int6]
        self.assertEqual(i.mergeOverlapping(list)[0].bra1,ans[0].bra1)
        self.assertEqual(i.mergeOverlapping(list)[0].bra2,ans[0].bra2)
        self.assertEqual(i.mergeOverlapping(list)[0].start,ans[0].start)
        self.assertEqual(i.mergeOverlapping(list)[0].end,ans[0].end)
        self.assertEqual(i.mergeOverlapping(list)[1].bra1,ans[1].bra1)
        self.assertEqual(i.mergeOverlapping(list)[1].bra2,ans[1].bra2)
        self.assertEqual(i.mergeOverlapping(list)[1].start,ans[1].start)
        self.assertEqual(i.mergeOverlapping(list)[1].end,ans[1].end)

    """ test for insert() """
    def test_insert(self):
        i = interval()
        int1 = interval('[',1,3,']')
        int2 = interval('[',6,9,']')
        int3 = interval('[',2,5,']')
        int4 = interval('[',1,9,']')
        list = [int1, int2]
        ans = [int4]
        self.assertEqual(i.insert(list,int3)[0].bra1,ans[0].bra1)
        self.assertEqual(i.insert(list,int3)[0].bra2,ans[0].bra2)
        self.assertEqual(i.insert(list,int3)[0].start,ans[0].start)
        self.assertEqual(i.insert(list,int3)[0].end,ans[0].end)
        
if __name__ == "__main__":
    unittest.main()