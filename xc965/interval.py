"""
This module defines a class allowing user to sort, merge and insert intervals.

NetID: xc965
"""

import re
from UserError import *


class interval(object):

    """
    The interval class represents a range of integers.
    It defines the valid input format and specifies occations of exceptions.
    """
    def __init__(self, inputs):
        # The inputs should not be empty.
        if inputs == '':
            raise EmptyInputError

        # remove the whitespace
        inputs = inputs.replace(' ', '')

        # Inputs should match the regularized interval format.
        # Non-numeric or floats bound values are not accepted.
        if not re.match(r'[\[\(]-?\d+\,-?\d+[\]\)]', inputs):
            raise FormatError

        # The inputs type should be string, an example: (3, 9].
        self.inputs = inputs
        # Lower bound close-open operation should be either '[' or '('.
        self.l = inputs[0]
        # Upper bound close-open operation should be either ']' or ')'.
        self.u = inputs[-1]

        # Devide interval into lower and upper part by splitter.
        k = inputs.index(',')
        # whitespace stripped for lower half in the interval
        self.lower = (inputs[:k]).strip()
        # whitespace stripped for upper half in the interval
        self.upper = (inputs[k+1:]).strip()

        # Bound values should be integers
        self.lb = int(inputs[1:k])  # lower bound value in inputs
        self.ub = int(inputs[k+1:-1])  # upper bound value in inputs

        # Open bound -> the smallest number is the lower bound value plus 1.
        # Close bound -> the smallest number is the lower bound value.
        self.lb += 1 if self.l == '(' else 0
        # Open bound -> the largest number is the upper bound value minus 1.
        # Close bound -> the largest number is the upper bound value.
        self.ub -= 1 if self.u == ')' else 0


        # The lower bound should not be greater than the upper.
        if self.lb > self.ub:
            raise InvalidIntervalError

    def __repr__(self):
        # Define the printing representation
        # In representation, float is allowed,
        # but will be converted into integers in main module.
        return self.lower + ',' + self.upper

    def real_range(self):
        return range(self.lb, self.ub +1)




def mergeIntervals(int1, int2):
    """
    This function takes two parameters (int1, int2).
    It allows user to merge these two intervals if overlapped or adjacent.

    NB:
    When merging, always choose close-bound bracket over open-bound parenthesis.
    This should be emphasized especially when running unittest.
    """

    # Put the interval with a smaller lower bound in the front.
    if int1.lb > int2.lb:
        temp = int1
        int1 = int2
        int2 = temp

    # int1 and int2 should have overlaps or at least be adjacent
    if int2.lb - int1.ub > 1:
        raise NoOverlapError

    else:
        # Find the lower bound for the merged interval
        if int1.lb == int2.lb and int2.l > int1.l:  #  '[' > '(' is True
            merge_lower = int2.lower  # choose '[' over '('
        else:
            merge_lower = int1.lower

        #Find the upper bound for the merged interal
        if int1.ub > int2.ub:
            merge_upper = int1.upper
        elif int1.ub == int2.ub and int1.u > int2.u:  # ']' > ')' is True
            merge_upper = int1.upper  # choose ']' over ')'
        else:
            merge_upper = int2.upper

        return merge_lower + ',' + merge_upper




def mergeOverlapping(intervals):
    """
    This function has one parameter (intervals).
    It allows user to merge multiple overlapping intervals
    and return a non-overlapping interval list.
    """

    # intervals should be a list of interval strings
    intervals = sorted(intervals, key=lambda x: interval(x).lb)  # sort the intervals list by the lower bounds
    stack = []

    for i in range(len(intervals)):

        # Push the first item to the stack
        if i == 0:
            stack.append(intervals[i])

        else:
            # update the merged interval value, if it overlaps with the previous item on stack
            try:
                update = mergeIntervals(interval(stack[-1]), interval(intervals[i]))
                stack[-1] = update

            # push to the stack if not overlapping with the previous item on stack
            except NoOverlapError:
                stack.append(intervals[i])
    return stack




def insert(intervals, newint):
    """
    This function allows user to insert a new interval, i.e. newint,
    into a non-overlapping, sorted and merged interval list, i.e. intervals.

    Intervals should be a list of interval strings,
    while newint should be an interval string.
    """

    intervals += [newint]
    stack = mergeOverlapping(intervals)

    return stack
