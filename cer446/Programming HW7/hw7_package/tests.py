'''
Created on Nov 14, 2016

@author: Caroline
'''
#got the test to work but it failed

import unittest
import interval_class as i
import functions as m

#test 0: Interval class

class Interval_test_case(unittest.TestCase):
    def setUp(self):
        print('In interval class setUp')
        self.input1 = '[-1,4)'
        self.output1=[-1, 0, 1, 2, 3]
        
    def tearDown(self):
        print('In interval class tearDown')
        del self.input1
        del self.output1
        
class Test_interval_creation(Interval_test_case):
    def test_interval_creation(self):
        self.assertEqual(i.Interval(self.input1).interval_list, self.output1)

#test 1: merge intervals

class Merge_intervals_test_case(unittest.TestCase):
    def setUp(self):
        print('In merge interval setUp')
        self.merged_interval = i.Interval('[-1,10)')
        self.first_interval = i.Interval('[-1,5]')
        self.second_interval = i.Interval('(4,10)')
        
    def tearDown(self):
        print('In merge interval tearDown')
        del self.merged_interval
        del self.first_interval
        del self.second_interval
        
class Test_Merge_Intervals(Merge_intervals_test_case):
    def test_merge(self):
        self.assertEqual(vars(m.Merge_intervals(self.first_interval,self.second_interval)), vars(self.merged_interval), 'Merged interval does not match intended result')

#test 2: merge overlapping

class mergeOverlapping_test_case(unittest.TestCase):
    def setUp(self):
        print('In merge overlapping setUp')
        self.interval_list_input = [i.Interval('[1,5]'), i.Interval('[2,6)'), i.Interval('(8,10]'), i.Interval('[8,18]')]
        self.interval_list_output = [i.Interval('[1,6)'), i.Interval('[8,18]')]
    
    def tearDown(self):
        print('In merge overlapping tearDown')
        del self.interval_list_input
        del self.interval_list_output

class Test_mergeOverlapping(mergeOverlapping_test_case): 
    def test_mergeOverlapping(self):
        self.assertEqual(str(m.mergeOverlapping(self.interval_list_input)), str(self.interval_list_output))

#test 3: insert
        
class insert_test_case(unittest.TestCase):
    def setUp(self):
        print('in insert setUp')
        self.interval_list_input = [i.Interval('[1,3]'), i.Interval('[6,9]')]
        self.interval_insert = [i.Interval('[2,5]')]
        self.interval_insert_output = [i.Interval('[1,9]')]
        
    def tearDown(self):
        print('in insert tearDown')
        del self.interval_list_input
        del self.interval_insert
        del self.interval_insert_output

class Test_insert(insert_test_case):
    def test_insert(self):
        self.assertEqual(str(m.insert(self.interval_list_input, self.interval_insert)), str(self.interval_insert_output))
        
        
if __name__== '__main__':
    unittest.main()
        

        
