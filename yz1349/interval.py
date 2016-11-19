import unittest

class interval(object):
    
    """The interval class represents the range of integers between a lower bound and an upper bound."""
    
    def __init__(self,inputstring):
        self.inputstring     = inputstring.strip()                                       # The input string
        self.leftmost        = self.inputstring[0]                                       # The leftmost character of the input string
        self.rightmost       = self.inputstring[-1]                                      # The rightmost character of the input string
        
        if self.inputstring.find(",") == -1:
            raise ValueError('Invalid input format')                                     # Raise error if no comma is present in the string
        elif len(self.inputstring.split(",")) != 2:
            raise ValueError('Invalid input format')                                     # Raise error if more than one comma is present in the string
        
        comma_index  = self.inputstring.find(",")                                        # Find the index of the comma in the string
        
        try: 
            self.lower = int(self.inputstring[1:comma_index])                            # Evaluate the lower bound
            self.upper =  int(self.inputstring[comma_index+1:len(self.inputstring)-1])   # Evaluate the upper bound
        except:
            raise ValueError('Invalid input format')
        
        if self.leftmost == "(":
            self.lower_inclusive = self.lower + 1
        elif self.leftmost == "[":
            self.lower_inclusive = self.lower
        else:
            raise ValueError('Invalid input format')                                      # Raise error if the leftmost is not a parenthesis or bracket 
        
        if self.rightmost == ")":
            self.upper_inclusive = self.upper - 1
        elif self.rightmost == "]":
            self.upper_inclusive = self.upper
        else:
            raise ValueError('Invalid input format')                                      # Raise error if the rightmost is not a parenthesis or bracket 

        if (self.lower_inclusive <= self.upper_inclusive) == False:
            raise ValueError('Invalid boundary values')
      
    
    def __repr__(self):
        return self.leftmost + str(self.lower) + ',' + str(self.upper) + self.rightmost
        
        
def mergeable(int1,int2):
    
    """ Helper function that determines if two intervals can be merged """
    
    if (int2.lower_inclusive - int1.upper_inclusive > 1 
        or int1.lower_inclusive - int2.upper_inclusive > 1):
        return False
    return True

def mergeIntervals(int1, int2):
    
    """This function takes two intervals class objects as input. 
    If the two intervals overlap or are adjacent, this function merges them into one."""
    
    if mergeable(int1,int2) == False:
        raise ValueError('Invalid input: disjoint intervals')
    lblist = [int1.lower,int2.lower]
    ublist = [int1.upper,int2.upper]                                     # make a list of the bounding values
    leftlist  = [int1.leftmost,int2.leftmost]
    rightlist = [int1.rightmost,int2.rightmost]                          # make a list of the corresponding bracket or parenthesis 
    lower = min(lblist)
    upper = max(ublist)
    leftmost  = leftlist[lblist.index(lower)]  
    rightmost = rightlist[ublist.index(upper)]
    if leftmost == "(":
        if int1.lower == int2.lower:
            if int2.leftmost == "[":
                leftmost = "[" 
    if rightmost == ")":
        if int1.upper == int2.upper:
            if int2.rightmost == "]":
                rightmost = "]"     
    merged = leftmost + str(lower) + ',' + str(upper) + rightmost
    return interval(merged)  

def mergeOverlapping(intervals):
    
    """ This function takes a list of class interval objects and merges all overlapping or adjacent intervals. """
    
    if False in [isinstance(thisinterval, interval) for thisinterval in intervals]:
        raise ValueError('Invalid input: not a list of objects of type interval')
        
    if len(intervals) == 0 or len(intervals) == 1:                   
        return intervals     
    
    intervals.sort(key = lambda x:x.lower) 
    result = []
    while len(intervals) > 1:
        if mergeable(intervals[0],intervals[1]):
            temp = mergeIntervals(intervals[0], intervals[1])
            intervals = intervals[2:]
            intervals.insert(0,temp)
        else:
            result.append(intervals[0])
            intervals = intervals[1:]      
    result.append(intervals[0])
    return result              
    
def insert(intervals, newint):
    
    """ This function takes two arguments: a list of non-overlapping intervals and a single interval. 
    The function inserts the new interval into the list; merges the result if necessary."""
    intervals.append(newint)
    
    return mergeOverlapping(intervals)

if __name__ == '__main__':
    unittest.main()