'''
This is the module for tests.
@author: ShashaLin
'''
import unittest
from funcs import interval, mergeIntervals, mergeOverlapping, insert
from Errors import InputError, MergeError
class Test(unittest.TestCase):
    
    def testInterval(self):
        self.assertIsInstance(interval('[-10,-7]'), interval)
        self.assertIsInstance(interval('(-4,1]'), interval)
        self.assertIsInstance(interval('[3,6)'), interval)
        self.assertIsInstance(interval('(8,12)'), interval)
        self.assertRaises(InputError, interval, '(8,-12)')
        self.assertRaises(InputError, interval, '(-1,-1)')
    
    def test_mergeIntervals(self):
        self.assertEqual(mergeIntervals('(-7,-6]', '[-5,1)'), '(-7,1)' )
        self.assertEqual(mergeIntervals('(-7,-6]', '(-6,2]'), '(-7,2]' )         
        self.assertEqual(mergeIntervals('[110,720)', '(719,730]'), '[110,730]' ) 
        self.assertRaises(MergeError, mergeIntervals, '[0,3)', '[4,7]')                   
    
    def test_mergeOverlapping(self):
        self.assertEqual(mergeOverlapping('[-10,-7], (-4,1], [3,6), (8,12), [15,23], [4,8]'), \
                         '[-10,-7], (-4,1], [3,12), [15,23]')
        self.assertEqual(mergeOverlapping('[-3,5), (5,10], [10,17), [17,23]'), \
                         '[-3,5), (5,23]')
        
    def test_insert(self):
        self.assertEqual(insert('[0,9), [11,27)', '(8,10]'), '[0,27)')
        self.assertEqual(insert('[4,6), (7,12]', '(13,14]'), '[4,6), (7,12], (13,14]')
                         
                         
if __name__ == '__main__':
    unittest.main()