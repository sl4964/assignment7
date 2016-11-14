'''
Created on Nov 14, 2016

@author: Yovela
'''


class interval(object):
    '''
    This class has a constructor that takes a string representation of the interval
    And represents the range of integers between a lower bound and an upper bound
    '''

    def __init__(self, input_range):

        try:
            # read a string and format it
            self.lowerbound = input_range[0]
            self.upperbound = input_range[-1]
            self.begin = int(input_range[1:-1].split(",")[0])
            self.end = int(input_range[1:-1].split(",")[1])

        except:
            raise InputError

        # decide range of integers based on type of boundaries
        if input_range[0] == "(" and input_range[-1] == ")":
            if self.begin < self.end - 1:
                self.represent = list(range(self.begin + 1, self.end))
            else:
                raise InputError

        elif input_range[0] == "[" and input_range[-1] == ")":
            if self.begin < self.end:
                self.represent = list(range(self.begin, self.end))
            else:
                raise InputError

        elif input_range[0] == "(" and input_range[-1] == "]":
            if self.begin < self.end:
                self.represent = list(range(self.begin + 1, self.end + 1))
            else:
                raise InputError


        elif input_range[0] == "[" and input_range[-1] == "]":
            if self.begin <= self.end:
                self.represent = list(range(self.begin, self.end + 1))
            else:
                raise InputError

    def __repr__(self):
        return '%s%d%s%d%s' % (self.lowerbound, self.begin, ',', self.end, self.upperbound)


class InputError(Exception):
    # Exception raised for invalid input
    def __str__(self):
        return "Invalid Interval\n"


class MergedError(Exception):
    # Exception raised for errors when merging two intervals
    pass


def mergeIntervals(int1, int2):
    '''
    This function takes two intervals.
    If the intervals overlap or are adjacent, returns a merged interval.
    If the intervals cannot be merged, raise an error.

    '''
    if not isinstance(int1, interval):
        raise InputError
    if not isinstance(int2, interval):
        raise InputError

    if int1.represent[0] <= int2.represent[0]:
        starter = int1
        ender = int2
    else:
        starter = int2
        ender = int1

    if starter.represent[-1] >= (ender.represent[0] - 1):

        first_num = min(starter.begin, starter.begin)
        last_num = max(starter.end, ender.end)

        if first_num in starter.represent or first_num in ender.represent:
            lowerbound = "["
        else:
            lowerbound = "("

        if last_num in starter.represent or last_num in ender.represent:
            upperbound = "]"
        else:
            upperbound = ")"
        merged_str = lowerbound + str(first_num) + "," + str(last_num) + upperbound
        merged_interval = interval(merged_str)

    else:
        raise MergedError

    return merged_interval


def mergeOverlapping(intervals):
    '''
     This function takes a list of intervals and merges all overlapping or adjacent intervals.
    '''

    sorted_intervals = sorted(intervals, key=lambda interval: interval.represent[0])
    new_intervals = []
    temp = intervals[0]

    for i in range(0, len(sorted_intervals)):
        try:
            temp = mergeIntervals(temp, sorted_intervals[i])
        except:
            new_intervals.append(temp)
            temp = sorted_intervals[i]
    new_intervals.append(temp)
    sorted_new_intervals = sorted(new_intervals, key=lambda new_interval: new_interval.represent[0])

    return sorted_new_intervals


def insert(intervals, newint):
    '''
    This function takes two arguments: a list of non-overlapping intervals: and a single interval.
    The function should insert this single interval into intervals, merging the result if necessary.
    Assumed that the intervals in this list were initially sorted according to their lower bounds.
    Returned a interval list sorted according to their lower bounds.

    '''

    if not isinstance(newint, interval):
        raise TypeError('bad operand type, please input an interval')

    sorted_intervals = sorted(intervals, key=lambda interval: interval.represent[0])

    new_intervals = []

    inserted_interval = newint

    for i in range(0, len(sorted_intervals)):
        try:
            inserted_interval = mergeIntervals(intervals[i], inserted_interval)
            new_intervals.append(inserted_interval)

        except:
            new_intervals.append(intervals[i])

    merged_interval = mergeOverlapping(new_intervals)

    return merged_interval