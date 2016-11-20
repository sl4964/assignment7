'''
Created on Nov 17, 2016

@author: kevinyan
'''

'''Create an interval class '''

class interval(object):
    
    def __init__(self, inputInterval):
        
        self.inputInterval = inputInterval 
        self.lower_border = self.inputInterval[0]  # left sign
        self.upper_border = self.inputInterval[-1]  # right sign                 
        self.lowerBound = int(inputInterval[1:-1].split(',')[0])  # left number in the interval
        self.upperBound = int(inputInterval[1:-1].split(',')[1])  # right number in the interval
        
        '''
        convert all intervals to inclusive ones
        '''
        if self.lower_border == '(' and self.upper_border == ')':
            self.lowerBegin = self.lowerBound + 1
            self.upperEnd = self.upperBound - 1
        elif self.lower_border == '(' and self.upper_border == ']':
            self.lowerBegin = self.lowerBound + 1
            self.upperEnd = self.upperBound
        elif self.lower_border == '[' and self.upper_border == ')':
            self.lowerBegin = self.lowerBound
            self.upperEnd = self.upperBound - 1
        else:
            self.lowerBegin = self.lowerBound
            self.upperEnd = self.upperBound
        
        '''
        The bounds must always meet the requirement that 
        lower <= upper if both bounds are inclusive, 
        lower < upper if one bound is exclusive and one inclusive, 
        or lower < upper-1 if both are exclusive. 
        '''
        
        if self.lower_border == '[' and self.upper_border == ')':
            if self.lowerBound >= self.upperBound:
                raise ValueError('the interval is invalid, enter again:')
        if self.lower_border == '[' and self.upper_border == ']':
            if self.lowerBound > self.upperBound:
                raise ValueError('the interval is invalid, enter again:')
        if self.lower_border == '(' and self.upper_border == ')':
            if self.lowerBound >= self.upperBound - 1:
                raise ValueError('the interval is invalid, enter again:')
        if self.lower_border == '(' and self.upper_border == ']':
            if self.lowerBound >= self.upperBound:
                raise ValueError('the interval is invalid, enter again:')    
        
    
    def __repr__(self):
        return self.inputInterval



def ismergeable(int1, int2):
    if int1.upperEnd < int2.lowerBegin - 1 or int2.upperEnd < int1.lowerBegin - 1:
        return False 
    else:
        return True
 
'''
two intervals can only merge if they are not disjoint
'''
def mergeIntervals(int1, int2):
    if ismergeable(int1, int2) == False:
        raise ValueError("this two intervals are disjoint and cannot be merged")
    
    if int1.lowerBound <= int2.lowerBound and int1.lowerBegin <= int2.lowerBegin:
        newLowerBound = int1.lowerBound
        newLowerBorder = int1.lower_border
    else:
        newLowerBound = int2.lowerBound
        newLowerBorder = int2.lower_border
    if int1.upperBound <= int2.upperBound and int1.upperEnd <= int2.upperEnd:
        newUpperBound = int2.upperBound
        newUpperBorder = int2.upper_border
    else:
        newUpperBound = int1.upperBound
        newUpperBorder = int1.upper_border
    new_interval = newLowerBorder + str(newLowerBound) + ',' + str(newUpperBound) + newUpperBorder
    return interval(new_interval)




def mergeOverlapping(intervals):
    '''
        the function takes list of intervals and merged them
    ''' 
    loopIndex = 0
    intervals.sort(key=lambda x: x.lowerBound)             
                                             
     
    while loopIndex < len(intervals) - 1:
        ismerged = False                                  
        for i in range(loopIndex + 1, len(intervals)):
            if ismergeable(intervals[loopIndex], intervals[i]) == True:
                intervals[loopIndex] = mergeIntervals(intervals[loopIndex], intervals[i])
                intervals.pop(i) 
                ismerged = True
                break
            else:
                pass
        if ismerged == False:
            loopIndex += 1
              
    return intervals       



def insert(intervals, newint):
    intervals.append(newint) 
    intervals.sort(key=lambda x: x.lowerBound)
    return mergeOverlapping(intervals)
