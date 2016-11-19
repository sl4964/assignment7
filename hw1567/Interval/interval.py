'''
Created on Nov 9, 2016

@author: wanghezhi
'''
import sys
import re

class interval():
    """class intercal constructor"""
    def __init__(self, inter):
        
        """check whether the input string 'inter' is a valid interval or not. 
        If not raise InvalidIntervals exception"""
    
        if isValidInterval(inter):
            inter = inter.replace(" ", "")
            self.inter = inter
            self.leftsymbol = inter[0]#left_symbol represents '(' or '[' of the interval
            self.rightsymbol = inter[-1]#right_symbol represents ')' or ']' of the interval
            i = inter.index(',')
            self.lowerbound = int(inter[1:i])#lowerbound represents the interval's literal lower bound
            self.upperbound = int(inter[i+1:-1])#upperbound represents the interval's literal upper bound
            
            """real_lowerbound represents the real lowerbound of interval's literal. 
            For example, real_lowerbound of interval '(2,4]' is 3. Similarly for real_upperbound
            and upperbound"""
            if self.leftsymbol == '(':
                self.real_lowerbound = self.lowerbound + 1
            else:
                self.real_lowerbound = self.lowerbound
            if self.rightsymbol == ')':
                self.real_upperbound = self.upperbound - 1
            else:
                self.real_upperbound = self.upperbound             
        else:
            raise InvalidIntervals('Invalid interval')    
    #repr function returns the string of the interval    
    def __repr__(self):
        return self.inter  
    
    def __gt__(self, other):
        return self.real_lowerbound > other.real_lowerbound
    
    def __ge__(self, other):
        return self.real_lowerbound >= other.real_lowerbound
    
    def __lt__(self, other):
        return self.real_lowerbound < other.real_lowerbound
    
    def __le__(self, other):
        return self.real_lowerbound <= other.real_lowerbound    
    
    def __eq__(self, other):
        #Two intervals are equal only when both their real lower bound and real upper bound equals
        return [self.real_lowerbound, self.real_upperbound \
                == other.real_lowerbound, other.real_upperbound]
        
    def __ne__(self, other):
        #Two intervals are not equal if both their real lower bound and real upper bound are not equals
        return not (self == other)
    
def mergeIntervals(int1, int2):
    """
    function mergeIntervals: Taking two intervals, if the intervals overlap or are adjacent,
     returns a merged interval. If the intervals cannot be merged, an IntervalsNotOnverlap 
     exception should be thrown.
    
    parameters:
        int1, int2: intervals
    
    returns: 
        interval(mergestr): merged interval
    
    throws:
       IntervalsNotOnverlap exception if the two intervals cannot be merged     
    """
    
    
    mergestr = ""
    if (int1.real_upperbound < int2.real_lowerbound - 1 or int2.real_upperbound < int1.real_lowerbound - 1):
        raise IntervalsNotOverlap("Two input intervals can't overlap!")
    
    if (int1.real_lowerbound <= int2.real_lowerbound and int1.lowerbound <= int2.lowerbound):
        mergestr = mergestr + int1.leftsymbol + str(int1.lowerbound) + ','
    else:
        mergestr = mergestr + int2.leftsymbol + str(int2.lowerbound) + ','
            
    if (int1.real_upperbound >= int2.real_upperbound and int1.upperbound >= int2.upperbound):
        mergestr = mergestr + str(int1.upperbound) + int1.rightsymbol
    else:
        mergestr = mergestr + str(int2.upperbound) + int2.rightsymbol
            
    return interval(mergestr)
        
def mergeOverlapping(intervals):
    """
    function mergeOverlapping takes a list of intervals and 
    merges all overlapping or adjacent intervals.
    
    Parameters:
        intervals: list of interval objects 
    
    Returns:
        mergelist: list of interval objects
    """
    
    #check every element in the input list of intervals is a valid interval object or not. 
    #If not, raise InvalidIntervals exception
    for inter in intervals:
        if (not isValidInterval(str(inter))):
            raise InvalidIntervals('At least one interval in the interval list is invalid!')
    
    if len(intervals) == 0:
        return []
    
    #sort intervals by their real lower bound
    intervals = sorted(intervals, key = lambda inter: inter.real_lowerbound) 
    mergelist = []
    
    """
    Given the list of interval objects 'intervals', try to merge its first element with the second one
    by calling mergeIntervals function. If merge successfully, insert this merged interval to 'intervals'
    and remove other two intervals that generates the merged interval.
    If the first interval can't merge with the second interval, then put the first interval into the return
    interval list 'mergelist' because not interval can merge with it.
    Doing the above repeatly until we check all the interval objects in the input interval lists.
    """
    i = 0
    while (i < len(intervals)):
        try:
            intervals.insert(i, mergeIntervals(intervals[i], intervals[i+1]))
            intervals.pop(i+1)
            intervals.pop(i+1)
            i = i - 1   
        except:
            mergelist.append(intervals[i])
            pass
        i += 1
        
    return mergelist
    
def insert(intervals, newint):
    """
    function insert will insert newint into intervals, merging the result if necessary.
    
    Parameters:
        intervals: a list of non-overlapping intervals
        newint: a single interval
        
    Return:
        a list of non-overlapping intervals 'mergeOverlapping(intervals)'
    """
    intervals.append(newint)
    return mergeOverlapping(intervals)
        
def isValidInterval(inter):
    """
    Check the input interval 'inter' is valid or not by two steps.
    First, splitting 'inter' and get all interval object attributes
    Second, check whether its real_lowerbound <= real_upperbound.
    If so, return True, if not, return false. 
    """
    inter = inter.replace(" ", "")
    if ((inter[0] == '(' or '[') and (inter[-1] == ')' or ']')):
            i = inter.index(',')
            leftsymbol = inter[0]
            rightsymbol = inter[-1]
            lowerbound = int(inter[1:i])
            upperbound = int(inter[i+1:-1])
            if leftsymbol == '(':
                real_lowerbound = lowerbound + 1
            else:
                real_lowerbound = lowerbound
            if rightsymbol == ')':
                real_upperbound = upperbound - 1
            else:
                real_upperbound = upperbound 
            
            if real_lowerbound <= real_upperbound:
                return True
            else:
                return False
    
def isIntervalListValid(interlist):
    """
    function isIntervalListValid check the all the elements in the input interval list 
    is valid or not by two steps.
    First, using the regular expression to get a list of interval strings
    Second, check each element in the above list is valid by calling function isValidInterval. 
    """
    interlist = interlist.replace(' ', '')
    strlist = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\)\]]+', interlist)
    if strlist == []:
        return False
        
    for inter in strlist:
        if (not isValidInterval(inter)):
            return False
    return True
    
class InvalidIntervals(Exception):
    #raise the exception if the interval is invalid
    pass

class IntervalsNotOverlap(Exception):
    #raise the exception if the two intervals don't overlap.
    pass