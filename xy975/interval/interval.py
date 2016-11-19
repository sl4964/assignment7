class interval(object):
    def __init__(self,string): 
        """
        Check if the input string is a valid interval. 
        """    
        if (string[0] == '(' or string[0] =='[') and (string[-1] == ')' or string[-1]==']'):
            self.string = string      
            # If the string doesn't have comma, raise ValueError.      
            separate = string.index(',')            
            # If the type of lowerbound or upperbound is not int, raise ValueError.
            self.lowerbound = int(string[1:separate])
            self.upperbound = int(string[separate+1:-1])   
            
            # [lowervalue, uppervalue] represent the close interval equivalent to our input
            if string[0] == '(' :
                lowervalue = self.lowerbound + 1
                self.lower_closed = False
            else:
                lowervalue = self.lowerbound
                self.lower_closed = True
            
            if string[-1] == ')' :
                uppervalue = self.upperbound - 1
                self.upper_closed = False
            else:
                uppervalue = self.upperbound
                self.upper_closed = True
            
            # Check if the input numbers are valid.
            if lowervalue <= uppervalue:
                self.interval_closed = [lowervalue, uppervalue]
            else:
                raise ValueError("Invalid value.")
        
        # If the string is not a interval, raise ValueError
        else:
            raise ValueError("Bound not found.")
            
            
    def __repr__(self):
        return self.string
       
        
def toString(lowervalue, uppervalue, lower_closed, upper_closed):
    """
    This function turns input into string so that it could be applied to interval().
    """
    if lowervalue == uppervalue:
        string = repr(lowervalue)
    else:
        lowerbound = repr(lowervalue)
        upperbound = repr(uppervalue)
        if lower_closed == True:
            lb = '['
        else:
            lb = '('
        
        if upper_closed == True:
            ub = ']'
        else:
            ub = ')'
        string = ''.join([lb, lowerbound, ',', upperbound, ub])
    return string        

    
def mergeIntervals(int1, int2):
    """
    This function merges two strings, int1 and int2, into a new interval string.
    Use the close interval which equivalent to our input to determine how to merge, 
    then return our input, which contains both bound_values and bound_closed.
    """
    # If the amount of arguements != 2, a TypeError would be raised
    # If a arguement is invalid, a ValueError would be raised
    [lowervalue1, uppervalue1] = interval(int1).interval_closed
    [lowervalue2, uppervalue2] = interval(int2).interval_closed
    lowerbound1 = interval(int1).lowerbound
    lowerbound2 = interval(int2).lowerbound
    upperbound1 = interval(int1).upperbound
    upperbound2 = interval(int2).upperbound
    lowerclosed1 = interval(int1).lower_closed
    lowerclosed2 = interval(int2).lower_closed
    upperclosed1 = interval(int1).upper_closed
    upperclosed2 = interval(int2).upper_closed
    if lowervalue1 == lowervalue2:
        if lowerclosed1 == True and lowerclosed2 == True:
            lowervalue = lowerbound1
            lower_closed = True
        else:
            lowervalue = lowervalue1 - 1
            lower_closed = False
        if uppervalue1 < uppervalue2:
            uppervalue = upperbound2
            upper_closed = upperclosed2
        else:
            uppervalue = upperbound1
            upper_closed = upperclosed1
        
    elif lowervalue1 < lowervalue2:
        lowervalue = lowerbound1
        lower_closed = lowerclosed1
        if uppervalue1 < lowervalue2 -1:
            # If it cannot be merged as an interval, a ValueError would be raised
            raise ValueError("Fail to merge.")
        elif uppervalue1 < uppervalue2:
            uppervalue = upperbound2
            upper_closed = upperclosed2
        else:
            uppervalue = upperbound1
            upper_closed = upperclosed1
    
    elif lowervalue1 < uppervalue2 + 2:
        lowervalue = lowerbound2
        lower_closed = lowerclosed2
        if uppervalue1 < uppervalue2:
            uppervalue = upperbound2
            upper_closed = upperclosed2
        else:
            uppervalue = upperbound1
            upper_closed = upperclosed1
    
    else:
        raise ValueError("Fail to merge.")
    
    res = toString(lowervalue, uppervalue, lower_closed, upper_closed)
    return res
    
    
def mergeOverlapping(intervals):
    """
    This function merges strings in list intervals into several intervals.
    """
    # If any element in intervals is not valid, raise ValueError
    intervals.sort(key = lambda x:interval(x).interval_closed[0])
    length = len(intervals)
    res = []
    for i in range(length):
        if res == []:
            res.append(intervals[i])
        else:
            size = len(res)
            try:
                res[size-1] = mergeIntervals(res[size-1], intervals[i])
            except ValueError:
                res.append(intervals[i])
    res = str(res).replace("'","")[1:-1]
    return res
    
    
def insert(intervals, newint):
    """
    This function merges a list of strings with a new interval (type:string).
    """
    intervals.append(newint)
    res = mergeOverlapping(intervals)
    return res