from exceptions import *
from interval import *

def isOverlapping(int1, int2):
    ''' check if 2 intervals are overlapping/adjacent so they can be merged '''

    if int1.upper+1 == int2.lower and int1.bound_upper==']' and int2.bound_lower=='[':
        return True
    elif int2.upper+1 == int2.lower and int2.bound_upper==']' and int1.bound_lower=='[':
        return True
    elif int1.upper < int2.lower or int1.lower > int2.upper:
        return False
    elif int1.lower == int2.upper and int1.bound_lower == '(' and int2.bound_upper== ')':
        return False
    elif int2.lower == int1.upper and int2.bound_lower == '(' and int1.bound_upper == ')':
        return False
    else:
        return True

def mergeIntervals(int1, int2):
    '''Take 2 intervals from input and merge them. If they are not overlapping/adjacent, 
    raise error.  Then the function find the lower side and the upper side of the merged
    list separately, and return the merged list.
    '''
    if not isOverlapping(int1,int2):
        raise MergeError
        
    intm = '' # merged list
    # find lower side of merged list    
    if int1.lower == int2.lower:
        if int1.bound_lower == '[' or int2.bound_lower == '[':
            intm += '['+ str(int1.lower) + ','
        else:
            intm += '('+ str(int1.lower) + ','
    if int1.lower < int2.lower:
        intm += int1.bound_lower + str(int1.lower) + ','
    if int1.lower > int2.lower:   
        intm += int2.bound_lower + str(int2.lower) + ','
    # find upper side of merged list    
    if int1.upper == int2.upper:
        if int1.bound_upper == ']' or int2.bound_upper == ']':
            intm += str(int1.upper) + ']'
        else:
            intm += str(int1.upper) + ')'
    if int1.upper < int2.upper:
        intm += str(int2.upper) + int2.bound_upper
    if int1.upper > int2.upper:   
        intm += str(int1.upper) + int1.bound_upper
    
    return interval(intm)

def mergeOverlapping(intervals):
    '''The input intervals are first sort by their lower side.
    For each loop, intervals[i] is merged with the next interval until it cannot be merged,
    and return the merged intervals.
    '''
    intervals.sort(key=lambda x: x.lower)  
    i = 0
    while i < len(intervals)-1:
        j = i+1
        if isOverlapping(intervals[i],intervals[j]):
            intervals[i] = mergeIntervals(intervals[i],intervals[j])
            intervals.pop(j)
        else:
            i += 1
    return intervals


def insert(intervals, newint):
    '''Append a new interval into list of intervals,
    then return the updated intervals that are sorted and merged'''
    intervals.append(newint)
    mergeOverlapping(intervals)
    return intervals

