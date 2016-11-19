# This is the interval class to represent the range of integers between a lower bound and an upper bound.
class interval(object):

    def __init__(self, interval):
        """
        This is the constructor of the interval. If we create a new class instance, the __init__() will be
        automatically invoked.
        """
        self.interval = interval

        if self.interval == '' or self.interval == ' ':
            raise ValueError('Invalid interval. (empty string)')

        if ',' not in self.interval:
            raise ValueError('Invalid interval. (missing comma)')

        self.interval_to_list = interval.split(',')

        try:
            self.lower_symbol = self.interval_to_list[0][0]
            self.upper_symbol = self.interval_to_list[1][-1]
            self.lower_number = int(self.interval_to_list[0][1:])
            self.upper_number = int(self.interval_to_list[1][0: -1])
        except:
            raise ValueError('Invalid interval. (not an interval)')

        if self.lower_symbol == '(':
            self.lower_number = self.lower_number + 1

        if self.upper_symbol == ')':
            self.upper_number = self.upper_number - 1

        if self.lower_number > self.upper_number:
            raise ValueError('Invalid interval. (lower bound > upper bound)')

    def __eq__(self, other):
        """
        If defines the equality of two intervals.
        """
        if self.interval != other.interval:
            return False
        if self.interval_to_list != other.interval_to_list:
            return False
        if self.upper_number != other.upper_number:
            return False
        if self.lower_number != other.lower_number:
            return False
        if self.upper_symbol != other.upper_symbol:
            return False
        if self.lower_symbol != other.lower_symbol:
            return False
        return True

    def __repr__(self):
        """
        It defines the way an interval is represented.
        """
        return self.interval

def mergeIntervals(int1, int2):
    """
    This function takes two intervals as arguments.
    If the intervals overlap or are adjacent, it returns a merged interval. Otherwise, it throws an error.
    """
    intervals_to_list = [int1, int2]
    intervals_to_list.sort(key=lambda x: x.lower_number) # sort the two intervals according to their lower bounds
    interval1, interval2 = intervals_to_list[0], intervals_to_list[1]

    merge = False

    if interval1.upper_number + 1 == interval2.lower_number or \
                            interval1.lower_number <= interval2.lower_number <= interval1.upper_number:
        merge = True

    if merge == True:
        new_upper_number = max(interval1.upper_number, interval2.upper_number)
        new_lower_number, new_lower_symbol = interval1.interval_to_list[0][1:], interval1.lower_symbol

        if new_upper_number == interval1.upper_number:
            new_upper_number, new_upper_symbol = interval1.interval_to_list[1][0: -1], interval1.upper_symbol
        if new_upper_number == interval2.upper_number:
            new_upper_number, new_upper_symbol = interval2.interval_to_list[1][0: -1], interval2.upper_symbol

        new_int = new_lower_symbol + str(new_lower_number) + ',' + str(new_upper_number) + new_upper_symbol
        return interval(new_int)

    else:
        raise UnboundLocalError

def mergeOverlapping(intervals):
    """
    This function takes a list of intervals as its argument, merges all overlapping or adjacent intervals,
    and finally returns a list of intervals sorted according to their lower bounds.
    """
    intervals.sort(key=lambda x: x.lower_number)
    i = 0
    new_intervals = [intervals[0]]

    while True:
        try:
            merge_outcome = mergeIntervals(new_intervals[-1], intervals[i])
            new_intervals[-1] = merge_outcome
        except UnboundLocalError:
            new_intervals.append(intervals[i])
        i += 1
        if i == len(intervals):
            break

    return new_intervals

def insert(intervals, newint):
    """
    This function takes a list of non-overlapping intervals and a single interval as its arguments.
    It inserts the single interval into the list of intervals and merge overlapping/adjacent intervals if necessary.
    Finally, it returns a list of new non-overlapping intervals sorted according to their lower bounds.
    """
    intervals.append(newint)
    return mergeOverlapping(intervals)