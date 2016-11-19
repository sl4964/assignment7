'''
This test module tests:
    - interval class with its methods
    - mergeIntervals functions
    - mergeOverlapping functions
    - insert functions
    - exceptions

NetID: xc965
'''

import unittest
from interval import *


class UserTest(unittest.TestCase):
    """
    This class allows us to run tests with class and functions.
    Import the test from the project's top level directory
    with this command:
    $ python -m unittest discover
    """

    def test_interval(self):
        """
        This test function examines the interval class from three aspects:
            1) representation
            2) other methods
            3) exceptions
        """

        # test the string representation of interval
        self.assertEqual('(1,5]', str(interval('(1, 5]')))
        self.assertEqual('[-10,-5]', str(interval('[-10, -5]')))
        self.assertEqual('[3,15)', str(interval('[   3   ,  1  5   )')))
        self.assertEqual('(1000,5000)', str(interval('(1000, 5000)')))
        self.assertEqual('(04,05]', str(interval('(04, 05]')))
        self.assertEqual('[9,9]', str(interval('[9, 9]')))

        # test the methods
        t1 = interval('[-70, 700)')
        t2 = interval('(6, 19]')
        t3 = interval('[04, 05]')
        t4 = interval('(3, 6)')

        self.assertEqual('[', t1.l)
        self.assertEqual(')', t1.u)
        self.assertEqual(-70, t1.lb)
        self.assertEqual(699, t1.ub)
        self.assertEqual('[-70', t1.lower)
        self.assertEqual('700)', t1.upper)
        self.assertEqual('[-70,700)', t1.__repr__())
        self.assertEqual(range(-70, 700), t1.real_range())

        self.assertEqual('(', t2.l)
        self.assertEqual(']', t2.u)
        self.assertEqual(7, t2.lb)
        self.assertEqual(19, t2.ub)
        self.assertEqual('(6', t2.lower)
        self.assertEqual('19]', t2.upper)
        self.assertEqual('(6,19]', t2.__repr__())
        self.assertEqual(range(7, 20), t2.real_range())

        self.assertEqual(4, t3.lb)
        self.assertEqual(5, t3.ub)
        self.assertEqual('[04', t3.lower)
        self.assertEqual('05]', t3.upper)

        # test the expected equal real range of [04, 05] and (3, 6)
        self.assertEqual(t3.real_range(), t4.real_range())

        #test exceptions
        with self.assertRaises(EmptyInputError):
            interval('')
        with self.assertRaises(FormatError):
            interval('[9)')
        with self.assertRaises(FormatError):
            interval('88')
        with self.assertRaises(FormatError):
            interval('foo')
        with self.assertRaises(FormatError):
            interval('[3.5, 15]')
        with self.assertRaises(FormatError):
            interval(',,')
        with self.assertRaises(FormatError):
            interval('[foo,bar)')
        with self.assertRaises(FormatError):
            interval('[foo,100)')
        with self.assertRaises(FormatError):
            interval(')3, 4]')
        with self.assertRaises(FormatError):
            interval('(3, 4}')
        with self.assertRaises(InvalidIntervalError):
            interval('(88, 77]')


    def test_mergeIntervals(self):
        """
        Assuming have passed the test_interval test;
        This test function examines the mergeIntervals function
        from three aspects:
            1) adjacent merge
            2) overlapping merge
            3) merge exceptions
        """
        t1 = interval('(1, 8]')
        t2 = interval('[9, 19)')
        t3 = interval('[16, 26)')
        t4 = interval('(30, 166)')
        t5 = interval('[60, 100]')

        # test adjacent merge
        self.assertEqual('(1,19)', mergeIntervals(t1, t2))
        # test overlapping merge
        self.assertEqual('[9,26)', mergeIntervals(t2, t3))
        self.assertEqual('(30,166)', mergeIntervals(t4, t5))
        # test merge exceptions
        with self.assertRaises(NoOverlapError):
            mergeIntervals(t3, t4)
        with self.assertRaises(NoOverlapError):
            mergeIntervals(t5, t1)

    def test_mergeOverlapping(self):
        """
        Assuming have passed the above two tests;
        This test function examines the mergeOverlapping function
        from two aspects: adjacent and overlapping merge.
        """
        t1 = ['[1,3]', '[2,5)', '(7,11]', '[7,27]', '(27, 51)']
        t2 = ['(-899,-1)', '[-4,2]', '(4,9]', '[6,1111)', '[1111,1111]']
        t3 = ['(-899,-1)', '[6,11)', '(30, 50)']
        t4 = ['(-4,-1)', '[-2,2)', '(0, 3)', '[2,4]']

        # test adjacent and overlapping merge
        self.assertEqual(['[1,5)', '[7,51)'], mergeOverlapping(t1))
        self.assertEqual(['(-899,2]', '(4,1111]'], mergeOverlapping(t2))
        self.assertEqual(['(-899,1111]'], mergeOverlapping(t1+t2))
        self.assertEqual(['(-899,-1)', '[6,11)', '(30, 50)'], mergeOverlapping(t3))
        self.assertEqual(['(-4,4]'], mergeOverlapping(t4))


    def test_insert(self):
        """
        Assuming have passed the above three tests;
        This test function examines the insert function
        with overlapping and adjacent intervals.
        """

        # test adjacent and overlapping insert
        t0 = ['[1,3]', '[6,9]']
        self.assertEqual(['[1,9]'], insert(t0, '[2,5]'))

        t1 = ['[-20,-17]', '(-14,11]', '[13,16)', '(18,22)', '[25,53]']
        t2 = insert(t1, '[14,18]')
        self.assertEqual('[-20,-17], (-14,11], [13,22), [25,53]', ', '.join(t2))
        t3 = insert(t2, '[54,54]')
        self.assertEqual('[-20,-17], (-14,11], [13,22), [25,54]', ', '.join(t3))
        t4 = insert(t3, '[22,23)')
        self.assertEqual('[-20,-17], (-14,11], [13,23), [25,54]', ', '.join(t4))
        t5 = insert(t4, '(12,22)')
        self.assertEqual('[-20,-17], (-14,11], [13,23), [25,54]', ', '.join(t5))
        t6 = insert(t5, '[-17,-12]')
        self.assertEqual('[-20,11], [13,23), [25,54]', ', '.join(t6))
        t7 = insert(t6, '[-12,15]')
        self.assertEqual('[-20,23), [25,54]', ', '.join(t7))


if __name__ == "__main__":
    unittest.main()
