import unittest
from interval.interval import *

#The following are test cases to ensure correct functionality of intervals
class MyTest(unittest.TestCase):
    """unit tests for functions relating to the interval class
    These should be run by enterring the command "python -m unittest discover"
    from the root directory of this project
    """
    def test_interval(self):
        """unit tests for the interval constructor"""

        # test expected behavior for correctly formatted inputs
        int1 = interval('[1,2)')
        self.assertEqual('[1,2)', str(int1))
        intneg1 = interval('[-1,0)')
        self.assertEqual('[-1,0)', str(intneg1))
        int1strict = interval('[1,1]')
        # check that [1, 2) is equal to [1,1]
        self.assertEqual(int1, int1strict)
        self.assertEqual('[1,2)', str(int1))
        int2 = interval('(1,2]')
        self.assertEqual('(1,2]', str(int2))
        int3 = interval('[3,3]')
        self.assertEqual('[3,3]', str(int3))
        int13 = interval('[1,3]')
        self.assertEqual('[1,3]', str(int13))
        intwithspaces = interval('       [ 1  , 2  )  ')
        self.assertEqual('[1,2)', str(intwithspaces))

        # test expected behavior for incorrectly formatted inputs
        with self.assertRaises(ValueError):
            int1 = interval('[1, a)')
        with self.assertRaises(ValueError):
            int1 = interval('d1, 2)')
        with self.assertRaises(ValueError):
            int1 = interval(' 1, 2)')
        with self.assertRaises(ValueError):
            int1 = interval('[1, [2)')
        with self.assertRaises(ValueError):
            int1 = interval('')
        with self.assertRaises(ValueError):
            int1 = interval('[]')
        with self.assertRaises(ValueError):
            int1 = interval('[1 2]')
        with self.assertRaises(ValueError):
            int1 = interval('[1,2(')
        with self.assertRaises(ValueError):
            int1 = interval('[3,3)')
        with self.assertRaises(ValueError):
            int1 = interval('(3,3]')
        with self.assertRaises(ValueError):
            int1 = interval('(3,3 3]')
        print("interval constructor test complete")

    def test_mergeIntervals(self):
        """unit tests for the mergeIntervals function"""

        # test expected behavior for correctly formatted inputs
        int1 = interval('[1,2)')
        int2 = interval('(1,2]')
        int12 = interval('[1,2]')
        merged12 = mergeIntervals(int1, int2)
        self.assertEqual(int12, merged12)
        int3 = interval('[3,3]')
        int13 = interval('[1,3]')
        self.assertEqual(int13, mergeIntervals(int12, int3))
        int4 = interval('(3,4]')
        int58 = interval('[5,8]')

        # test expected behavior for incorrectly formatted inputs
        with self.assertRaises(ValueError):
            int1 = mergeIntervals(int1, int4)
        with self.assertRaises(ValueError):
            int1 = mergeIntervals(int4, int1)
        with self.assertRaises(ValueError):
            int1 = mergeIntervals(int3, int1)
        with self.assertRaises(ValueError):
            int1 = mergeIntervals(int3, int58)
        with self.assertRaises(ValueError):
            int1 = mergeIntervals(int1, 4)
        with self.assertRaises(ValueError):
            int1 = mergeIntervals(3, int1)
        with self.assertRaises(ValueError):
            int1 = mergeIntervals(3, "not an interval")
        with self.assertRaises(ValueError):
            int1 = mergeIntervals(3, "[1,3]")
        with self.assertRaises(ValueError):
            int1 = mergeIntervals([], "")
        with self.assertRaises(ValueError):
            int1 = mergeIntervals([12, "hi"], "interval")
        with self.assertRaises(ValueError):
            int1 = mergeIntervals(int1, "")
        with self.assertRaises(ValueError):
            int1 = mergeIntervals([], int2)
        print("merge test complete")



    def test_mergeOverlapping(self):
        """unit tests for the mergeOverlapping function"""

        # test expected behavior for correctly formatted inputs
        int1 = interval('[1,2)')
        int2 = interval('(1,2]')
        int12 = interval('[1,2]')
        merged12 = mergeOverlapping([int1, int2])
        self.assertEqual([int12], merged12)
        int3 = interval('[3,3]')
        int13 = interval('[1,3]')
        intneg1 = interval('[-1,0)')
        int0 = interval('[0,1)')
        intneg13 = interval('[-1,3]')
        self.assertEqual([intneg13], mergeOverlapping([intneg1, int0, int13]))
        self.assertEqual([intneg1, int3], mergeOverlapping([intneg1, int3]))
        self.assertEqual([int13], mergeOverlapping([int12, int3]))
        int4 = interval('(3,4]')
        int58 = interval('[5,8]')
        intnothing = mergeOverlapping([])
        self.assertEqual([], intnothing)
        self.assertEqual([int13, int58], mergeOverlapping([int12, int3, int58]))
        self.assertEqual([int13, int58], mergeOverlapping([int58, int13]))
        self.assertEqual([int13], mergeOverlapping([int1, int2, int3]))
        self.assertEqual([int13], mergeOverlapping([int1, int2, int2, int3, int12]))
        self.assertEqual([int1], mergeOverlapping([int1]))

        # test expected behavior for incorrectly formatted inputs
        with self.assertRaises(ValueError):
            int1 = mergeOverlapping([int1, 4])
        with self.assertRaises(ValueError):
            int1 = mergeOverlapping([3, int1])
        with self.assertRaises(ValueError):
            int1 = mergeOverlapping([3, "not an interval"])
        with self.assertRaises(ValueError):
            int1 = mergeOverlapping([3, "[1,3]"])
        with self.assertRaises(ValueError):
            int1 = mergeOverlapping([[], ""])
        with self.assertRaises(ValueError):
            int1 = mergeOverlapping([[12, "hi"], "interval"])
        with self.assertRaises(ValueError):
            int1 = mergeOverlapping([int1, ""])
        with self.assertRaises(ValueError):
            int1 = mergeOverlapping([[], int2])
        print("merge overlapping list test complete")


    def test_insert(self):
        """unit tests for the insert function"""

        # test expected behavior for correctly formatted inputs
        int1 = interval('[1,2)')
        int2 = interval('(1,2]')
        int12 = interval('[1,2]')
        inserted12 = insert([int1], int2)
        self.assertEqual([int12], inserted12)
        int3 = interval('[3,3]')
        int13 = interval('[1,3]')
        self.assertEqual([int13], insert([int12], int3))
        int4 = interval('(3,4]')
        int58 = interval('[5,8]')
        inserted4 = insert([],int4)
        self.assertEqual([int4], inserted4)
        self.assertEqual([int13, int58], insert([int12, int3], int58))
        self.assertEqual([int13, int58], insert([int58], int13))
        self.assertEqual([int13], insert([int2, int3], int1))
        self.assertEqual([int13], insert([int1, int2, int2, int3], int12))
        self.assertEqual([int1], insert([int1], int1))

        # test expected behavior for incorrectly formatted inputs
        with self.assertRaises(ValueError):
            int1 = insert([int1], 4)
        with self.assertRaises(ValueError):
            int1 = insert([3], int1)
        with self.assertRaises(ValueError):
            int1 = insert([3], "not an interval")
        with self.assertRaises(ValueError):
            int1 = insert([3], "[1,3]")
        with self.assertRaises(ValueError):
            int1 = insert([[]], "")
        with self.assertRaises(ValueError):
            int1 = insert([[12, "hi"]], "interval")
        with self.assertRaises(ValueError):
            int1 = insert([int1], "")
        with self.assertRaises(ValueError):
            int1 = insert([[]], int2)
        print("insert test complete")

    def test_get_interval_list(self):
        """unit tests for the get_interval_list function"""

        # test expected behavior for correctly formatted inputs
        int12 = interval('[1,2]')
        processed12 = get_interval_list('[1, 2), (1, 2]')
        self.assertEqual([int12], processed12)
        int3 = get_interval_list('[3,3]')[0]
        int13 = get_interval_list('[1,3]')[0]
        intneg1 = get_interval_list('[-1,0)')[0]
        intneg13 = get_interval_list('[-1,3]')[0]
        self.assertEqual([intneg13], get_interval_list("[-1, 2], [1, 3]"))
        self.assertEqual([intneg1, int3], get_interval_list("[-1, -1], [3, 3]"))
        self.assertEqual([int13], get_interval_list("[2, 3], [1,2]"))
        int4 = interval('(3,4]')
        int58 = interval('[5,8]')

        # test expected behavior for incorrectly formatted inputs
        with self.assertRaises(ValueError):
            int1 = get_interval_list("")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("[]")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("[1, 5a]")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("[,]")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("5,3")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("[5, 4 4]")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("[4 5, 4 4]")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("[4,,5]")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("(4, 2[")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("[[1,2], [3, 4]")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("[4, 5], [")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("[1 2]")
        with self.assertRaises(ValueError):
            int1 = get_interval_list("]]")
        print("get inteval list from user complete")
