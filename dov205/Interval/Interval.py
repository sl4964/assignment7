import re
from typing import List, Any


class IntervalError(Exception):
    """Base Interval exception class."""
    pass


class ParsingException(IntervalError):
    """Raised when unable to parse user-defined Interval."""
    def __init__(self, interval):
        self.interval = interval

    def __str__(self):
        return "Interval '{}' was improperly parsed -- " \
               "make sure it's of the form [int, int], e.g. (0, 10), [1, 12), (1, 3]".format(self.interval)


class GroupingException(IntervalError):
    """Raised when either of user-defined Interval's grouping symbols are invalid."""
    def __init__(self, opening, closing):
        self.opening = opening
        self.closing = closing

    def __str__(self):
        return "Invalid Interval grouping in one of '{}' or '{}' -- " \
               "make sure they're both one of '[', ']', '(', ')'.".format(self.opening, self.closing)


class RangeException(IntervalError):
    """Raised when user's grouping and range values are not allowed."""
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __str__(self):
        return "Interval has invalid range: from {} to {} -- " \
               "make sure your interval goes from low to high.".format(self.lower, self.upper)


class RangeMismatchException(RangeException):
    """Raised when user-defined Interval's lower and upper values are not allowed."""
    def __str__(self):
        return "Interval has invalid range -- {} (left) cannot " \
               "be greater than than {} (right).".format(self.lower, self.upper)


class DisjointIntervalException(IntervalError):
    """Raised when two Interval objects cannot be merged."""
    def __init__(self, interval_1, interval_2):
        self.interval_1 = interval_1
        self.interval_2 = interval_2

    def __str__(self):
        return "Intervals {} and {} cannot be merged -- " \
               "there is no overlap.".format(self.interval_1, self.interval_2)


class UserInputException(IntervalError):
    """Raised when a user's initial input to main() is not a valid list of intervals"""
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return "Interval list {} is not an even length -- " \
               "you're likely one comma off!".format(self.components)


