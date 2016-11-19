'''
Created on Nov 14, 2016

@author: muriel820
'''
class IntervalErrors(Exception):
    '''Superclass of Exceptions'''
    pass
class InputNotString(IntervalErrors):
    def __str__(self):
        return 'Please input as a string'
class MissingBracket(IntervalErrors):
    def __str__(self):
        return 'Your input should state either inclusive or exclusive with [] or ().\n '
class CommaError(IntervalErrors):
    def __str__(self):
        return 'Your input should include only one comma, separating the lower bound and upper bound.\n '
class IntervalNoExistence(IntervalErrors):
    def __str__(self):
        return 'Your interval has a non positive size, please check\n'


class Interval(object):
    
    
    '''
    Define the constructor of object 'Interval'
    '''         
    def __init__(self, interval_input):
        
        '''
        Check whether input is a string input, if not raise error
        Check whether input provides correct brackets, if not raise error
        Check whether two integers are separated by comma, if not raise error
        '''
        if type(interval_input) != str:
            raise InputNotString
        self.input = interval_input.replace(" ","")
        self.left_bracket = self.input[0]
        self.right_bracket = self.input[-1]
        if (self.left_bracket != '(' and self.left_bracket != '[' ) or (self.right_bracket != ')' and self.right_bracket != ']' ):
            raise MissingBracket()
        self.inner = self.input[1:-1].split(",")
        if len(self.inner) != 2 :
            raise CommaError()

        
        
        '''
        define inclusive or exclusive with brackets, set default as [a,b)
        because default of range in python is also lower inclusive, upper exclusive.
        store corresponding lowerbound and upperbound by default form
        store the list of integers included in such an interval
        raise exception if there's paradox in input
        (such as: lower bound excluded a number, while upper bound included it
        or lower bound is greater than upper bound)
        it will also raise ValueError by default if input are not integers(but float, double, etc.)
        '''
        self.left_end = int(self.input[1:-1].split(",")[0])
        self.right_end = int(self.input[1:-1].split(",")[1])
        if self.left_bracket == '(':
            self.left_end = self.left_end + 1
        if self.right_bracket == ']':
            self.right_end += 1
        if self.left_end >= self.right_end:
            raise IntervalNoExistence()
        self.integerlist = []
        for x in range(self.left_end,self.right_end):
            self.integerlist.append(x)
    
    '''
    Define output form of interval
    '''
    def __repr__(self):
        str =  '%s ' % self.input
        return str
    
    '''
    Define equality between two intervals by comparing their uniformed lower and upper bounds
    '''
    def __eq__(self, other):
        return (self.left_end == other.left_end and self.right_end == other.right_end)


'''
Define function to merge two intervals, 
return to a tuple of input intervals if unable to merge
return to a new interval if merge succeeded
'''    
def mergeIntervals(int1,int2):
    if (int1.left_end >int2.right_end or int2.left_end >int1.right_end):
        return int1,int2
    else:
        left_end = min(int1.left_end, int2.left_end)
        right_end = max(int1.right_end, int2.right_end)
        str =  '[ %d , %d )'% (left_end, right_end) 
        new_merge = Interval(str)
        return new_merge

'''
Sort the interval list first by their lowerbound, because of reason below:
For example, a sorted interval list a has a[0],a[1],a[2]
if a[0] cant merge with a[1], it means a[0].right_end < a[1].left_end <a[2].left_end
which means a[0] cant merge with a[2] either.
'''
def mergeOverlapping(intervals):
    if len(intervals) in range(0, 1):
        return intervals
    else:
        intervals = sorted(intervals, key = lambda interval: interval.left_end)
        merged_list = [intervals[0]]
        for i in range(0, len(intervals)):
            new_merge = mergeIntervals(merged_list[-1], intervals[i])
            if type(new_merge) == tuple:
                merged_list.append(intervals[i])
            else:
                merged_list[-1] = new_merge
        return merged_list

'''
insert a new interval into an interval list by append,sort,and mergeOverlapping
'''    
def insert(intervals, newint):
    if type(newint) != Interval:
        newint = Interval(newint)
    if len(intervals) == 0:
        intervals.append(newint)
        return intervals
    else:
        intervals.append(newint)
        intervals = sorted(intervals, key = lambda interval: interval.left_end)
        intervals = mergeOverlapping(intervals)
        return intervals
    