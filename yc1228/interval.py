class IntervalException(Exception):
    def __init__(self):
        '''Return error message when the input intervals are invalid '''
        return "Invalid input intervals!\n"

class IntervalMergeException(Exception):
    def __init__(self):
        '''Handle two intervals that cannot be merged'''
        pass
class NoOverlappingException(Exception):
    def __init__(self):
        '''Return error message when two intervals do not overlap'''
        return "No Overlapping!\n"
    
#Check whether the interval is valid or not    
def valid_interval(input_interval):
    if len(input_interval) % 2 !=0:
        return False
    if input_interval[0][0] != '(' and input_interval[0][0] != '[':
        return False
    if input_interval[1][-1] != ')' and input_interval[0][0] != ']':
        return False
    

class interval:
    '''Class interval represents the range of integers between a lower bound 
    and an upper bound'''
    def __init__(self,input_interval):
        '''A constructor takes a string representation of the interval
        and ensure that the interval is valid '''
        input_interval = input_interval.split(',')
        if not valid_interval(input_interval):
            self.lower = int(input_interval[0][1:])  
            self.upper = int(input_interval[1][:-1])
            self.lower_bound = input_interval[0][0]
            self.upper_bound = input_interval[1][-1]
            if self.lower_bound == '[' :
                self.lb = self.lower
            if self.lower_bound == '(' :
                self.lb = self.lower + 1
            if self.upper_bound == ']' :
                self.ub = self.upper
            if self.upper_bound == ')' :
                self.ub = self.upper - 1
            if self.lb > self.ub:
                raise IntervalException

        
    def __repr__(self):
        '''Return a string of interval'''
        return self.lower_bound + str(self.lower) + ',' + str(self.upper) + str(self.upper_bound)
    

def mergeIntervals(int1,int2):
    '''Merge two intervals that overlap or are adjacent; otherwise, throw an
    exception'''
    mergedint = ""
    # sort int1 and int2
    if int1.lower > int2.lower:
        temp = int1
        int1 = int2
        int2 = temp
        
    if int1.upper < (int2.lower - 1) :
        raise IntervalMergeException
    elif int1.upper == int2.lower and int1.upper_bound == ')' and int2.lower_bound == '(':
        raise IntervalMergeException
  
    if int1.lower < int2.lower:
        mergedint = int1.lower_bound + str(int1.lower) +','
    elif int1.lower == int2.lower and int1.lower_bound == '(' and int2.lower_bound == '(':
        mergedint = '('+ str(int1.lower) + ','
    else:
        mergedint = '['+ str(int1.lower) + ','
    
    
    if int1.upper < int2.upper:
        mergedint = mergedint + str(int2.upper) + int2.upper_bound
    elif int1.upper == int2.upper and int1.upper_bound == ')' and int2.upper_bound == ')':
        mergedint = mergedint + str(int2.upper) + ')'
    else:
        mergedint = mergedint +str(int2.upper)+ ']'
    
    return interval(mergedint)   
        

def mergeOverlapping(intervals):
    '''Merge all overlapping or adjacent intervals'''
    if len(intervals) <= 1:
        return intervals
    intervals = intervals.sort(key=lambda x: x.lower)
    result = []
    length = len(intervals)
    for i in range(0, length):
        try:
            intervals.sort(key=lambda x: x.lower)
            intervals[i+1] = mergeIntervals(intervals[i],intervals[i+1])
        except NoOverlappingException:
            result.append(intervals[i])
    return result
 

def insert(intervals, newint):
    '''Merge the new interval with a list of non-overlapping intervals'''
    intervals.append(newint)
    mergeOverlapping(intervals)
    