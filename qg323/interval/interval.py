
import re

class interval(object):
    def __init__(self, left, right):
        '''
        Parameters
        ----------
        left, right : int
            Left-end and right-end values.  left should be always smaller
            than right.
        '''
        if left > right:
            raise ValueError("left value bigger than right")
        self._left = left
        self._right = right

    def __repr__(self):
        return 'interval(%d, %d)' % (self._left, self._right)

    def __str__(self):
        return '[%d, %d]' % (self._left, self._right)

    @classmethod
    def fromString(cls, s):
        '''
        Parse a string representation of an interval.
        Ignores all leading and trailing whitespaces.
        Does not allow empty intervals (i.e. left > right).
        Does not allow empty string as input.

        Examples
        --------
        >>> interval.fromString('[5,9)')
        interval(5, 8)
        '''
        s = s.strip()
        if s == '':
            raise ValueError("empty string not allowed")

        if s[0] == '(':
            left_open = True
        elif s[0] == '[':
            left_open = False
        else:
            raise ValueError("invalid left-end specification")

        try:
            comma_index = s.index(',')
        except ValueError:
            raise ValueError("missing comma")

        # int() throws exception with clear message
        left_value = int(s[1:comma_index])
        right_value = int(s[comma_index+1:-1])

        if s[-1] == ')':
            right_open = True
        elif s[-1] == ']':
            right_open = False
        else:
            raise ValueError("invalid right-end specification")

        return interval(
                (left_value + 1) if left_open else left_value,
                (right_value - 1) if right_open else right_value
                )

    def __or__(self, value):
        return mergeIntervals(self, value)

    def __eq__(self, value):
        return (self._left == value._left) and (self._right == value._right)

    def __ne__(self, value):
        return (self._left != value._left) or (self._right != value._right)


def _sortTwo(int1, int2):
    '''
    Sorts two intervals according to left-end value in ascending order.

    Parameters
    ----------
    int1, int2 : interval

    Returns
    -------
    int_left, int_right : interval
        The left-end value of int_left is smaller or equal to that of
        int_right.

    Notes
    -----
    This function does not care about right-end values, so they can appear
    in any order.
    '''
    if int1._left < int2._left:
        int_left = int1
        int_right = int2
    else:
        int_left = int2
        int_right = int1
    return int_left, int_right


def overlapOrAdjacent(int1, int2):
    '''
    Determines if two intervals overlap or are adjacent to each other.

    Parameters
    ----------
    int1, int2 : interval

    Returns
    -------
    overlapOrAdjacent : bool
    '''
    int_left, int_right = _sortTwo(int1, int2)
    if int_left._right < int_right._left - 1:
        return False
    else:
        return True


def mergeIntervals(int1, int2):
    '''
    Merges two intervals if they overlap or are adjacent, or throws an
    exception otherwise.

    Parameters
    ----------
    int1, int2 : interval

    Returns
    -------
    merged : interval

    Throws
    ------
    ValueError
        if int1 and int2 are not adjacent or don't overlap.
    '''
    if not overlapOrAdjacent(int1, int2):
        raise ValueError('intervals are not overlapping or adjacent')
    return interval(
            min(int1._left, int2._left),
            max(int1._right, int2._right)
            )


def mergeOverlapping(intervals):
    '''
    Merges all the possible intervals in the given list, and returns
    a list of disjoint intervals.
    Empty list is allowed, and an empty list is returned in this case.

    Parameters
    ----------
    intervals : list or any iterable of interval

    Returns
    -------
    merged : list of interval
    '''
    # Handle empty list separately
    if len(intervals) == 0:
        return []

    intervals = sorted(intervals, key=lambda x: x._left)
    merged = [intervals[0]]
    # Merge intervals one by one: for each interval, check if it can be
    # merged to the last interval in the @merged list.  Replace the last
    # interval with the merged one if so, or append current interval
    # to the list otherwise.
    for i in range(1, len(intervals)):
        if overlapOrAdjacent(merged[-1], intervals[i]):
            merged[-1] = mergeIntervals(merged[-1], intervals[i])
        else:
            merged.append(intervals[i])
    return merged


def insert(intervals, newint):
    '''
    Insert and merge an interval @newint into a list of intervals given in
    @intervals, and returns a list of disjoint intervals.

    This is just a wrapper of mergeOverlapping(), and @intervals does not
    need to be disjoint.

    Parameters
    ----------
    intervals : list or any iterable of interval
    newint : interval

    Returns
    -------
    merged : list of interval
    '''
    return mergeOverlapping(intervals + [newint])
