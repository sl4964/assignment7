import unittest
from interval import *

class intervalTest(unittest.TestCase):
    '''
    Tests for the interval class helper functions, overloaded methods, and methods
    '''
    
    def testinclusiveLowerVal(self):
        '''
        Test inclusiveLowerBoundValue() returns normalized lower bound value
        '''
        self.assertEqual(interval("(0,2)").inclusiveLowerBoundValue(), 1)
        self.assertEqual(interval("[0,2)").inclusiveLowerBoundValue(), 0)
    
    def testinclusiveUpperVal(self):
        '''
        Test inclusiveUpperBoundValue() returns normalized upper bound value
        '''
        self.assertEqual(interval("(0,2)").inclusiveUpperBoundValue(), 1)
        self.assertEqual(interval("[0,2]").inclusiveUpperBoundValue(), 2)
    
    def testComparisonVals(self):
        '''
        Test comparisonValues() returns tuple of normalized lower, normalized upper, original lower, original upper bound vals
        '''
        self.assertEqual(interval("(0,3)").comparisonValues(), (1, 2, 0, 3))
        self.assertEqual(interval("[0,3]").comparisonValues(), (0, 3, 0, 3))
    
    def testeq(self):
        '''
        Test overloaded "=" operator for interval objects
        '''
        self.assertTrue(interval("(-1,3)") == interval("(-1,3)"))
        self.assertFalse(interval("(-1,3)") == interval("[0,2]"), 
                         "Error: Normalized equal intervals should not be literally equal")
   
    def testlt(self):
        '''
        Test overloaded "<" operator for interval objects
        '''
        self.assertLess(interval("(-1,3)"), interval("[0,3]"))

class containsTests(unittest.TestCase):
'''
Tests for contains method from interval class, grouped here for clarity
'''
    
    def testSelf(self):
        '''
        Test interval contains identical interval
        '''
        self.assertTrue(interval("(-1,3)").contains(interval("(-1,3)")))
    
    def testInclusiveContainsExclusive(self):
        '''
        Test inclusive bound contains exclusive bound e.g. [x,y] contains (x,y)
        '''
        self.assertTrue(interval("[-1,3]").contains(interval("(-1,3)")))
    
    def testExclusiveNotContainInclusive(self):
        '''
        Test exclusive bound does not contain inclusive bound
        '''
        self.assertFalse(interval("(-1,3)").contains(interval("[-1,3]")))
    
    def testContains(self):
        '''
        Test contains on interval that is proper subset
        '''
        self.assertTrue(interval("(-1,3)").contains(interval("(0,2)")))

        
    def testAdjacent(self):
        '''
        Test that x) and [x are adjacent but not x) and (x
        '''
        self.assertTrue(interval("(0,3)").adjacent(interval("[3,4]")))
        self.assertFalse(interval("(0,3)").adjacent(interval("(3,4]")))
        
    def testIntersects(self):
        '''
        Test that overlapping intervals intersect
        '''
        self.assertTrue(interval("(3,5]").intersects(interval("[5,7]")))

class parseListTests(unittest.TestCase):
'''
Tests for parseLists classmethod from interval, grouped for clarity
'''
    
    def testValidList(self):
        '''
        Test that valid format string input is parsed into list of interval objects
        '''
        self.assertEqual(interval.parseList("[0,3], [5,6]"), [interval("[0,3]"), interval("[5,6]")])
    
    def testEmpty(self):
        '''
        Test that empty string input is parsed into empty list
        '''
        self.assertEqual(interval.parseList(""), [])
    
    def testInvalidList(self):
        '''
        Test that invalid input string (i.e. invalid interval) raises ValueError
        '''
        with self.assertRaises(ValueError):
            interval.parseList("(1,1), (2,5)")

class MergeIntervalsTests(unittest.TestCase):
'''
Tests for mergeIntervals method from interval class, grouped here for clarity
'''
    
    def testDisjoint(self):
        '''
        Test that mergeInterval raises Exception when passed disjoint intervals 
        '''
        with self.assertRaises(Exception):
            mergeIntervals(interval("(3,5)"), interval("(5,8)"))
    
    def testContains(self):
        '''
        Test that mergeInterval works on interval that contains other interval
        '''
        self.assertEqual(mergeIntervals(interval("(0,6)"), interval("[1,5]")), interval("(0,6)"))
    
    def testAdjacent(self):
        '''
        Test that mergeInterval merges adjacent intervals
        '''
        self.assertEqual(mergeIntervals(interval("[3,5]"), interval("(5,8)")), interval("[3,7]"))        
                
    def testIntersecting(self):   
        '''
        Test that mergeInterval merges intersecting intervals
        ''' 
        self.assertEqual(mergeIntervals(interval("[3,5]"), interval("[4,8)")), interval("[3,7]"))

