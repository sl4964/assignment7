
import re

class interval(object):
    def __init__(self, left, right):
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
        Does not allow empty intervals (i.e. left > right)
        '''
        s = s.strip()
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
    if int1._left < int2._left:
        int_left = int1
        int_right = int2
    else:
        int_left = int2
        int_right = int1
    return int_left, int_right


def overlapOrAdjacent(int1, int2):
    int_left, int_right = _sortTwo(int1, int2)
    if int_left._right < int_right._left - 1:
        return False
    else:
        return True


def mergeIntervals(int1, int2):
    if not overlapOrAdjacent(int1, int2):
        raise ValueError('intervals are not overlapping or adjacent')
    return interval(
            min(int1._left, int2._left),
            max(int1._right, int2._right)
            )


def mergeOverlapping(intervals):
    # Handle empty list separately
    if len(intervals) == 0:
        return []

    intervals = sorted(intervals, key=lambda x: x._left)
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if overlapOrAdjacent(merged[-1], intervals[i]):
            merged[-1] = mergeIntervals(merged[-1], intervals[i])
        else:
            merged.append(intervals[i])
    return merged


def insert(intervals, newint):
    return mergeOverlapping(intervals + [newint])
