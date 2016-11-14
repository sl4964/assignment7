'''
Created on Nov 11, 2016

@author: Fanglin Chen
'''
from interval import *

def mergeIntervals(int1, int2):
    '''
    The function takes two intervals as arguments. 
    If the intervals overlap or are adjacent, it returns a merged interval. 
    If the intervals cannot be merged, it throws an exception.
    '''
    if int1.lower_integer <= int2.lower_integer:
        if int1.upper_integer >= int2.lower_integer - 1:
            if int1.upper_integer > int2.upper_integer:
                return int1
            else:
                return interval(str(int1)[0] + str(int1.lower) + ', ' + str(int2.upper) + str(int2)[-1])
        else:
            raise Exception('The intervals cannot be merged')
            
    else:
        if int1.lower_integer <= int2.upper_integer + 1:
            if int1.upper_integer > int2.upper_integer:
                return interval(str(int2)[0] + str(int2.lower) + ', ' + str(int1.upper) + str(int1)[-1])
            else:
                return int2
        else:
            raise Exception('The intervals cannot be merged')
        
def mergeOverlapping(intervals):
    '''
    The function takes a list of intervals and merges all overlapping or adjacent intervals.
    '''   
    intervals.sort(key = lambda i: i.lower)  # Sort the intervals by their lower bounds
    previous = 0
    for i in range(1, len(intervals)):
        if intervals[previous].upper_integer >= intervals[i].lower_integer - 1:
            intervals[previous] = mergeIntervals(intervals[previous], intervals[i])  # Starting from the second interval, merge each interval with its previous interval
        else:
            previous += 1
            intervals[previous] = intervals[i]                   
    return intervals[:previous + 1]

def insert(intervals, newint):
    '''
    The function takes a list of intervals and a single interval as arguments. 
    It inserts newint into intervals, merging the result if necessary.
    '''
    intervals.append(newint)
    intervals = mergeOverlapping(intervals)
    return intervals


    
        
    