class IntervalMergeOverlappingTests(unittest.TestCase):
'''
Tests for mergeOverlapping method from interval class, grouped for clarity
'''
    
    def testEmpty(self):
        '''
        Test for empty list
        '''
        self.assertEqual(mergeOverlapping([]), [])

    def testOne(self):
        '''
        Test for list of single interval
        '''
        intervals = [interval("[1,2]")]
        self.assertEqual(mergeOverlapping(intervals), intervals)
        
    def testNoneOverlap(self):
        '''
        Test that nonoverlapping interval is added to list but not merged
        '''
        intervals = [interval("(0,2)"), interval("(2,5)")]
        self.assertEqual(mergeOverlapping(intervals), intervals)
    
    def testStartOverlap(self):
        '''
        Test that mergeOverlapping merges overlapping intervals at the start of list
        '''
        intervals = [interval("(0,2]"), interval("(2,5)"), interval("(6,8)")]
        self.assertEqual(mergeOverlapping(intervals), [interval("[1,4]"), interval("(6,8)")])
    
    def testMiddleOverlap(self):
        '''
        Test that mergeOverlapping merges intervals in middle of list
        '''
        intervals = [interval("(0,2)"), interval("(2,5]"), interval("[4,8)"), interval("(10,12)")]
        self.assertEqual(mergeOverlapping(intervals), [interval("(0,2)"), interval("[3,7]"), interval("(10,12)")])
    
    def testEndOverlap(self):
        '''
        Test that mergeOverlapping merges intervals at end of list
        '''
        intervals = [interval("(0,2]"), interval("(3,5)"), interval("(4,8)")]
        self.assertEqual(mergeOverlapping(intervals), [interval("(0,2]"), interval("[4,7]")])
        
    def testAllOverlap(self):
        '''
        Test that mergeOverlapping merges all members of list of overlapping intervals
        '''
        intervals = [interval("(0,2]"), interval("[1,5)"), interval("[4,8)")]
        self.assertEqual(mergeOverlapping(intervals), [interval("[1,7]")])
    
    def testOverlapEx(self):
        '''
        Test that mergeOverlapping correctly merges example given in Assignment7 instructions
        '''
        intervals = [interval("[1,5]"), interval("[2,6)"), interval("(8,10]"), interval("[8,18]")]
        self.assertEqual(mergeOverlapping(intervals), [interval("[1,5]"), interval("[8,18]")]) 

class InsertTests(unittest.TestCase):
'''
Tests for insert method method from interval class, grouped for clarity
''' 
    def testEmptyList(self):
        '''
        Test that insert works on empty list
        '''
        intervals = []
        insertInt = interval("(1,3)")
        self.assertEqual(insert(intervals, insertInt), [insertInt])
    
    def testInsertWithoutMerge(self):
        '''
        Test that insert adds interval to list when none can be merged
        '''
        intervals = [interval("(0,3)"), interval("(6,10)")]
        insertInt = interval("(4,5]")
        self.assertEqual(insert(intervals, insertInt), [interval("(0,3)"), interval("(4,5]"), interval("(6,10)")])
        
    def testInsertMiddleAndMerge(self):
        '''
        Test that insert merges interval at middle of list
        '''
        intervals = [interval("(0,5)"), interval("(6,10)")]
        insertInt = interval("(4,8]")
        self.assertEqual(insert(intervals, insertInt), [interval("[1, 9]")])
    
    def testInsertEndMerge(self):
        '''
        Test that insert merges interval at an extremity of list
        '''
        intervals = [interval("(4,8]"), interval("(6,10)")]
        insertInt = interval("(0,5)")
        self.assertEqual(insert(intervals, insertInt), [interval("[1, 9]")])

if __name__ == '__main__':
    unittest.main()
    