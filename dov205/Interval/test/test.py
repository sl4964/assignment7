import unittest
from assignment7 import *


class IntervalTest(unittest.TestCase):
    """Unit-testing class that allows us to run tests with expected outcomes/

    Run the test in the project's root directory (e.g. pwd should be '.../dov205/')
    with the following command:

        $ python -m unittest discover
    """

    def test_valid_creation(self):
        """Test the creation of valid inputs to Interval constructor."""

        # Initialize list of values we would expect to be valid
        valid = ['[0, 10]', '[0, 10)', '(0, 10]', '(0, 10)',         # "Nice" inputs
                 '[0, 1]', '[0, 1)', '(0, 1]', '[0, +1]',
                 '[-1, 1]', '[-1, 1)', '(-1, 1]', '(-1, +1)',        # Start negative
                 '[-3, -1]', '[-3, -1)', '(-3, -1]', '(-3, -1)',     # Start, end negative
                 '[0,10]', ' [0,10]', ' [ 0,10]', ' [ +0 ,10]',      # Whitespace abuse
                 ' [ +0 , 10]', ' [ 0 , 10 ]', ' [ 0 , 10 ] ',
                 '[00, 10]',  '[-03, -00]', '[0, +000010]']          # Leading 0's

        # Create valid Interval objects for each string in our :valid string list.
        intervals = [Interval(candidate) for candidate in valid]

        # Assert that all intervals in :valid were made into
        # Interval objects in :intervals.
        self.assertEqual(len(valid), len(intervals), 'Error: invalid interval input in :valid list.')

    def test_invalid_parse(self):
        """Test the rejection of invalid inputs to Interval constructor."""

        # Define intervals that we would expect to raise a ParsingException
        invalid = ['', '[', ']', '[]', '(', ')', '()', '[,]',
                   '[4.0, 9.0]', '[1.1]', '[3, [4, 9]]', '[4i, 0]'
                   ]

        # Container for any valid intervals
        intervals = []

        # Attempt to create invalid Interval objects for each string in our object's :valid field.
        for candidate in invalid:
            with self.assertRaises(ParsingException):
                interval = Interval(candidate)
                intervals.append(interval)

        # Assert that not a single interval was instantiated.
        self.assertEqual(0, len(intervals), 'Error: valid interval input in :invalid list.')

    def test_equal(self):
        """Unit test equality among equal intervals."""

        # Initialize intervals that are equal to one another.
        eq_1, eq_2 = Interval('[1, 3]'), Interval('[1, 4)')
        eq_3, eq_4 = Interval('(0, 3]'), Interval('(0, 4)')
        eq_5, eq_6 = Interval('  [01,  03 ]     '), Interval('(000,0004   )')

        # Assert that all are equal.
        equal_error = 'Error: Intervals that should be equal are not equal.'
        self.assertEqual(eq_1, eq_2, equal_error)
        self.assertEqual(eq_2, eq_3, equal_error)
        self.assertEqual(eq_3, eq_4, equal_error)
        self.assertEqual(eq_4, eq_5, equal_error)
        self.assertEqual(eq_5, eq_6, equal_error)

    def test_unequal(self):
        """Unit test inequality among unequal intervals."""

        # Initialize intervals that are not equal to one another.
        ne_1, ne_2 = Interval('[0, 5]'), Interval('[0, 5)')
        ne_3, ne_4 = Interval('(-00001, 5]'), Interval('(-2, 4]')

        # Assert that all are not equal.
        not_equal_error = 'Error: Intervals that should not be equal are equal.'
        self.assertNotEqual(ne_1, ne_2, not_equal_error)
        self.assertNotEqual(ne_2, ne_3, not_equal_error)
        self.assertNotEqual(ne_3, ne_4, not_equal_error)

    def test_valid_merge_overlapping(self):
        """Unit test valid merging of overlapping intervals."""

        # Initialize intervals that are merge-able, join into a list.
        t_1, t_2 = Interval('[0, 1]'), Interval('[2, 3]')
        t_3, t_4 = Interval('[4, 6]'), Interval('(4, 9]')
        intervals_list = [t_1, t_2, t_3, t_4]

        # Define our expected merge result.
        expected_result = Interval('[0, 9]')
        result = merge_overlapping(intervals_list)[0]

        # Assert that after merging overlapping Intervals we arrive at
        # the expected result.
        self.assertEqual(result, expected_result, 'Error: merge overlapping returned invalid result.')

    def test_provided_merge_overlapping(self):
        """Unit test valid inputs based on example assignment inputs."""

        # (3) merge_overlapping()

        # Define (3)'s string intervals and create their Interval representations.
        string_intervals = ['[1,5]', '[2,6)', '(8,10]', '[8,18]']
        intervals = [Interval(intervals) for intervals in string_intervals]

        # Obtain result from call to merge_overlapping and define correct result.
        result = merge_overlapping(intervals)
        expected_result = [Interval('[1,6)'), Interval('[8,18]')]

        # Assert our :result and :expected_result are equal.
        self.assertEqual(result, expected_result, 'Error: merge_overlapping() is incorrect on sample input.')

    def test_provided_insert(self):
        """Unit test valid inputs based on example assignment inputs."""

        # (4) insert()

        # Define examples as nested dictionary. Each iteration over :examples
        # is self-contained in its own nested dictionary.
        examples = {1: {'string_intervals': ['[1,3]', '[6,9]'],
                        'intervals': [],
                        'result': [],
                        'insert': Interval('[2,5]'),
                        'expected_result': [Interval('[1,9]')]
                        },
                    2: {'string_intervals': ['[1,2]', '(3,5)', '[6,7)', '(8,10]', '[12,16]'],
                        'intervals': [],
                        'result': [],
                        'insert': Interval('[4,9]'),
                        'expected_result': [Interval('[1,2]'), Interval('(3,10]'), Interval('[12,16]')]
                        }
                    }

        # Check both provided examples work fine.
        for example in examples.values():

            # Create example's Interval representations of string intervals.
            example['intervals'] = [Interval(intervals) for intervals in example['string_intervals']]

            # Obtain result from call to insert()
            example['result'] = insert_into(example['intervals'], example['insert'])

            # Assert our :result and :expected_result are equal.
            self.assertEqual(example['result'], example['expected_result'],
                             'Error: insert_into() is incorrect on sample input.')

    def test_provided_interactive_input(self):
        """Unit test valid sequence of insertions based on example assignment inputs."""

        # (5) interactive input (main() in assignment7.py)

        # Emulate main()'s execution. Provide string and split on commas
        # to simulate user input.
        string_intervals = '[-10,-7], (-4,1], [3,6), (8,12), [15,23]'.split(',')

        # Create intervals from our list of comma-delimited strings.
        intervals = create_intervals(string_intervals)

        # Define our error message for ease on the eyes.
        error = 'Error: interactive is incorrect on sample input.'

        # Perform each insert into our :intervals list.
        intervals = insert_into(intervals, Interval('[4,8]'))

        intervals = insert_into(intervals, Interval('[24,24]'))

        # Catch the RangeMismatchException raised by attempting to create interval [4,-1].
        with self.assertRaises(RangeMismatchException):
            intervals = insert_into(intervals, Interval('[4,-1]'))

        intervals = insert_into(intervals, Interval('[12,13)'))

        # Catch the RangeException raised by attempting to create interval (3,4).
        with self.assertRaises(RangeException):
            intervals = insert_into(intervals, Interval('(3,4)'))

        intervals = insert_into(intervals, Interval('(2,12)'))

        intervals = insert_into(intervals, Interval('(-7,-2]'))

        # Attempting to coerce 'foo' into an Interval raises a ParsingException.
        with self.assertRaises(ParsingException):
            intervals = insert_into(intervals, Interval('foo'))

        intervals = insert_into(intervals, Interval('[-2,5]'))

        # Define our expected intervals list.
        expected_intervals = [Interval('[-10,13)'), Interval('[15,24]')]

        # If everything's gone right, :intervals should match :expected_intervals.
        self.assertEqual(intervals, expected_intervals, error)


if __name__ == '__main__':
    unittest.main()
