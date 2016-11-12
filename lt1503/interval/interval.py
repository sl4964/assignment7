import sys
import numpy as np


# I chose to have the interval class only input strings
# with no extra characters other than spaces, rather than parsing intelligently for
# divserse input typos. Also 3 3 is not treated as the number 33, it is treated as an error.
# I allow comparison between interval types by stating that x] should be less than x+1),
# which models float behavior to allow this class to be easily expanded to handle floats
def get_integer_if_possible(s):
    """get an integer from the input, or raise a value error if s does not represent an integer"""
    try: 
        return int(s)
    except:
        raise ValueError('%s is not an integer' % (s))

INCLUSIVE = 0
EXCLUSIVE = 1
MIN_CHARS = {INCLUSIVE : '[', EXCLUSIVE : '('}
MAX_CHARS = {INCLUSIVE : ']', EXCLUSIVE : ')'}


def remove_whitespace(s):
    return "".join(s.split())


class interval(object):
    """This is a class of intervals of integers"""
    def __init__(self, user_input):
        """A interval needs to have a lower bound and upper bound,
        where each bound contains a value and a bound type (inclusive or exclusive)"""
        self._lower_bound_value = -np.inf
        self._upper_bound_value = np.inf
        try:
            cleaned_input = user_input.strip()
            self.left_input,self.right_input = str.split(cleaned_input, ",")
        except:
            raise ValueError("cannot split %s with by one comma", (cleaned_input))
            sys.exit(0)
        self._set_bounds()

    def __eq__(self, other):
        """two intervals are equal if they have the same highest and smallest bound (value and type)"""
        if not isinstance(other, interval):
            return False
        return self.get_lowest_value() == other.get_lowest_value() and \
                self.get_highest_value() == other.get_highest_value()

    def __ne__(self, other):
        """two intervals are not equal if they have the same
        highest and smallest bound (value and type)"""
        if not isinstance(other, interval):
            return True
        return not (self.get_lowest_value() == other.get_lowest_value() and \
                self.get_highest_value() == other.get_highest_value())
    
    def __repr__(self):
        """An interval is represented by the input string that would create it"""
        rep_str = MIN_CHARS[self.lower_bound_type] + str(self.lower_bound_value) + ',' + \
                            str(self.upper_bound_value) + MAX_CHARS[self.upper_bound_type]
        return rep_str
        
    def _set_bounds(self):
        """Set the bounds of an interval"""
        self._set_bound_type()
        self._set_lower_bound()
        self._set_upper_bound()
        
    def _set_bound_type(self):
        """Set the bound types of an interval"""
        self.lower_bound_type = self._get_bound_type(
                self.left_input[0],MIN_CHARS[EXCLUSIVE], MIN_CHARS[INCLUSIVE])
        self.upper_bound_type = self._get_bound_type(
                self.right_input[-1], MAX_CHARS[EXCLUSIVE], MAX_CHARS[INCLUSIVE])
        
    
    def _get_bound_type(self, bound_char, exclusive_char, inclusive_char):
        """Get the bound type from the input bound characters"""
        if bound_char == exclusive_char:
            return EXCLUSIVE
        elif bound_char == inclusive_char:
            return INCLUSIVE
        else:
            raise ValueError('not a correct bound variable: %s' % (bound_char))
        
    def _set_lower_bound(self):
        try:
            self.lower_bound_value = get_integer_if_possible(self.left_input[1:])
        except ValueError:
            raise ValueError("give me an integer for lower bound")
    
    def _set_upper_bound(self):
        try:
            self.upper_bound_value = get_integer_if_possible(self.right_input[:-1])
        except ValueError:
            raise ValueError("give me an integer for upper bound")
            
    def get_lowest_value(self):
        """Smallest integer in the interval"""
        return self.lower_bound_value + self.lower_bound_type
    
    def get_highest_value(self):
        """Largeset integer in the interval"""
        return self.upper_bound_value - self.upper_bound_type
    
    def get_approximate_lowest_value(self):
        """Smallest value in the interval. Not exact, to allow for (0 to be smaller than [1
        as if intervals were expanded to floats"""
        return self.lower_bound_value + self.lower_bound_type * 0.5
    
    def get_approximate_highest_value(self):
        """Largest value in the interval. Not exact, to allow for 4) to be larger than 3]
        as if intervals were expanded to floats"""
        return self.upper_bound_value - self.upper_bound_type * 0.5
    
    @property
    def lower_bound_value(self):
        return self._lower_bound_value
    
    @lower_bound_value.setter
    def lower_bound_value(self, lower_bound_value):
        buffer = self.lower_bound_type + self.upper_bound_type
        if lower_bound_value <= self.upper_bound_value - buffer:
            self._lower_bound_value = lower_bound_value
        else:
            raise ValueError("lower bound ' %c ' is not low enough" % (lower_bound_value))
    
    @property
    def upper_bound_value(self):
        return self._upper_bound_value
    
    @upper_bound_value.setter
    def upper_bound_value(self, upper_bound_value):
        buffer = self.lower_bound_type + self.upper_bound_type
        if upper_bound_value >= self.lower_bound_value + buffer:
            self._upper_bound_value = upper_bound_value
        else:
            raise ValueError("upper bound ' %s ' is not high enough" % str(upper_bound_value))
            
        

