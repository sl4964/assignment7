'''
Created on Nov 14, 2016

@author: ChuanYa Hsu
'''

import sys
import re

class interval():
    """class interval constructor"""
    def __init__(self, inter):
                
        """check if the input string 'inter' is a valid interval.
         Otherwise, raise InvalidIntervals exception"""
      
        if isValidInterval(inter):
            inter = inter.replace(" ", "") 
            self.inter = inter
            self.leftsymbol = inter[0] #left_symbol represents '(' or '[' of the interval
            self.rightsymbol = inter[-1] #right_symbol represents ')' or ']' of the interval
            i = inter.index(',')
            self.lowerbound = int(inter[1:i]) #lowerbound represents the literal lower bound of the interval
            self.upperbound = int(inter[i+1:-1]) #upperbound represents the literal upper bound of the interval
          
            """real_lowerbound represents the real lower bound of the interval.
            For example, real_lowerbound of interval '(1, 2]' is 0. Same idea for
            real_upperbound and upperbound"""
          
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
    
    def __repr__(self): #repr function returns the string of the interval
        return self.inter
        
    def __gt__(self, other):
        return self.real_lowerbound > other.real_lowerbound
    
    def __ge__(self, other):
        return self.real_lowerbound >= other.real_lowerbound
    
    def __lt__(self, other):
        return self.real_lowerbound > other.real_lowerbound
    
    def __le__(self, other):
        return self.real_lowerbound <= other.real_lowerbound
    
    def __eq__(self, other):
        #two intervals are equal when both their real lower and upper bound equals
        return [self.real_lowerbound, self.real_upperbound \
                 == other.real_lowerbound, other.real_upperbound]
        
    def __ne__(self, other):
        #two intervals are not equal if any of their real lower or upper bound are not equal
        return not (self == other)
    
def mergeIntervals(int1, int2):
        
    """
    function mergeIntervals:
        Taking two intervals. If the intervals overlap or are adjacent, return
        a merged interval. If the intervals cannot be merged, an exception 
        should be thrown.
        
    parameters:
        int1, int2: intervals
        
    returns:
        interval(mergestr): merged interval
        
    throws:
        IntervalsNotOverlap exception if the two intervals cannot be merged
    """
        
    mergestr = ""
    if (int1.real_upperbound < int2.real_lowerbound - 1 or int2.real_upperbound < int1.real_lowerbound - 1):
        raise IntervalsNotOverlap('Two input intervals cannot be merged')
        
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
    function mergeOverlapping:
        Taking a list of intervals and merges all overlapping or adjacent intervals.
            
    parameters:
        intervals: list of interval objects
        
    returns:
        mergelist: list of interval objects
    """
        
    #check every elements in the input list is a valid interval object. If not, raise InvalidIntervals exception
    for inter in intervals:
        if (not isValidInterval(str(inter))):
            raise InvalidIntervals('At least one interval in the list is invalid')
            
    if len(intervals) == 0:
        return []
                
    #sort intervals by their real lower bound
    intervals = sorted(intervals, key = lambda inter: inter.real_lowerbound)
    mergelist = []
        
    """
    Given the list of interval objects 'intervals', try to merge its first element 
    with the second one by calling mergeIntervals function. If merge successfully, 
    insert this merged interval to 'intervals' and remove other two intervals that 
    generates the merged interval. If the first interval can't merge with the second 
    interval, then put the first interval into the return interval list 'mergelist' 
    because not interval can merge with it. Doing the above repeatly until we check 
    all the interval objects in the input interval lists.
    """
        
    i = 0
    while (i < len(intervals)):
        try:
            intervals.insert(i, mergeIntervals(intervals[i], intervals[i+1]))
            intervals.pop(i+1)
            i = i - 1
        except:
            mergelist.append(intervals[i])
            pass
        i += 1 
        
    return mergelist
    
def insert(intervals, newint):
        
    """
    function insert:
        Inserting newint into intervals, merging the result if necessary.
            
    parameters:
        intervals: a list of non-overlapping intervals
        newint: a single interval
        
    returns:
        a list of non-overlapping intervals 'mergeOverlapping(intervals)'
    """
        
    intervals.append(newint)
    return mergeOverlapping(intervals)
    
def isValidInterval(inter):
        
    """
    Check the input interval 'inter' is valid or not.
    First, splitting 'inter' and get all interval object attributes.
    Second, check whether its real_lowerbound <= real_upperbound.
    If so, return True. Otherwise, return false.
    """
        
    inter = inter.replace(" ","")
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
    Check all elements in the input interval list is valid or not.
    First, using the regular expression to get a list of interval strings.
    Second, check each element in the above list is valid by calling function
    isValidInterval.
    """
        
    interlist = interlist.replace(' ', '')
    strlist = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\(\]]+', interlist)
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
    #raise the exception if the two intervals do not overlap
    pass
        
            