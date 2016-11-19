'''
Main program for assignment 7
@author: jonathanatoy
'''
[]
from interval import *

def isMergeable(int1, int2):
    """Determines whether two intervals are overlapping or adjacent"""
    mergeable = True
    if (int2.lower_bound > int1.upper_bound) or (int1.lower_bound > int2.lower_bound):
        mergeable = False
    if (int1.lower_bound == int2.upper_bound) & (int1.lower_bound + int2.upper_bound == 0):
        mergeable = False
    if (int1.lower_bound == int2.upper_bound) & (int2.lower_bound + int1.upper_bound == 0):
        mergeable = False
    return mergeable

class IntervalException(Exception):
    def __str__(self):
        out = 'There are no integers in this interval. Exception!'
        return out

class MergeException(Exception):
    def __str__(self):
        out = 'There is no overlap between intervals. Exception!'
        return out

def mergeIntervals(int1, int2):
    """Attempts to merge two adjacent or overlapping intervals"""
    if isMergeable(int1, int2):
        l_bound = min(int1.lower_bound, int2.lower_bound)
        u_bound = max(int1.upper_bound, int2.upper_bound)
    else:
        raise MergeException()
    
    
    if (int1.lower_bound < int2.lower_bound):
        exclusive_lower = int1.exclusive_lower
    elif (int2.lower_bound < int1.lower_bound):
        exclusive_lower = int2.exclusive_lower
    ##Inclusive takes precedence if bounds are the same
    else:
        exclusive_lower = (int1.exclusive_lower or int2.exclusive_lower)
    
    if (int1.upper_bound > int2.upper_bound):
        exclusive_upper = int1.exclusive_upper
    elif (int2.upper_bound < int1.upper_bound):
        exclusive_upper = int2.exclusive_upper
    ##Inclusive takes precedence if bounds are the same
    else:
        exclusive_upper = (int1.exclusive_upper or int2.exclusive_upper)
        
    mergeInt = interval(l_bound, u_bound, exclusive_lower, exclusive_upper)
    
    return mergeInt

def mergeOverlapping(intervals):
    """Merges overlapping intervals in a list of intervals"""
    
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda x: x.lower_bound)
    index = 0
    
    # attempt to merge interval with its right neighbor
    # move counter only upon failure (non-overlapping intervals)
    while index < len(intervals) - 1:
        try:
            intervals[index] = mergeIntervals(intervals[index], intervals[index + 1])
            del intervals[index + 1]
        except MergeException:
            index = index + 1
         
    return intervals
   
def insert(intervals, newint):
    """Insert new interval into a list of intervals"""
    
    intervals.append(newint)
    intervals.sort(key=lambda x: x.lower_bound)
    new_intervals = mergeOverlapping(intervals)
    new_intervals.sort(key=lambda x: x.lower_bound)
    return new_intervals

def parseString_Interval(s):
    """Parses string input for parameters for interval constructor"""
    
    if s[0] == '[':
        lower_exclusive = False
    elif s[0] == ')':
        lower_exclusive = True
    else:
        raise IntervalException
    
    if s[-1] == ']':
        upper_exclusive = False
    elif s[-1] == ')':
        upper_exclusive = True
    else:
        raise IntervalException
    
    #split the input to find the lower and upper bounds
    split_int = s.split(',')
    
    #check if either lower or upper bound are empty
    if len(split_int[0]) < 2:
        raise IntervalException
    if len(split_int[1]) < 2:
        raise IntervalException
    
    lower_bound = int(split_int[0][1:])
    upper_bound = int(split_int[1][:-1])
    
    return lower_bound, upper_bound, lower_exclusive, upper_exclusive

def main():
    input_line = str(input("Interval? "))
    int_list = input_line.split(', ')
    intervals = []
    for ints in int_list:
        try:
            lower_bound, upper_bound, lower_exclusive, upper_exclusive = parseString_Interval(ints)
            intervals.append(interval(lower_bound, upper_bound, lower_exclusive, upper_exclusive))
        except IntervalException:
            print('Invalid Intervals')
    
    while True:
        input_line = input_line = input("Interval? ")
        if input_line == 'quit':
            break
        try:
            lower_bound, upper_bound, lower_exclusive, upper_exclusive = parseString_Interval(input_line)
            newint = interval(lower_bound, upper_bound, lower_exclusive, upper_exclusive)
            intervals = insert(intervals, newint)
            print(intervals)
        except  (IntervalException, MergeException):
            print('Invalid interval')

if __name__ == '__main__':
    main()