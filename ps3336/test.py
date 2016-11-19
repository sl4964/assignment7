'''
Created on Nov 13, 2016

@author: peimengsui
'''
import unittest
from intervalclass import interval

class Test(unittest.TestCase):


    def setUp(self):
        pass
    def test_int(self):
        self.assertEqual(interval('[1,4]').lower,1)
        self.assertEqual(interval('[1,4]').upper,4)
        self.assertEqual(interval('(2,5]').lower,3)
        self.assertEqual(interval('(2,5]').upper,5)
        self.assertEqual(interval('[4,8)').lower,4)
        self.assertEqual(interval('[4,8)').upper,7)
        self.assertEqual(interval('(3,9)').lower,4)
        self.assertEqual(interval('(3,9)').upper,8)
        self.assertEqual(interval('[24,24]').lower,24)
        self.assertEqual(interval('[24,24]').upper,24)
    def test_Merge(self):
        self.assertEqual(interval.to_string([interval.mergeIntervals(interval('[1,3]'), interval('[3,5]'))]),'[1,5]')
        self.assertEqual(interval.to_string([interval.mergeIntervals(interval('[-1,4]'), interval('[2,3]'))]),'[-1,4]')
        self.assertEqual(interval.to_string([interval.mergeIntervals(interval('[2,3]'), interval('[1,2]'))]),'[1,3]')
        self.assertEqual(interval.to_string([interval.mergeIntervals(interval('[1,5]'), interval('[6,9]'))]),'[1,9]')
        self.assertEqual(interval.to_string([interval.mergeIntervals(interval('[1,23]'), interval('[24,24]'))]),'[1,24]')
    def test_MergeOvp(self):
        self.assertEqual(interval.to_string(interval.mergeOverlapping([interval('[1,5]'),interval('[2,6)'),interval('(8,10]'),interval('[8,18]')])), '[1,5], [8,18]')
        self.assertEqual(interval.to_string(interval.mergeOverlapping([interval('[-10,-7]'),interval('(-4,1]'),interval('[3,12)'),interval('[15,23]'),interval('[24,24]')])), '[-10,-7], (-4,1], [3,12), [15,24]')
    def test_InsertInt(self):
        self.assertEqual(interval.to_string(interval.insert([interval('[1,3]'),interval('[6,9]')], interval('[2,5]'))), '[1,9]')
        self.assertEqual(interval.to_string(interval.insert([interval('[1,2]'),interval('(3,5)'),interval('[6,7)'),interval('(8,10]'),interval('[12,16]')], interval('[4,9]'))), '[1,2], (3,10], [12,16]')
if __name__ == "__main__":
    unittest.main()


