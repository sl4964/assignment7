'''
    This module includes a class called "Interval", three functions "mergeIntervals" "mergeOverlapping" and"insert", and some user-defined exceptions. When running the program, type "python main.py" in the command prompt, and type in the strings of intervals.
'''
class InputTypeException(Exception):
    pass

class InputValueException(Exception):
    pass

class MergeException(Exception):
    pass

# Make sure input strings are composed of integers, regardless if it is positive of negative
def isIntStr(s):
    if s[0] in ('-', '+'): return s[1:].isdigit()
    return s.isdigit()

class Interval(object):
    def __init__(self, intervalString):
        # check if input string is valid.
        if type(intervalString) != str:
            raise InputTypeException('The input is not String type.')
        elif len(intervalString) < 5:
            raise InputValueException('The length of the input string is less than 5.')
        elif intervalString[0] not in ['(', '[']:
            raise InputValueException('The input string does not start with a \'(\' or \'[\'. A valid example: [2, 5)')
        elif intervalString[-1] not in [')', ']']:
            raise InputValueException('The input string does not end with a \')\' or \']\'. A valid example: [2, 5)') 
        
        # check if upper bound and lower bound are inclusive
        self.lower_is_inclusive = (intervalString[0] == '[')
        self.upper_is_inclusive = (intervalString[-1] == ']')
        
        # exclude the brackets
        intervalString = intervalString[1:-1]
        
        # can't have more than 1 comma
        if intervalString.count(',') != 1:
            raise InputValueException('The input string contains invalid num commas')
        
        # parse the string by comma
        self.lower = intervalString.split(',')[0].strip()
        self.upper = intervalString.split(',')[1].strip()
        
        # check if the left of the comma and the right of the comma are valid integers
        if not isIntStr(self.lower):
            raise InputValueException('The lower bound is not a valid integer')
        if not isIntStr(self.upper):
            raise InputValueException('The upper bound is not a valid integer')
        
        self.lower = int(self.lower)
        self.upper = int(self.upper)
        
        # Some conditions for lower bound and upper bound to be valid
        if self.lower_is_inclusive and self.upper_is_inclusive:
            if self.lower > self.upper:
                raise InputValueException('Lower bound needs to be smaller than or equal to the upper bound.')
        elif self.lower_is_inclusive or self.upper_is_inclusive:
            if self.lower >= self.upper:
                raise InputValueException('Lower bound needs to be smaller than the upper bound.')
        elif (not self.lower_is_inclusive) and (not self.upper_is_inclusive):
            if  self.lower >= self.upper-1:
                raise InputValueException('Lower bound needs to be less than upper bound - 1.')
        
        self.lower_parenthesis='[' if self.lower_is_inclusive else '('
        self.upper_parenthesis=']' if self.upper_is_inclusive else ')'
            
    # To print out the correct form of output
    def __repr__(self):
        return '%s%d,%d%s'%(self.lower_parenthesis, self.lower, self.upper, self.upper_parenthesis)
    
    def makeInclusive(self):
        if not self.lower_is_inclusive:
            self.lower += 1
            self.lower_is_inclusive = True
            self.lower_parenthesis='['
        if not self.upper_is_inclusive:
            self.upper -= 1
            self.upper_is_inclusive = True
            self.upper_parenthesis=']'

# Function to merge two intervals if they are adjacent or overlapped
def mergeIntervals(int1, int2):
    int1.makeInclusive()
    int2.makeInclusive()
    
    # sort two intervals by their lower bounds, so that int1 lower always have a smaller lower bound
    if int1.lower > int2.lower:
        int1, int2 = int2, int1
        
    # if not mergeable, raise error
    if int1.upper + 1 < int2.lower:
        raise MergeException('The two intervals are not mergeable.')
    
    # perform the merge
    lower = min(int1.lower, int2.lower)
    upper = max(int1.upper, int2.upper)
    
    return Interval('[%d,%d]'%(lower, upper))


# Function to merge multiple intervals
def mergeOverlapping(intervals):
    if len(intervals) <= 1:
        return intervals
    
    # sort intervals according to their lower bounds
    sortedInvervals = sorted(intervals, key=lambda i: i.lower)
    result = []
    # Take the first interval in the list as the current interval.
    # If current interval is mergeable with the next interval, then set the merged interval as the current interval and repeat the process.
    # Else, store the current interval in the list, and use the next interval as the current interval.
    currentInterval = sortedInvervals[0]
    for interval in sortedInvervals[1:]:
        try:
            currentInterval = mergeIntervals(currentInterval, interval)
        except MergeException:
            result.append(currentInterval)
            currentInterval = interval
    result.append(currentInterval)
    return result

# Function to insert a interval in a list of intervals
def insert(intervals, newint):
    intlist = intervals + [newint]
    return mergeOverlapping(intlist)


