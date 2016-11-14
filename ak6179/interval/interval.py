from . import interval_utils


class Interval(object):
    """Interval class for integers
    Throws exception in the constructor if the interval string input is invalid.
    """

    @property
    def opening_bracket(self):
        return self._opening_bracket

    @property
    def closing_bracket(self):
        return self._closing_bracket

    @property
    def opening_limit(self):
        return self._opening_limit

    @property
    def closing_limit(self):
        return self._closing_limit

    @staticmethod
    def _validate_interval_string(s):
        """Checks whether the interval string is a valid interval."""
        interval_utils.check_brackets(s)
        interval_utils.check_interval_limits(s)

    def _set_interval_brackets(self, s):
        self._opening_bracket = s[0]
        self._closing_bracket = s[-1]

    def _set_interval_limit(self, s):
        limits = s[1:-1].split(",")
        self._opening_limit = int(limits[0])
        self._closing_limit = int(limits[-1])

    def _create_interval(self, s):
        self._set_interval_brackets(s)
        self._set_interval_limit(s)

    def get_limits(self):
        """Returns the limits of the interval.
        This method adjusts for the fact that whether the
        interval is an opening interval or a closing interval.
        """
        left = self.opening_limit
        if self.opening_bracket == "(":
            left += 1
        right = self.closing_limit
        if self.closing_bracket == ")":
            right -= 1
        return left, right

    def __lt__(self, other):
        tuple1 = self.get_limits()
        tuple2 = other.get_limits()
        return tuple1 < tuple2

    def __repr__(self):
        return self.opening_bracket + str(self.opening_limit) + "," + str(self.closing_limit) + str(
            self.closing_bracket)

    def __init__(self, interval_string):
        """Constructor for creating Interval from a string.
        Checks whether the string input of the interval is a valid representation or not.
        Creates an interval object if the input interval string is a valid representation.
        """
        clean_string = interval_utils.get_clean_string(interval_string)
        self._validate_interval_string(clean_string)
        self._create_interval(clean_string)


def intervals_overlap(int1, int2):
    """Checks whether two intervals are overlapping.
    Note that this function returns False if the intervals are
    only adjacent.
    """
    left1, right1 = int1.get_limits()
    left2, right2 = int2.get_limits()
    if left1 <= right2 and left2 <= right1:
        return True
    else:
        return False


def intervals_adjacent(int1, int2):
    """Checks whether two intervals are adjacent or not."""
    left1, right1 = int1.get_limits()
    left2, right2 = int2.get_limits()
    if (not intervals_overlap(int1, int2)) and (left1 == right2 + 1 or left2 == right1 + 1):
        return True
    else:
        return False


def merge_intervals(int1, int2):
    """Merges two overlapping or adjacent intervals. Throws
    an exception if the intervals are non-overlapping or non-adjacent.
    """
    if intervals_overlap(int1, int2) or intervals_adjacent(int1, int2):
        left1, right1 = int1.get_limits()
        left2, right2 = int2.get_limits()
        # Setting the limits of new merged interval
        if left1 <= left2:
            opening_bracket = int1.opening_bracket
            opening_limit = int1.opening_limit
        else:
            opening_bracket = int2.opening_bracket
            opening_limit = int2.opening_limit
        if right1 >= right2:
            closing_bracket = int1.closing_bracket
            closing_limit = int1.closing_limit
        else:
            closing_bracket = int2.closing_bracket
            closing_limit = int2.closing_limit
        return Interval(opening_bracket + str(opening_limit) + "," + str(closing_limit) + closing_bracket)
    else:
        raise Exception(
            "The intervals %s and %s cannot be merged. Only adjacent or overlapping intervals can be merged." % (str(
                int1), str(int2)))


def merge_overlapping(intervals):
    """Takes input a list of intervals and keeps on merging the intervals
    until intervals can no longer be merged. Always returns a sorted list
    of intervals.
    """
    if len(intervals) == 0:
        return intervals
    # Sort the intervals.
    temp_list = sorted(intervals)
    new_list = list()
    new_list.append(temp_list[0])
    for it in temp_list[1:]:
        prev_interval = new_list[-1]
        # Check if it interval can be merged with the last interval in the sorted list.
        if intervals_overlap(prev_interval, it) or intervals_adjacent(prev_interval, it):
            # Merge the intervals
            new_interval = merge_intervals(prev_interval, it)
            # Update the last interval in the list.
            new_list[-1] = new_interval
        else:
            # it interval can't be merged with the prev_interval hence insert it into the list.
            new_list.append(it)
    return new_list


def insert(intervals, newint):
    """Insert an interval into a list of intervals.
    Returns the sorted list of intervals after insertion.
    """
    new_intervals = list(intervals)
    new_intervals.append(newint)
    return merge_overlapping(new_intervals)


def get_intervals_list(input_string, sep=", "):
    """Retuns a list of intervals after splitting the input string by sep.
    Assumes that the left and right limit of interval are separated by ','.
    If the separator given is ',' this function raises an exception because
    the limit of the intervals have an ambiguous interpretation.
    """
    if sep == ",":
        raise ValueError("Please use a separator other than ',' for separating the elements of the list")
    intervals_list = [Interval(interval_string) for interval_string in input_string.split(sep)]
    return intervals_list
