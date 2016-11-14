import re

class interval(object):
    '''
    interval Class and its methods and helper functions.
    '''

    def __init__(self, userinput):
        '''
        Constructor: inits interval object from string user input
        Raises ValueError if interval format or bounds is invalid
        '''
        
        if not re.match(r"(\(|\[)-?\d+,\s?-?\d+(\)|\])", userinput):
            raise ValueError("Invalid interval format")        
        
        self.lowerBoundIsExclusive = userinput.startswith("(")
        self.upperBoundIsExclusive = userinput.endswith(")")
        
        splitInterval = userinput.split(",")
        self.lower = int(splitInterval[0][1:])
        self.upper = int(splitInterval[1][:-1])
        
        # check interval covers valid range
        if self.lowerBoundIsExclusive and self.upperBoundIsExclusive:
            if self.lower >= self.upper - 1:
                raise ValueError("Invalid interval")
        
        if not self.lowerBoundIsExclusive and not self.upperBoundIsExclusive:
            if self.lower > self.upper:
                raise ValueError("Invalid interval")
        
        if self.lowerBoundIsExclusive != self.upperBoundIsExclusive:
            if self.lower >= self.upper:
                raise ValueError("Invalid interval")
    
    @classmethod
    def parseList(cls, listAsString):
        '''
        Parse string representation of list of intervals
        Returns list of interval objects
        '''
        if listAsString == "":
            return []
        
        split = [word.strip() for word in listAsString.split(",")]
            
        if len(split) % 2 == 1:
            raise ValueError("Invalid list of intervals")
        
        return [
            interval(",".join(split[index * 2 : index * 2 + 2]))
            for index in range(int(len(split) / 2))
        ]    
    
    def __repr__(self):
        '''
        Defines string representation of interval object
        '''
        return "{}{},{}{}".format(
            "(" if self.lowerBoundIsExclusive else "[",
            self.lower,
            self.upper,
            ")" if self.upperBoundIsExclusive else "]"
        )

    def inclusiveLowerBoundValue(self):
        '''
        Return normalized inclusive lower bound of interval object
        E.g. interval with lower bound (2 and [4 return 3
        '''
        if self.lowerBoundIsExclusive:
            return self.lower + 1 
        else:
            return self.lower
    
    def inclusiveUpperBoundValue(self):
        '''
        Return normalized inclusive upper bound of interval object
        E.g. interval with uppe rbound 5) and 4] return 4
        '''
        if self.upperBoundIsExclusive:
            return self.upper - 1
        else:
            return self.upper
    
    def comparisonValues(self):
        '''
        Return tuple of normalized and original lower/upper values for interval comparison
        '''
        return (
            self.inclusiveLowerBoundValue(),
            self.inclusiveUpperBoundValue(),
            self.lower,
            self.upper
        )        

    def __lt__(self, other):
        '''
        Overloads "<" operator for interval objects
        Returns true if normalized and initial lower/upper values are less
        '''
        return self.comparisonValues() < other.comparisonValues()
    
    def __eq__(self, other):
        '''
        Overloads "=" operator for interval objects
        Returns true if normalized and initial lower/upper values are equal
        '''
        return self.comparisonValues() == other.comparisonValues()
        
    def contains(self, other):
        '''
        Returns true if interval contains other interval
        '''
        return (
            self.inclusiveLowerBoundValue() <= other.inclusiveLowerBoundValue() and 
            self.inclusiveUpperBoundValue() >= other.inclusiveUpperBoundValue()
        )
    
    def intersects(self, other):
        '''
        Returns true if intervals overlap
        '''
        int1, int2 = sorted((self, other))
        return int1.inclusiveUpperBoundValue() >= int2.inclusiveLowerBoundValue()    
    
    def adjacent(self, other):
        '''
        Returns true if intervals are adjacent (nonoverlapping)
        '''
        int1, int2 = sorted((self, other))
        return int1.inclusiveUpperBoundValue() + 1 == int2.inclusiveLowerBoundValue()
    
def mergeIntervals(int1, int2):
    '''
    Takes 2 interval objects. Returns a merged interval or raises an Exception if merger not possible
    '''
    if int1.contains(int2):
        return int1
    
    elif int2.contains(int1):
        return int2
    
    elif int1.adjacent(int2) or int1.intersects(int2):
        sortedint1, sortedint2 = sorted((int1, int2))
        
        return interval("[{},{}]".format(
            sortedint1.inclusiveLowerBoundValue(),
            sortedint2.inclusiveUpperBoundValue()
        ))
        
    else:
        raise Exception("Nonoverlapping nonadjacent intervals, cannot merge")    
    
def mergeOverlapping(intervals):
    '''
    Takes a list of intervals objects
    Returns a list with all possible mergers performed
    '''    
    merged = []
    current = None
    
    for interval in sorted(intervals):
        if current is None:
            current = interval
        
        elif current.adjacent(interval) or current.intersects(interval):
            current = mergeIntervals(current, interval)
        
        else:
            merged.append(current)
            current = interval
    
    if current is not None:    
        merged.append(current)   
    
    return merged

def insert(intervals, newint):
    '''
    Takes a list of intervals and an interval object
    Merges interval with all possible intervals in list. Returns a list of intervals
    '''
    return mergeOverlapping(intervals + [newint])