class Interval:
    """Our representation of a set notation interval."""

    def __init__(self, interval_input: str):
        """Initialize instance of Interval class

        :param interval_input: user-provided string input
               representing integer interval
        """

        # Validate input interval is a string.
        Interval._validate_input(interval_input)

        # Assign valid input to Interval object's :input_string attribute
        self.input_string = interval_input

        # Parse type-valid input, returning relevant interval components.
        interval_groupings, interval_range = self._parse_interval()

        # Store valid opening and closing groupings.
        self.opening, self.closing = interval_groupings

        # Store one of: 'inclusive', 'inclusive-exclusive', 'exclusive-inclusive', 'exclusive'.
        self.description = self._determine_interval_type()

        # Validate lower and upper bounds.
        self._validate_range(interval_range)

        # Store valid starting and ending interval range.
        self.lower, self.upper = interval_range

        # For convenience, store normalized versions of our Interval instance's
        # range. This will help us compare intervals.
        self.normalized_lower = self.lower + 1 if self.opening == '(' else self.lower
        self.normalized_upper = self.upper - 1 if self.closing == ')' else self.upper

    @staticmethod
    def _validate_input(user_input: str):
        """Validate user input is a string.

        :param user_input: user's input to call to Interval constructor
        :return: raises TypeError if invalid, otherwise continues construction
        """

        # Validate input type is string
        if type(user_input) is not str:
            raise TypeError('Interval must be a string.')

    def _parse_interval(self) -> (List[str], List[int]):
        """Given user input is valid, parse it for the interval itself.

        :return: (groupings, range) components of our Interval object
        """

        # Parse input string. This expression handles:
        # \s*        <ignored> any leading whitespace
        # ([\[\(])   1. a single leading '[' or '('
        # \s*        <ignored> any internal whitespace
        # [-]?       2. a single dash (unary minus operator)
        # \d+        3. one or more digits (start of interval)
        # \s*        <ignored> any internal whitespace
        # (,)        4. a single comma
        # \s*        <ignored> some more whitespace
        # ([-]?\d+)  5. (2) and (3), this time representing end of interval
        # \s*        <ignored> any internal whitespace
        # ([\]\)])   6. (1), this time a closing grouping symbol
        # \s*        <ignored> any trailing whitespace
        # Note: escaping the parentheses ('\(', '\)') is not required, but
        #       I prefer to do so. Explicit is better than implicit, etc.
        split_string = re.split(r'^\s*([\[\(])\s*([-]?\d+)\s*(,)\s*([-]?\d+)\s*([\]\)])\s*$', self.input_string)

        # Omit the first and last entries (they're just '') because I'm
        # evidently not very good at capturing regular expressions.
        split_string = split_string[1:-1]

        # Ensure sanitized input is still valid.
        self._validate_parse(split_string)

        # Tie together valid grouping and numeric range characters.
        interval_groupings = [split_string[0], split_string[4]]
        interval_range = [int(split_string[1]), int(split_string[3])]

        return interval_groupings, interval_range

    def _validate_parse(self, parsed_input: List[str]):
        """Check parsed input to be sure it meets our criteria.

        :param parsed_input: user input parsed in _parse_interval
        :return: raises ParsingException if invalid, otherwise continues construction
        """

        # If not, raise a ParsingException that informs the user of the error.
        if not parsed_input:
            raise ParsingException(self.input_string)

        # After being split a valid interval will always be of length 5.
        if len(parsed_input) != 5:
            raise ParsingException(self.input_string)

    def _determine_interval_type(self) -> str:
        """Identify what type of groupings our new Interval is dealing with.

        :return: description of our interval's grouping types
        """

        # Create set of parameters :open and :close
        open_close = {self.opening, self.closing}

        # Run the gauntlet of grouping combinations.
        # Conditional branch either returns string representation
        # of Interval or raises a GroupingException.
        if open_close == {'[', ']'}:
            interval_type = 'inclusive'

        elif open_close == {'[', ')'}:
            interval_type = 'inclusive-exclusive'

        elif open_close == {'(', ']'}:
            interval_type = 'exclusive-inclusive'

        elif open_close == {'(', ')'}:
            interval_type = 'exclusive'

        else:

            # This shouldn't be possible due to our regular expression,
            # but we include it for safety.
            raise GroupingException(self.opening, self.closing)

        return interval_type

    def _validate_range(self, from_to: List[int]):
        """Determine whether our new Interval's range is valid.

        :param from_to: length 2 list containing Interval's proposed
                        lower and upper values
        :return: raises RangeException or RangeMismatchException if
                 start > end or the start-to-end relationship does not
                 fit the Interval's groupings, otherwise continues construction
        """

        # Unpack length 2 parameter representing our interval range.
        start, end = from_to

        # Start should not be greater than the end under any circumstance.
        if start > end:
            raise RangeMismatchException(start, end)

        # Run the gamut of interval type tests.
        # Start and end logic is provided by the assignment instructions.
        if self.description == 'inclusive':
            if not start <= end:
                raise RangeException(start, end)

        elif self.description in ['inclusive-exclusive', 'exclusive-inclusive']:
            if not start < end:
                raise RangeException(start, end)

        elif self.description == 'exclusive':
            if not start < end - 1:
                raise RangeException(start, end)

    def range(self):
        """Provide a way to iterate over an Interval's values.

        :return: Python's builtin range() reflected to represent Interval's groupings
        """

        # Variant range behavior, offset end by 1.
        if self.description == 'inclusive':
            add_amount = [0, 1]

        # Default range behavior, no addition required.
        elif self.description == 'inclusive-exclusive':
            add_amount = [0, 0]

        # Double variant range behavior, offset both by 1.
        elif self.description == 'exclusive-inclusive':
            add_amount = [1, 1]

        # Variant range behavior ('exclusive'), offset start by 1.
        else:
            add_amount = [1, 0]

        return range(self.lower + add_amount[0], self.upper + add_amount[1])

    def __repr__(self):
        """Unambiguous representation of Interval object -- its instantiation."""
        return "Interval('{}{}, {}{}')".format(self.opening, self.lower, self.upper, self.closing)

    def __str__(self):
        """Human-readable representation of Interval object."""
        return "{0}{1}, {2}{3}".format(self.opening, self.lower, self.upper, self.closing)

    # We define binary comparison operators to compare the :normalized_lower
    # field between two intervals. This means [0, 999] < [1, 2]. It also
    # means [2, 3] > [1, 1000].

    def __gt__(self, other):
        return self.normalized_lower > other.normalized_lower

    def __ge__(self, other):
        return self.normalized_lower >= other.normalized_lower

    def __lt__(self, other):
        return self.normalized_lower < other.normalized_lower

    def __le__(self, other):
        return self.normalized_lower <= other.normalized_lower

    def __eq__(self, other):
        """Two Intervals are equal only when their normalized upper and lower are equal.

        Hence: [1, 3], (0, 4), [1, 4), and (0, 3] are all equal.
        """
        return [self.normalized_lower, self.normalized_upper] == \
               [other.normalized_lower, other.normalized_upper]

    def __ne__(self, other):
        """If two Intervals are not equal when using our __eq__ definition, they aren't equal."""
        return not (self == other)


