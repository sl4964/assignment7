'''
Created on Nov 12, 2016

@author: sunyifu
'''
import numpy as np

class IntervalMergeError(Exception):
    pass

class InvalidIntervalError(Exception):
    pass

class interval(object):
    '''
    classdocs
    '''


    def __init__(self, string):
        '''
        Constructor
        '''
        self.lowerbound = np.int(string[1:-1].split(',')[0])
        self.upperbound = np.int(string[1:-1].split(',')[1])
        self.left_parenthesis = string[0]
        self.right_parenthesis = string[-1]
        self.content = string
        if self.left_parenthesis =="(":
            self.actuallowerbound = self.lowerbound + 1
        else:
            self.actuallowerbound = self.lowerbound
        if self.right_parenthesis ==")":
            self.actualupperbound = self.upperbound - 1
        else:
            self.actualupperbound = self.upperbound
        if self.actuallowerbound > self.actualupperbound:
            raise InvalidIntervalError("Invalid interval")
        if string.type != string:
            raise InvalidIntervalError("Invalid interval")
        
        
    def __repr__(self):
        return self.content  
    
def mergeIntervals(int1, int2):
    
    mergedInterval = ""
    if int1.actualupperbound < int2.actuallowerbound or int2.actualupperbound < int1.actuallowerbound:
        raise IntervalMergeError("Two Intervals Doesn't Overlap")
    if int1.actuallowerbound < int2.actuallowerbound and int1.actualupperbound > int2.actuallowerbound:
        return int1
    if int2.actuallowerbound < int1.actuallowerbound and int2.actualupperbound > int1.actuallowerbound:
        return int2
    if int1.actuallowerbound <= int2.actuallowerbound and int1.lowerbound <= int2.lowerbound:
        mergedInterval = mergedInterval + int1.left_parenthesis + str(int1.lowerbound) + ","
    else :
        mergedInterval = mergedInterval + int2.left_parenthesis + str(int2.lowerbound) + ","
    if int1.actualupperbound >= int2.actualupperbound and int1.upperbound >= int2.upperbound:
        mergedInterval = mergedInterval + str(int1.upperbound) + int1.right_parenthesis
    else :
        mergedInterval = mergedInterval + str(int2.upperbound) + int2.right_parenthesis
    return interval(mergedInterval)

    
    
     
def mergeOverlapping(intervals): 
    if len(intervals) <= 1:
        return intervals
    
    sortedInvervals = sorted(intervals, key=lambda x: x.actuallowerbound)
    mergedIntervals = []
    currentIndex = sortedInvervals[0]
    
    for interval in sortedInvervals:
        try :
            currentIndex = mergeIntervals(currentIndex, interval)
        except IntervalMergeError:
            mergedIntervals.append(currentIndex)
            currentIndex = interval
            
    mergedIntervals.append(currentIndex)
    
    return mergedIntervals
            
    
def insert(intervals, newint):
    if len(intervals) == 0:
        return [newint]
    
    insertedIntervals = intervals + [newint]
    
    return  mergeOverlapping(insertedIntervals)
    
