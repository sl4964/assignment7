#Task 6
import unittest
#Taks 1
import numpy as np
import re

class interval:
    
    def __init__(self,lower, upper):
        self.lower = int(lower)
        self.upper = int(upper)
        if lower > upper:
            raise ValueError('The input is invalid.')
      
    def inclusive(lower, upper, fsymbol, bsymbol):
        
        if int(lower) > int(upper):
            raise ValueError('Invalid for inclusive symbol.')
        
        if fsymbol=='[' and bsymbol == ']':
            new_str = np.arange(int(lower),int(upper)+1)
        print('[',new_str,']')
        return new_str
    
    def exclusive(lower, upper, fsymbol, bsymbol):
        
        if int(lower) >= int(upper)-1:
            raise ValueError('Invalid for exclusive symbol.')
        if fsymbol=='(' and bsymbol == ')':
            new_str = np.arange(int(lower)+1,int(upper))
        print('[',new_str,']')
        return new_str
    
    def in_exclusive(lower, upper, fsymbol, bsymbol):
        
        if int(lower) >= int(upper):
            raise ValueError('Invalid for inclusive-exclusive symbol.')
        
        if fsymbol=='[' and bsymbol==')':
            new_str = np.arange(int(lower),int(upper))
            print('[',new_str,')')
            return new_str
        if fsymbol=='(' and bsymbol==']':
            new_str = np.arange(int(lower)+1,int(upper)+1)
            print('(',new_str,']')
        return new_str
   
def Interval():
    b = input('please input: ')
    def tsplit(string, delimiters):
        stack = [string,]
        for delimiter in delimiters:
            for i, substring in enumerate(stack):
                substack = substring.split(delimiter)
                stack.pop(i)
                for j, _substring in enumerate(substack):
                    stack.insert(i+j, _substring)
        return stack
    b1 = tsplit(b, (',','[',']','(',')'))
    #print(b1[0],b1[1],b1[2],b1[3])
    if b[0]=='[' and b[len(b)-1]==']':
        return interval.inclusive(b1[1],b1[2],b[0],b[len(b)-1])
    elif b[0]=='(' and b[len(b)-1]==')':
        return interval.exclusive(b1[1],b1[2],b[0],b[len(b)-1])
    elif b[0]=='[' and b[len(b)-1]==')':
        return interval.in_exclusive(b1[1],b1[2],b[0],b[len(b)-1])
    elif b[0]=='(' and b[len(b)-1]==']':
        return interval.in_exclusive(b1[1],b1[2],b[0],b[len(b)-1])

print('Please input interval int1:')
int1 = Interval()
print('Please input interval int2 which will overlapp with int1 for testing the task2:')
int2 = Interval()
print('Please input interval int3 which will not overlapp with int1 and int2 for testing task 3 and task4:')
int3 = Interval()
print('Please input interval int4 which will cover the gap between int1 and int3 for testing task 4:')
int4 = Interval()

#Taks 2 
def mergeIntervals(int1, int2):
    new = []
    try:
        if int1[0] <= int2[len(int2)-1] and int1[len(int1)-1]>int2[len(int2)-1] and int1[0]>int2[0]:
            new.append(int2[0])
            new.append(int1[len(int1)-1])
            #return new
        elif int1[len(int1)-1] >= int2[0] and int1[len(int1)-1] < int2[len(int2)-1] and int1[0] <int2[0]:
            new.append(int1[0])
            new.append(int2[len(int2)-1])
        return new
    except:
        print('exception')
        
task2 = mergeIntervals(int1, int2)
print('To result interval after merge the first and second input intervals:')
print(task2)

#task 3
import numpy as np
import pandas as pd
from operator import itemgetter
from itertools import groupby

#a = np.arange(3,7) # only for testing, need to input combine with the task1 function
#b = np.arange(4,8) # to gain the inclusive and exclusive restriction
#c = np.arange(9,12)

group = np.unique(np.concatenate((int1,int2,int3),0))

def mergeOverlapping(multi_interval):
    
    lower = upper = group[0]
    for i in group[1:]:
        if i - 1 == upper: 
            upper = i
        else: 
            yield lower, upper
            lower = upper = i
    yield lower, upper
    
task3 = mergeOverlapping(group)
print('The result after merge overlapping/adjacent or isolated interval of first, second, third input intervals(multi-intervals): ')
print(list(task3))

#task 4

def insert(intervals, newInterval):
    results = []
    insertPos = 0
    for interval in intervals:
        if interval[len(intervals)-1] < newInterval[0]:
            results.append(interval)
            insertPos += 1
        elif interval[0] > newInterval[len(newInterval)-1]:
            results.append(interval)
        else:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[len(newInterval)-1] = max(interval[len(intervals)-1], newInterval[len(newInterval)-1])
    results.insert(insertPos, newInterval)
    return results
    

intervals = (int1, int3)
print('The result of non-overlapping intervals of int1 and int2 after being merged by the new insert interval int4:')
print(insert(intervals,int4))

#task 5
import unittest

class task_6(unittest.TestCase):
    def test(self):
        self.assertTrue(mergeIntervals() )
        self.assertTrue(insert())
        self.assertTrue(mergeOverlapping())

    
    if __name__ == '__main__':
        unittest.main()
    
