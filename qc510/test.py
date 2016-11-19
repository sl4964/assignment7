import unittest
from assignment7 import interval,mergeOverlapping,insert,mergeIntervals

class UnitTestForInter(unittest.TestCase):
    
    def test_constructor(self):
        class_test = interval('[2,6)')
        class_interv = '[2,6)'
        class_front='['
        class_lower=2
        class_upper=6
        class_end = ')'
        self.assertEqual(class_test.interv,class_interv)
        self.assertEqual(class_test.front,class_front)
        self.assertEqual(class_test.lower,class_lower)
        self.assertEqual(class_test.upper,class_upper)
        self.assertEqual(class_test.end,class_end)
    def test_mergeIntervals(self):
        class_test_first = mergeIntervals('[2,6]','[7,10)')
        class_result_first = '[2,10)'
        self.assertEqual(class_test_first,class_result_first)
        

    def test_mergeOverlapping(self):
        class_test_first = mergeOverlapping('[2,6],[7,10),[12,15)')
        class_result_first = ['[2,10)','[12,15)']
        self.assertEqual(class_test_first,class_result_first)
    
    def test_insert(self):
        class_test_first = insert(['[2,6]','[7,10)','[12,15)'],'[17,19]')
        class_result_first =['[2,10)', '[12,15)', '[17,19]']
        self.assertEqual(class_test_first,class_result_first)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()