def merge_intervals(interval_1: Interval, interval_2: Interval) -> Interval:
    """Given two intervals, create their union or raise an exception that we can't.

    The criteria for merging any two intervals is that one must be true:
        1. :interval_1 and :interval_2 overlap
        2. :interval_1 and :interval_2 are adjacent
    Hence, if the two are disjointed and not adjacent, we raise an exception.
    Otherwise, we create a new, merged interval based on each individual
    interval's groupings and values. See determine_union().

    :param interval_1: instance of Interval
    :param interval_2: separate instance of Interval
    :return: new instance of Interval such that it represents the union
    """

    # Prepare and coerce our intervals into sets for disjoint evaluation.
    set_1, set_2 = set(interval_1.range()), set(interval_2.range())

    # If our sets are too distant to be merged, raise a DisjointIntervalException.
    if set_1.isdisjoint(set_2) and not is_adjacent_intervals(set_1, set_2):
        raise DisjointIntervalException(interval_1, interval_2)

    # Otherwise, create and return the union/merged interval.
    return union(interval_1, interval_2)


def is_adjacent_intervals(set_1: set, set_2: set) -> bool:
    """Given two sets of integers, determine if they're adjacent.

    We define adjacency to mean if (:set_1's max + 1) is in :set_2 or
    (:set_1's min - 1) is in :set_2. Return their or-evaluation.

    :param set_1: Set of integers representing our first Interval instance
    :param set_2: Set of integers representing our next Interval instance
    :return: boolean denoting whether parameters are adjacent (True) or not (False)
    """

    # If :set_1's max + 1 or min - 1 is in set_2, we have adjacency.
    max_to_min = max(set_1) + 1 in set_2
    min_to_max = min(set_1) - 1 in set_2

    # Return or-evaluation of adjacency conditions.
    return max_to_min or min_to_max


def union(interval_1: Interval, interval_2: Interval) -> Interval:
    """Given two intervals, generate the Interval representation of their union.

    :param interval_1: first interval to be compared
    :param interval_2: second interval to be compared
    :return: four fields required to create new interval: opening, lower, upper, closing.
    """

    # Establish union's lower and upper bounds and groupings.
    lower_interval = interval_2 if interval_1.normalized_lower > interval_2.normalized_lower else interval_1
    upper_interval = interval_2 if interval_1.normalized_upper < interval_2.normalized_upper else interval_1

    # Create and return an Interval with our unified interval groupings and values.
    return Interval('{0}{1}, {2}{3}'.format(lower_interval.opening, lower_interval.lower,
                                            upper_interval.upper, upper_interval.closing))


