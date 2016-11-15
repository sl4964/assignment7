#separate, constructed exceptions
class IntervalError(Exception):
    def __init__(self):
        return "Invalid interval! "
class MergeError(Exception):
    def __init__(self):
        pass
class OverlappingError(Exception):
    def __init__(self):
        return 'Cannot be overlapped! '

''' Q1: Functions will take in a valid interval and
the constructor will take a string representation'''
#check whether user inputs a valid interval
def valid_interval(inp_interval):
    if inp_interval[1][-1] != ')' and inp_interval[0][0] != ']':
        return False
    if inp_interval[0][0]!= '(' and inp_interval[0][0] != '[':
        return False
    if len(inp_interval) % 2 !=0:
        return False

class interval:
    def __init__(self,inp_interval):
        inp_interval = inp_interval.split(',')
        if not valid_interval(inp_interval):
            self.lower = int(inp_interval[0][1:])
            self.upper = int(inp_interval[1][:-1])
            self.lower_bound = inp_interval[0][0]
            self.upper_bound = inp_interval[1][-1]
        if self.lower_bound == '[' :
            self.lb = self.lower
        if self.lower_bound == '(' :
            self.lb = self.lower + 1
        if self.upper_bound == ']' :
            self.ub = self.upper
        if self.upper_bound == ')' :
            self.ub = self.upper - 1
        if self.lower_bound > self.upper_bound:
            raise IntervalError

    def __repr__(self):
        return self.lower_bound + str(self.lower) + ',' + str(self.upper) + str(self.upper_bound)

'''Q2: Merge two adjacent intervals. If the intervals cannot be merged,
an Exception will be thrown'''

def mergeIntervals(int1,int2):
    merged = ""
    if int1.lower > int2.lower:
        temp = int1
        int1 = int2
        int2 = temp

    if int1.upper < (int2.lower - 1) :
        raise MergeError
    elif int1.upper == int2.lower and int1.upper_bound == ')' and int2.lower_bound == '(':
        raise MergeError

    if int1.lower < int2.lower:
        merged = int1.lower_bound + str(int1.lower) +','
    elif int1.lower == int2.lower and int1.lower_bound == '(' and int2.lower_bound == '(':
        merged = '('+ str(int1.lower) + ','
    else:
        merged = '['+ str(int1.lower) + ','

    if int1.upper < int2.upper:
        merged = merged+ str(int2.upper) + int2.upper_bound
    elif int1.upper == int2.upper and int1.upper_bound == ')' and int2.upper_bound == ')':
        merged = merged + str(int2.upper) + ')'
    else:
        merged = merged +str(int2.upper)+ ']'

    return interval(merged)

'''Q3: All overlapping or adjacent intervals will be merged'''
def mergeOverlapping(intervals):
    if len(intervals) == 0:
        return intervals
    intervals = intervals.sort(key=lambda x: x.lower)
    output = []
    l = len(list(intervals))
    for i in range(l):
        try:
            intervals.sort(key=lambda x: x.lower)
            intervals[i+1] = mergeIntervals(intervals[i],intervals[i+1])
        except OverlappingError:
            output.append(intervals[i])
    return output

'''Q4: A new single interval will be inserted into two intervals'''
def insert(intervals, newint):
    intervals.append(newint)
    mergeOverlapping(intervals)
