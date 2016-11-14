'''
Created on Nov 8, 2016

@author: peimengsui
'''
from nb_conda.handlers import static

class interval:
    '''
    represents the range of integers between a lower bound and an upper bound
    '''


    def __init__(self, string):
        '''
        Constructor
        '''
        try:
            bounds = [int(s) for s in string[1:-1].split(",")]
            self.left = string.split(",")[0]
            self.right = string.split(",")[1]
            if (string[0] == '[' and string[-1]==']' and bounds[0]  <= bounds[1]):
                self.lower = bounds[0]
                self.upper = bounds[1]
            elif (string[0] == '(' and string[-1]==']' and bounds[0] < bounds[1]):
                self.lower = bounds[0]+1
                self.upper = bounds[1]
            elif (string[0] == '[' and string[-1]==')' and bounds[0] < bounds[1]):
                self.lower = bounds[0]
                self.upper = bounds[1]-1
            elif (string[0] == '(' and string[-1]==')' and bounds[0] < bounds[1]-1):
                self.lower = bounds[0]+1
                self.upper = bounds[1]-1
        except Exception:
            raise ValueError("Invalid interval") 
    @staticmethod   
    def mergeIntervals(int1,int2):
        '''
        This function merge two intervals if they are overlapped or adjacent
        '''
        if int1.lower > int2.lower:
            tmp = int1
            int1 = int2
            int2 = tmp
        string = ''
        if (int1.upper >= int2.lower):
            string = string + int1.left+','
            if int1.upper >= int2.upper:
                string = string +int1.right
            else:
                string = string +int2.right
            return interval(string)
        elif (int1.upper == int2.lower-1):
            string = string + int1.left+',' + int2.right
            return interval(string)
        else:
            raise Exception("no overlap")
    @staticmethod
    def mergeOverlapping(intervals):
        '''
        This function takes a list of intervals and merges all overlapping or adjacent intervals
        '''
        tmp = []
        for i in range(0,len(intervals)):
            try:
                intervals.sort(key= lambda x:x.lower)
                intervals[i+1] = interval.mergeIntervals(intervals[i],intervals[i+1])
            except Exception:
                tmp.append(intervals[i])
        return tmp
    @staticmethod
    def insert(intervals, newint):
        '''
        This function takes two arguments: a list of non-overlapping intervals 
        (i.e. any adjacent or overlapping intervals have been merged); and a single interval. 
        The function should insert newint into intervals, merging the result if necessary. 
        You may assume that the intervals in intlist were initially sorted according to their lower bounds. 
        The resulting list should also be sorted according to their lower bounds.
        '''
        for i in range(0,len(intervals)):
            if newint.lower < intervals[i].lower:
                intervals.insert(i,newint)
                break
            else:
                intervals.append(newint)
        return interval.mergeOverlapping(intervals)
    @staticmethod
    def to_string(intervals):
        string = ""
        for i in range(0,len(intervals)-1):
            string = string + intervals[i].left + ','+intervals[i].right+', '
        string = string + intervals[len(intervals)-1].left+','+intervals[len(intervals)-1].right
        return string
        
                