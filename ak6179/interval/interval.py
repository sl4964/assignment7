from . import interval_utils


class Interval(object):
    """Interval class for integers"""

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
        Checks whether the string input of the interval is a valid represetation or not.
        """
        clean_string = interval_utils.get_clean_string(interval_string)
        self._validate_interval_string(clean_string)
        self._create_interval(clean_string)


def intervals_overlap(int1, int2):
    left1, right1 = int1.get_limits()
    left2, right2 = int2.get_limits()
    if left1 <= right2 and left2 <= right1:
        return True
    else:
        return False


def intervals_adjacent(int1, int2):
    left1, right1 = int1.get_limits()
    left2, right2 = int2.get_limits()
    if (not intervals_overlap(int1, int2)) and (left1 == right2 + 1 or left2 == right1 + 1):
        return True
    else:
        return False


def merge_intervals(int1, int2):
    # TODO: split this method into more functions
    # TODO: check if int1 and int2 are intervals
    if intervals_overlap(int1, int2) or intervals_adjacent(int1, int2):
        left1, right1 = int1.get_limits()
        left2, right2 = int2.get_limits()
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
    # TODO: check if intervals is a list of intervals
    initial_size = len(intervals)
    if initial_size == 0:
        return intervals
    temp_list = sorted(intervals)
    new_list = list()
    new_list.append(temp_list[0])
    for it in temp_list[1:]:
        prev_interval = new_list[-1]
        if intervals_overlap(prev_interval, it) or intervals_adjacent(prev_interval, it):
            new_interval = merge_intervals(prev_interval, it)
            new_list[-1] = new_interval
        else:
            new_list.append(it)
    new_size = len(new_list)
    if new_size < initial_size:
        return merge_overlapping(new_list)
    else:
        return new_list


def insert(intervals, newint):
    # TODO: check if intervals is a list of intervals and newint is an interval
    new_intervals = list(intervals)
    new_intervals.append(newint)
    return merge_overlapping(new_intervals)


def get_intervals_list(input_string):
    # TODO: make this function more robust to handle the comma separator properly
    intervals_list = [Interval(interval_string) for interval_string in input_string.split(", ")]
    return intervals_list
