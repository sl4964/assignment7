'''
Created on 2016.11.13

@author: xulei
'''

from assignment7 import Interval
from exceptionClass import mergeException


def sortInterval(interval1,interval2):
    intervals=[interval1,interval2]
    sortedInt= sorted(intervals, key=lambda x:(int(x.int_left[1:]),x.lower,x.upper,int(x.int_right[:-1])))       
    #so this define the left bound of merged interval which has left side with smaller integer
    return (sortedInt[0],sortedInt[1])
    
def overLapping(int1,int2): #here int1 and int2 sorted
    if int1.upper<int2.lower-1:
        return False
    else:
        return True
    
def mergeTwo(interval1, interval2): 
    if overLapping(interval1,interval2):
        if interval1.upper<interval2.upper:
            interval_right=interval2.int_right
        elif interval1.upper > interval2.upper:
            interval_right=interval1.int_right
        else: #define when actually the end number is the same, take the one with 'exclusive' half
            if int(interval1.int_right[:-1])<int(interval2.int_right[:-1]): # staring num of int1 is smaller so also means int 1 'exclusive'
                interval_right=interval2.int_right
            else:
                interval_right=interval1.int_right
        
        merged=interval1.int_left+','+interval_right #get a new string 
        return Interval(merged)

def mergeIntervals(int1, int2): 
    interval1,interval2 = sortInterval(int1,int2)   #now interval1 and interval2 follow order
    if not overLapping(interval1,interval2):
        raise mergeException()
    else:
        return mergeTwo(interval1,interval2)


def mergeOverlapping(intervals): #intervals is a list of intervals 
    #taken a list of intervals, return a list of merged with ordered intervals w.r.t first element
    if len(intervals)==0 :
        return intervals
    else:
        sortedInt= sorted(intervals, key=lambda x:(int(x.int_left[1:]),x.lower,x.upper,int(x.int_right[:-1])))
        merged=[sortedInt[0]]
        for  i in range(1,len(sortedInt)):
            if not overLapping(merged[-1],sortedInt[i]):
                merged.append(sortedInt[i])
            else:
                merged[-1]=mergeTwo(merged[-1], sortedInt[i])
        return merged               
            
def insert(intervals,newint):
    for i in range(len(intervals)):
        if overLapping(intervals[i], newint):
            intervals[i]=mergeTwo(intervals[i],newint)
            break
    if i== len(intervals)-1:
       intervals.append(newint)
    return mergeOverlapping(intervals)