def no_space_intervals(left_interval, right_interval):
    """if the two inputs are intervals check if they are mergeable or not"""
    if not isinstance(left_interval, interval):
        raise ValueError("can only handle intervals, not %s" % (type(left_interval)))
    if not isinstance(right_interval, interval):
        raise ValueError("can only handle intervals, not %s" % (type(right_interval)))
    return right_interval.get_lowest_value() <= left_interval.get_highest_value() + 1 and \
           right_interval.get_highest_value() >= left_interval.get_highest_value() - 1

def mergeIntervals(left_interval, right_interval):
    """attempt to merge the two intervals. Should only be called if intervals are mergeable.
    If intervals are not mergeable, then this should raise a ValueError"""
    if no_space_intervals(left_interval, right_interval):
        new_interval = interval(left_interval.__repr__())
        if right_interval.get_approximate_lowest_value() < left_interval.get_approximate_lowest_value():
            new_interval.lower_bound_type = right_interval.lower_bound_type
            new_interval.lower_bound_value = right_interval.lower_bound_value
        if right_interval.get_approximate_highest_value() > left_interval.get_approximate_highest_value():
            new_interval.upper_bound_type = right_interval.upper_bound_type
            new_interval.upper_bound_value = right_interval.upper_bound_value
        return new_interval
    else:
        raise ValueError("intervals have a gap, cant merge intervals")

def iteratively_merge_sorted(intervals):
    """merge the input list of sorted intervals into as few intervals as possible"""
    mergedIntervals = []
    activeInterval = intervals[0]
    
    for next_interval in intervals[1:]:
        if no_space_intervals(activeInterval, next_interval):
            # Iterate through the intervals by their lower bound, merging if possible
            activeInterval = mergeIntervals(activeInterval, next_interval)
        else:
            # If a merge is not possible, start over
            # with the larger interval as the new activeInterval
            mergedIntervals.append(activeInterval)
            activeInterval = next_interval
            
    mergedIntervals.append(activeInterval)
    return mergedIntervals

def mergeOverlapping(intervals):
    """Sort, then merge the input list of intervals into the
    smallest list of intervals that can represent them"""
    if not isinstance(intervals, list):
        raise ValueError("mergeOverlapping only accepts lists. Received %s" % (type(intervals)))
    if len(intervals) == 0:
        return []
    try:
        intervals.sort(key=lambda x:x.get_approximate_lowest_value())
    except AttributeError:
        raise ValueError("merge Overlapping values list elements should be intervals")
    
    mergedIntervals = iteratively_merge_sorted(intervals)
        
    return mergedIntervals
    

def insert(intervals, new_interval):
    """return a new list of intervals from a list of intervals and one new interval"""
    if not isinstance(intervals, list):
        raise ValueError("insert only accepts lists as first argument. Received %s" % (type(intervals)))
    if not isinstance(new_interval, interval):
        raise ValueError("insert only accepts intervals as second argument. Received %s" % (type(new_interval)))
    return mergeOverlapping(intervals + [new_interval])
        


def get_interval_list(user_input):
    """get list of intervals from string of intervals, or raise a ValueError"""
    if not isinstance(user_input, str):
        raise ValueError("get_interval_list only takes in strings. Received %s" % (type(user_input)))
    cleaned_input = user_input.strip()
    intervals = []
    split_intervals = str.split(cleaned_input, ',')

    # The user_input interval list must be split by commas between intervals.
    # However, each interval also contains a comma.
    # Therefore, we split by intervals by commas and enforce that there should be an even number
    # of resulting sections. If there is an even number of resulting splits, we should be able to merge
    # every other section and get an appropriately structured interval out of the ','.join() output.
    # Otherwise, interval(single_interval) will raise a ValueError if the input from the user was not
    # correctly structured.
    if len(split_intervals) % 2 != 0:
        raise ValueError("Input data formatted wrong %s" % (cleaned_input))
    for idx in range(0, len(split_intervals), 2):
        single_interval = ",".join([split_intervals[idx].strip(),split_intervals[idx+1].strip()])
        # Raises a ValueError if single_interval is not correctly structured as an interval
        intervals.append(interval(single_interval))
    return mergeOverlapping(intervals)
        


