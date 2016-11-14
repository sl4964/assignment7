"""
Module storing interval class and error.
"""
from __future__ import print_function
class IntervalError(Exception):
    """
    Exception used for interval errors.
    """
    pass
        
class interval(object):
    """
    This is a class that is used for intervals of integers.
    """
    def __init__(self, intervalStr):
        """
        Sets brackets and bounds based on input. 
        """
        intervalStr = intervalStr.strip()
        lowerBracket = intervalStr[0]
        upperBracket = intervalStr[-1]
        parsedStr = intervalStr[1:-1].split(",")
        #Set bounds that ignore bracket-type
        self.lowerBound = int(parsedStr[0].strip())
        self.upperBound = int(parsedStr[1].strip())
        
        #Update bounds based on bracket type
        if lowerBracket == '(':
            self.lowerBound += 1
        if upperBracket == ')':
            self.upperBound -= 1

        if self.lowerBound > self.upperBound :
            raise IntervalError('Invalid bounds on interval')
        
    def __str__(self) :
        """
        Nicely outputs interval as a closed interval.
        """
        return '['+str(self.lowerBound)+','+str(self.upperBound)+']'

    __repr__ = __str__
    
    def __eq__(self, other):
        return self.lowerBound == other.lowerBound and self.upperBound == other.upperBound

    @staticmethod
    def mergeIntervals(int1, int2):
        """
        Takes two intervals and merges them if they overlap or are adjacent. Throws exception if they cannot be merged.
        """
        if int2.lowerBound < int1.lowerBound:
            int1,int2 = int2,int1        
        if int1.upperBound >= int2.upperBound:
            return int1
        ## Merges adjacent intervals:
        elif int1.upperBound >= int2.lowerBound-1:
            return interval('['+str(int1.lowerBound)+','+str(int2.upperBound)+']')
        else :
            raise IntervalError('Cannot merge intervals')
            
    @staticmethod
    def mergeOverlapping(intervals) :
        """
        Takes a list of intervals and merges overlapping or adjacent intervals. 
        """
        ## We sort the interval to allow for easy merging:
        slist = sorted(intervals,key = lambda val : val.lowerBound)
        retlist = []
        curr = None
        for i in range(len(slist)) :
            if curr is None :
                curr = slist[i]
            else :
                try :
                    curr = interval.mergeIntervals(curr,slist[i])
                except IntervalError:
                    retlist.append(curr)
                    curr = slist[i]
        if curr is not None :
            retlist.append(curr)
        return retlist

    @staticmethod
    def insert(intervals, newint) :
        """
        Inserts a new interval into the list and merges if it can. 
        """
        retlist = intervals
        retlist.append(newint)
        retlist = interval.mergeOverlapping(retlist)
        return retlist

    @staticmethod
    def printList(intervals) :
        """
        Nicely prints intervals as a list.
        """
        for i in range(len(intervals)) :
            if i > 0 :
                print(", ",end="")
            print(intervals[i],end="")
        print('')
        
    @staticmethod    
    def parseList(s) :
        """
        Given a list of intervals as a string, returns a list of interval objects.
        """
        intervals = []
        s = s.strip()
        pos = 0
        while pos < len(s) :
            first = s.find(',',pos)
            second = s.find(',',first+1)
            if first == -1 :
                raise IntervalError('Could not find comma')
            if second == -1 :
                intervals.append(interval(s[pos:]))
                pos = len(s)
            else :
                intervals.append(interval(s[pos:second]))
                pos = second+1
        return intervals
        