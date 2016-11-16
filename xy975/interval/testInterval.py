from interval import *
import unittest

class intervalTest(unittest.TestCase):
    """
    Test functions in class interval.
    Assume that the type of inputs are strings or list of strings.
    """
    def testInterval(self):    
        self.assertEqual(str(interval('[1,4]')),'[1,4]')
        self.assertEqual(str(interval('(2, 5]')),'(2, 5]')
        self.assertEqual(str(interval('[4,8)')),'[4,8)')
        self.assertEqual(str(interval('(3,9 )')),'(3,9 )')
        
        with self.assertRaises(ValueError):
            str(interval('(1,1)'))
        with self.assertRaises(ValueError):
            str(interval('(3,2]'))
        with self.assertRaises(ValueError):
            str(interval('(15)'))
        with self.assertRaises(ValueError):
            str(interval('(1,3,5]'))
        with self.assertRaises(ValueError):
            str(interval('1,23'))
        with self.assertRaises(ValueError):
            str(interval('(1,!)'))
        with self.assertRaises(ValueError):
            str(interval('( , )'))            
        with self.assertRaises(ValueError):
            str(interval('(as,df)'))
        with self.assertRaises(ValueError):
            str(interval('asdf'))
            
        print ('Test interval finished..')

    def testMergeIntervals(self):
        self.assertEqual(mergeIntervals('(1,4)','(2,5]'),'(1,5]')
        self.assertEqual(mergeIntervals('(3,5)','[5,7)'),'(3,7)')
        self.assertEqual(mergeIntervals('[7,9]','[2,6]'),'[2,9]')
        
        with self.assertRaises(TypeError):
            mergeIntervals('(1,4)')
        with self.assertRaises(ValueError):
            mergeIntervals('(1,4)','asdf')            
        with self.assertRaises(ValueError):
            mergeIntervals('(1,4)','(4,7)')            

        print ('Test mergeIntervals finished..')

    def testMergeOverlapping(self):
        self.assertEqual(mergeOverlapping(['(1,4)','[2,5]']),'(1,5]')
        self.assertEqual(mergeOverlapping(['(1,4)']),'(1,4)')
        self.assertEqual(mergeOverlapping(['[1,5]','[2,6)','(8,10]','[8,18]']),'[1,5], [8,18]')
        self.assertEqual(mergeOverlapping(['[1,5)','[5,6)','[6,10)','[10,18]']),'[1,18]')

        with self.assertRaises(ValueError):
            mergeOverlapping(['[1,5]','[6,2)'])
        with self.assertRaises(ValueError):
            mergeOverlapping(['[1,5]','2,6'])
        with self.assertRaises(ValueError):
            mergeOverlapping(['[1,5]','asdf'])
             
        print ('Test mergeOverlapping finished..')

    def testInsert(self):
        intervals = ['[-10,-7]', '(-4,1]', '[3,6)', '(8,12)', '[15,23]']
        self.assertEqual(insert(intervals, '[4,8]'),'[-10,-7], (-4,1], [3,12), [15,23]')
        intervals = ['[-10,-7]', '(-4,1]', '[3,12)', '[15,23]']
        self.assertEqual(insert(intervals, '[24,24]'),'[-10,-7], (-4,1], [3,12), [15,24]')
        intervals = ['[-10,-7]', '(-4,1]', '[3,12)', '[15,24]']
        self.assertEqual(insert(intervals, '(-7,-2]'),'[-10,1], [3,12), [15,24]')
        intervals = ['[-10,1]', '[3,12)', '[15,24]']
        self.assertEqual(insert(intervals, '[-2,5]'),'[-10,12), [15,24]')
            
        with self.assertRaises(ValueError):
            insert(intervals, '[-2,-5]')     
        with self.assertRaises(ValueError):
            insert(intervals, 'foo')     
        with self.assertRaises(ValueError):
            insert(['[-10,1]', '[3,12)', '[15,4]'], '[-2,5]') 
                     
        print ('Test insert finished..') 
        
        intervals = None
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(intervalTest("testInterval"))
    suite.addTest(intervalTest("testMergeIntervals"))
    suite.addTest(intervalTest("testMergeOverlapping"))
    suite.addTest(intervalTest("testInsert"))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)