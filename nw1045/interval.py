'''
This module contains:

1  Class: 
   (1) Interval: Define a group of intervals, creation and display  
   (2) InputError : User defined exception
   (3) MergeError : User defined exception
2  Functions:
   (1) mergeIntervals
   (2) mergeOverlapping
   (3) insert
   (4) is_int
   
Created on Nov 7, 2016
Last Modified        : 
Version        : 1.0
@author: Nan Wu
'''

def is_int(s):
    ''' 
    little function to check the type of argument 
    Args:
        s: object
    Returns:
        bool: is or not the type of s is int 
    Raises:  
    '''
    try: 
        int(s)
        return True
    except ValueError:
        return False

class InputError(Exception):
    # Handling meaningless Input
    def __str__(self):
        return 'Invalid interval!\n' 
class MergeError(Exception):
    # Handling two intervals can not be merge 
    pass  
  
class Interval():
    '''
    This Interval Class defines the structure and print of intervals.
    The class has a constructor that takes a string representation of the interval.
    
    '''
    def __init__(self, input_interval_string):
        '''
        Constructor of a interval which takes a string input and transforms the interval into 
        its mathematical meaning. 
        raise:
        InputError
        '''
        input_interval_string = input_interval_string.replace(' ', '')
        if (input_interval_string[0] in ['(','[']) and (input_interval_string[-1] in [')',']']) and (',' in input_interval_string) and (len(input_interval_string[1:-1].split(',')) ==2) and (is_int(input_interval_string[1:-1].split(',')[0])) and (is_int(input_interval_string[1:-1].split(',')[1])):
            lower_borded=input_interval_string[0]
            upper_borded=input_interval_string[-1]
            lower=int(input_interval_string[1:-1].split(',')[0])
            upper=int(input_interval_string[1:-1].split(',')[1])
            if (lower_borded=='(' and upper_borded==')' and lower<upper-1) or (lower_borded=='[' and upper_borded==']' and lower<=upper) or (lower_borded=='(' and upper_borded==']' and lower<upper) or (lower_borded=='[' and upper_borded==')' and lower<upper):
            
                self.lower_border=lower_borded
                self.upper_border=upper_borded
                self.lower=lower
                self.upper=upper
                l=lower
                u=upper
                if lower_borded=='(':
                    l=lower+1
                if upper_borded==')':
                    u=upper-1    
                self.list=range(l,u+1)
            else:
                raise InputError
        else:
            raise InputError
                    
        
    def __repr__(self):
        return '%s%d,%d%s' % (self.lower_border, self.lower,self.upper, self.upper_border)
 
def mergeIntervals(Interval1,Interval2):
    '''
    It takes two intervals. If the intervals overlap or are adjacent, returns a merged interval. 
    If the intervals cannot be merged, an exception should be thrown.

    Args:
        Interval1: 
        Interval2:
    Returns:
        Interval
    Raises:
        MergeError
    '''
    if Interval1.list[0]>Interval2.list[-1]+1 or Interval2.list[0]>Interval1.list[-1]+1:
        raise MergeError
    else:
        return Interval('%s%d,%d%s' % ('[', min(Interval1.list[0],Interval2.list[0]),max(Interval1.list[-1],Interval2.list[-1]), ']'))
           
def mergeOverlapping(IntervalList):
    '''
    Takes a list of intervals and merges all overlapping or adjacent intervals
    Args:
        IntervalList: a list of intervals need to be merge and sort
    Returns:
        a list of Interval: sorted according to their lower bounds.
    Raises:
        
    '''
    Final_interval=[]
    for interv in IntervalList:
        Final_interval=insert(Final_interval,interv)
    return Final_interval
  
def insert(IntervalList,newinterval):
    '''
    The function could insert newinterval into  intervals, merging the result if necessary. 
    Args:
        IntervalList: a list of non-overlapping intervals (i.e. any adjacent or overlapping intervals have been merged)
        newinterval: a single interval
    Returns:
        a list of Interval: sorted according to their lower bounds.
    Raises:
        
    '''
    if IntervalList==[]:
        return [newinterval]
    else:  
        Final_interval=[] # The list after insert
        merged_flag=False #  the status of whether or not the newinterval has been merged 
        add_flag=False # the status of whether or not the newinterval has been add into the final_interval
        for n in range(0,len(IntervalList)):
            if merged_flag:
                try:
                    Final_interval[-1]=mergeIntervals(Final_interval[-1], IntervalList[n])
                except MergeError:
                    if Final_interval[-1].lower<IntervalList[n].lower:
                        Final_interval.extend(IntervalList[n:])
                        break
                    else:
                        Final_interval.insert(-1, IntervalList[n])   
            else:
                try:
                    Final_interval.append(mergeIntervals(newinterval,IntervalList[n]))
                    merged_flag=True
                    add_flag=True
                except MergeError:
                    if newinterval.lower<IntervalList[n].lower:
                        Final_interval.append(newinterval)
                        Final_interval.extend(IntervalList[n:])
                        add_flag=True
                        break
                    else:
                        Final_interval.append(IntervalList[n])
        if not add_flag:
            Final_interval.append(newinterval)
        return Final_interval           