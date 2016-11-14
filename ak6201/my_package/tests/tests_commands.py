import sys
sys.path.append('..')

import unittest
from main_file import interval

class TestInput(unittest.TestCase):
    def setUp(self):
        test_interval = interval('[1,2]', 0) # the second parameter(to_print_or_not) is 0 because we don't want to print "Invalid Input" for invalid inputs while running test cases
        test_interval.to_print_or_not = 0        
    def test_constructor_valid_string(self):
        test_interval = interval('[2,5]', 0)
        self.assertEqual(test_interval.valid_string, 1)
    def test_constructor_invalid_string_inclusive_bounds(self):
        test_interval = interval('[6,5]', 0)
        self.assertEqual(test_interval.valid_string, 0)
    def test_constructor_invalid_string_exclusive_bounds_type_1(self):
        test_interval = interval('(2,2)', 0)
        self.assertEqual(test_interval.valid_string, 0)
    def test_constructor_invalid_string_exclusive_bounds_type_2(self):
        test_interval = interval('(2,3)', 0)
        self.assertEqual(test_interval.valid_string, 0)
    def test_constructor_invalid_string_exclusive_bounds_type_3(self):
        test_interval = interval('(4,3)', 0)
        self.assertEqual(test_interval.valid_string, 0)
    def test_constructor_invalid_string_inclusive_and_exclusive_bounds_type_1(self):
        test_interval = interval('[3,3)', 0)
        self.assertEqual(test_interval.valid_string, 0)
    def test_constructor_invalid_string_inclusive_and_exclusive_bounds_type_2(self):
        test_interval = interval('(3,3]', 0)
        self.assertEqual(test_interval.valid_string, 0)
    def test_constructor_invalid_string_inclusive_and_exclusive_bounds_type_3(self):
        test_interval = interval('(5,3]', 0)
        self.assertEqual(test_interval.valid_string, 0)
    def test_input_as_string(self):
        test_interval = interval('fooooo', 0)
        self.assertEqual(test_interval.valid_string, 0)
    def test_incomplete_input(self):
        test_interval = interval('[234,678', 0)
        self.assertEqual(test_interval.valid_string, 0)

class TestMergeOverlapping(unittest.TestCase):
    def setUp(self):
        self.int = interval('[1,2]', 0) # A sample instance of the class 'interval' is created --> so that we don't need to create
                                        # an instance of the class for every test case. We can use this sample for all the test cases
    def test_check_1(self):
        self.assertEqual(self.int.mergeOverlapping('[1,5], [2,6), (8,10], [8,18]'), ['[1,6)', '[8,18]'])
    def test_check_2(self):
        self.assertEqual(self.int.mergeOverlapping('[1,5], [8,18], (19,25)'), ['[1,5]', '[8,18]', '(19,25)'])
    def test_check_3(self):
        self.assertEqual(self.int.mergeOverlapping('[1,5], (3,9), [5,10]'), ['[1,10]'])
    def test_check_4(self):
        self.assertEqual(self.int.mergeOverlapping('(1,5), (3,9], (1005,10007]'), ['(1,9]', '(1005,10007]'])
        
class TestMergeInterval(unittest.TestCase):
    def setUp(self):
        self.int = interval('[1,2]', 0)      # A sample instance of the class 'interval' is created --> so that we don't need to create
                                             # an instance of the class for every test case. We can use this sample for all the test cases
    def test_check_merged_type_1(self):
        self.assertEqual(self.int.mergeIntervals('(1,5)', '(3,7)', 0), '(1,7)')
    def test_check_merged_type_2(self):
        self.assertEqual(self.int.mergeIntervals('(1,5]', '[6,7)', 0), '(1,7)')
    def test_check_merged_type_3(self):
        self.assertEqual(self.int.mergeIntervals('[1,4]', '[2,3]', 0), '[1,4]')
    def test_check_merged_type_4(self):
        self.assertEqual(self.int.mergeIntervals('[1,6]', '[4,9]', 0), '[1,9]')
    def test_check_merged_type_5(self):
        self.assertEqual(self.int.mergeIntervals('[1,5)', '(3,17)', 0), '[1,17)')
    def test_check_not_mergeable_type_1(self):
        self.assertEqual(self.int.mergeIntervals('(1,5)', '(6,7)', 0), -1)
    def test_check_not_mergeable_type_2(self):
        self.assertEqual(self.int.mergeIntervals('[1,5]', '[7,8]', 0), -1)
    def test_check_not_mergeable_type_3(self):
        self.assertEqual(self.int.mergeIntervals('(11,14]', '(15,56]', 0), -1)

class TestInsert(unittest.TestCase):
    def setUp(self):
        self.int = interval('[1,2]', 0)
        
    def test_check_1(self):
        self.assertEqual(self.int.insert('[-10,-7], (-4,1], [3,6), (8,12), [15,23]', '[4,8]'), ['[-10,-7]', '(-4,1]', '[3,12)', '[15,23]'])
    def test_check_2(self):
        self.assertEqual(self.int.insert('[-10,-7], (-4,1], [3,12), [15,23]', '[24,24]'), ['[-10,-7]', '(-4,1]', '[3,12)', '[15,24]'])
    def test_check_3(self):
        self.assertEqual(self.int.insert('[-10,-7], (-4,1], [3,12), [15,24]', '[12,13)'), ['[-10,-7]', '(-4,1]', '[3,13)', '[15,24]'])
    def test_check_4(self):
        self.assertEqual(self.int.insert('[-10,-7], (-4,1], [3,12), [15,24]', '(2,12)'), ['[-10,-7]', '(-4,1]', '(2,12)', '[15,24]'])
    def test_check_5(self):
        self.assertEqual(self.int.insert('[-10,-7], (-4,1], [3,13), [15,24]', '(-7,-2]'), ['[-10,1]', '[3,13)', '[15,24]'])
    def test_check_6(self):
        self.assertEqual(self.int.insert('[-10,1], [3,13), [15,24]', '[-2,5]'), ['[-10,13)', '[15,24]'])
    def test_check_invalid_input_1(self):
        self.assertEqual(self.int.insert('[-10,-7], (-4,1], [3,12), [15,24]', '[4,-1]'), 'Invalid Input')
    def test_check_invalid_input_2(self):
        self.assertEqual(self.int.insert('[-10,-7], (-4,1], [3,13), [15,24]', '(3,4)'), 'Invalid Input')
    def test_check_invalid_input_3(self):
        self.assertEqual(self.int.insert('[-10,1], [3,13), [15,24]', 'foo'), 'Invalid Input')
        



if __name__ == "__main__":
    unittest.main()