def merge_overlapping(intervals: List[Interval]) -> List[Interval]:
    """Given a list of intervals, merge overlapping intervals until irreducible.

    :param intervals: list of valid Interval objects
    :return: merged :intervals list of Interval objects
    """

    # Exit early if empty or one interval.
    if len(intervals) in [0, 1]:
        return intervals

    # Sort input list of Intervals
    intervals = sorted(intervals)
    intervals_offset = intervals[1:]

    # Initialize container for successful merges. Also initialize boolean
    # denoting whether we've completed at least one iteration through our
    # list of Intervals.
    successful, one_iteration = [], False

    # Initialize indicators of :intervals' current length and its
    # length during the previous iteration.
    intervals_length_prev, intervals_length = -1, len(intervals)

    # While we can still reduce our list of Interval objects
    while not intervals_length_prev == intervals_length:

        # Initialize bit array. Will be used as a 1:1 look-aside array
        # to denote whether we've merged, at an index i, intervals[i] and
        # intervals[i + 1]. Will eventually determine what intervals are remaining.
        to_be_removed = [False] * len(intervals)

        # Perform pair-wise iteration over intervals.
        for index, pair in enumerate(zip(intervals, intervals_offset)):

            # Isolate the current, next Interval objects.
            current, offset = pair

            try:
                # Attempt to merge the current pair. This may
                # throw a DisjointIntervalException.
                merged = merge_intervals(current, offset)

                # If merge_intervals() does not throw an exception,
                # we consider the merge successful and append it into
                # the :successful container.
                successful.append(merged)

                # Mark to_be_removed at :index and :index + 1 (mapping
                # to removing intervals[:index] and intervals[:index + 1]).
                to_be_removed[index] = True
                to_be_removed[index + 1] = True

            except DisjointIntervalException:

                # In the event where we've traversed the sorted intervals
                # more than once and we still get DisjointIntervalExceptions,
                # return the intervals. Otherwise, continue.
                if one_iteration and intervals_length == intervals_length_prev:
                    return intervals
                else:
                    pass

        # Filter :intervals depending on whether its corresponding look-aside
        # location has been marked as True. True's are removed, False's are kept.
        intervals = filter_intervals(intervals, to_be_removed)
        intervals = extend_and_sort(intervals, successful)

        # Update previous length to current length, then update current length.
        intervals_length_prev, intervals_length = intervals_length, len(intervals)

        # Perform resets to :intervals_offset and :successful;
        # flag that we've completed one iteration.
        intervals_offset, successful, one_iteration = intervals[1:], [], True

    return intervals


def filter_intervals(intervals: List[Any], to_be_removed: List[bool]) -> List:
    """Filter out Interval at intervals[i] if to_be_removed[i] is True.

    :param intervals: any list; used here on a list of Interval objects
    :param to_be_removed: list of booleans denoting whether to remove intervals[i] or not
    :return: intervals that did not get merged in the previous while-loop iteration
    """
    return [interval for index, interval in enumerate(intervals) if not to_be_removed[index]]


def extend_and_sort(intervals: List[Any], successful: List[Any]) -> List:
    """Extend list of Intervals :intervals by :successful and sort the result.

    :param intervals: any list; used here on a list of Interval objects
    :param successful: any list; used here to hold successful merges
    :return: the :intervals extended by :successful, sorted.
    """
    return sorted(intervals + successful)


def insert_into(intervals: List[Interval], insert: Interval) -> List[Interval]:
    """Given a list of Interval objects, insert :insert into the list and reduce.

    :param intervals: list of Interval objects, presumably irreducible
    :param insert: new Interval object to be inserted into :intervals
    :return: the merged, irreducible version of :intervals after inserting :insert
    """
    intervals.append(insert)
    return merge_overlapping(intervals)
