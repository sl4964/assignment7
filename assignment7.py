'''
November 13, 2016, net id: jyc436
Name: Julie Cachia
Python Assignment 7
'''

class interval:
    '''
    This class represents the range of integers between a lower bound and an upper bound. 
    Either of the bounds of an interval can be “inclusive" or “exclusive”.  
    '''
    def __init__(self, intervalString):
        self.intervalInput = intervalString.strip()
        self.intervalIntegers=list(map(int,self.intervalInput[1:-1].split(",")))
        self.lower=(self.intervalInput[0],self.intervalIntegers[0])
        self.upper=(self.intervalInput[-1],self.intervalIntegers[1])
        self.beginning = self.intervalInput[0]
        self.end = self.intervalInput[-1]
                    
        if self.beginning == '(':
            self.first = self.lower[1] + 1
        elif self.beginning == '[':
            self.first = self.lower[1]
        else: 
            raise ValueError("Invalid left bound")
            
        if self.end == ')':
            self.last = self.upper[1] - 1
        elif self.end == ']':
            self.last = self.upper[1]
        else: 
            raise ValueError("Invalid right bound")
            
            ##Qualify the statements
            
        if self.beginning == '(' and self.end == ')':
            if self.lower[1] <= self.upper[1]:
                self.check = True
            else:
                raise ValueError("Beginning integer bigger than end integer")
                
        if self.beginning == '(' and self.end == ']':
            if self.lower[1] < self.upper[1]:
                self.check = True
            else: 
                raise ValueError("Beginning integer is greater than or equal to end integer")
        
        if self.beginning == '[' and self.end == ')':
            if self.lower[1] < self.upper[1]:
                self.check = True
            else:
                raise ValueError("Beginning integer is greater than or equal to end integer")
                
        if self.beginning == '[' and self.end == ']':
            if self.lower[1] < self.upper[1] - 1:
                self.check = True
            else:
                raise ValueError("Beginning integer is greater than or equal to one less than end integer")
        
    def __repr__(self):
        if self.check == True:
            return str(self.lower[0]) + str(self.lower[1]) + "," + str(self.upper[1]) + str(self.upper[0])
        else:
            raise ValueError ("Invalid interval bounds")
     
   
    
    
def mergeIntervals(int1, int2):
    '''
    This function takes two intervals as inputs. 
    If intervals overlap or are adjacent, returns a merged interval.
    '''     
    
    if (int1.first < int2.first and int1.last + 1 < int2.first) or (int2.first < int1.first and int2.last + 1 < int1.first):
        raise ValueError ('Intervals are not overlapping or adjacent, so cannot merge intervals')
    else:    
        #merge
        if int1.first <= int2.first:
            mergedFirst=int1.first
        else: mergedFirst=int2.first
    
        if int1.last >= int2.last:
            mergedLast=int1.last
        else: mergedLast=int2.last

    mergedOutput="(" + str(mergedFirst) + "," + str(mergedLast) + ")"
    return interval(mergedOutput)

def ableToMerge(int1, int2):
    '''
    This function checks whether two intervals are able to be merged together.
    '''
    if int1.last < int2.first -1 or int1.first > int2.last +1:
        return False
    if int1.upper[0] != ']' and int2.lower[0] != '[' and int1.last <= int2.first-1:
        return False
    if int1.lower[0] != '[' and int2.upper[0] != ']' and int1.first >int2.last +1:
        return False
    return True 

def mergeOverlapping(intervals):
    '''
    This function takes a list of intervals and merges all overlapping or adjacent intervals.
    '''
    intervals.sort(key= lambda a: a.first)
    
    beginMerge = intervals[0]
    mergedIntervals = []
    
    for everyInterval in intervals[1:]:
        if ableToMerge(beginMerge, everyInterval):
            new_merged = mergeIntervals(beginMerge, everyInterval)
        else:
            mergedIntervals.append(beginMerge)
            beginMerge = everyInterval
    mergedIntervals.append(beginMerge)
    return mergedIntervals

def insert(intervals, newint):
    '''
    This function inserts newint into intervals, merging the result if necessary.
    '''
    intervals.append(newint)
    return mergeOverlapping(intervals)


import sys

def main():
    '''
    This program uses the class Interval and relevant functions that prompt the user for a list of intervals, 
    reads a string from the user, and creates a list containing these intervals. 
    '''
    while True:
        try:
            user_input = input("List of intervals?") 
            if user_input.lower() == 'quit':
                break
            else:
                splitInput = user_input.split(",")
                list_intervals = []
                for i in range(0, len(splitInput), 2):
                    list_intervals.append(interval(splitInput[i] + ',' + splitInput[i+1]))
                list_intervals = mergeOverlapping(list_intervals)
                break
        except:
            print("invalid interval")
    
    while True:
        try:
            moreInput = input("Intervals?") 
            if moreInput.lower() == 'quit':
                break
            else:
                moreInput = interval(moreInput)
                list_intervals = insert(list_intervals,moreInput)
                print(list_intervals)
        except:
            print("invalid interval")

if __name__ == '__main__':
    main()


