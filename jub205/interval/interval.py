class interval():
    '''Interval Class takes interval string and converts to interval object'''
    def __init__(self, interval):
        
        self.interval = interval
        self.uppper = 0
        self.upperstring = ''
        self.lower = 0
        self.lowerstring = ''
        self.intervallist = []
        self.build_interval()
        
    def build_interval(self):
        '''Determine lower and upper bound and assign
           it to instances'''
        
        intervalsplit = self.interval.split(',')
        
        if len(intervalsplit)!=2:
            raise ValueError('Invalid Input')
            
        lower = intervalsplit[0].strip() 
        upper = intervalsplit[-1].strip()
        self.lowerstring = lower
        self.upperstring = upper
        
        if lower.find('(') >= 0:
            lowernumber = int(lower.replace('(','')) + 1
        elif lower.find('[') >= 0:
            lowernumber = int(lower.replace('[',''))
        else:
            raise ValueError('Invalid interval')
        
        if upper.find(')') >= 0:
            uppernumber = int(upper.replace(')','')) -1
        elif upper.find(']') >= 0:
            uppernumber = int(upper.replace(']',''))
        else:
            raise ValueError('Invalid interval')
    
        if lowernumber > uppernumber:
            raise ValueError('Invalid interval')
            
        self.lower = lowernumber
        self.upper = uppernumber
        self.intervallist = [lowernumber, uppernumber]
        
    def __repr__(self):
        '''Prints the interval'''
        return "%s represents the numbers %d through %d" %(self.interval, self.lower, self.upper)
    
def mergeIntervals(int1, int2):
    '''Function takes two intervals. If the intervals overlap or are adjacent,
        returns a merged interval. If the intervals cannot be merged,
        an exception is thrown.
    '''
    intervals = [int1, int2]
    intervals.sort(key = lambda interval:interval.lower)
    firstint = intervals[0]
    secondint = intervals[1]
    mergedinterval = ''
    
    if firstint.lower <= secondint.lower and firstint.upper >= secondint.upper:
        mergedinterval = firstint
    
    elif secondint.lower >= firstint.lower and secondint.lower <= firstint.upper + 1 and secondint.upper > firstint.upper:
        mergedinterval = interval(','.join([firstint.lowerstring,secondint.upperstring]))
        
    else:
        raise ValueError('Intervals cannot be merged')
        
    return mergedinterval
   
def mergeOverlapping(intervals):
    '''Function takes a list of intervals and merges all overlapping or adjacent intervals'''
    
    if len(intervals)<2:
        
        return intervals
    
    ExitLoop = False
    
    while not ExitLoop:
        
        intervals.sort(key = lambda interval:interval.lower) #Sort intervals by lower bound
        mergedintervals = [] #placeholder for newly merged intervals
        
        i = 0 #While loop counter
        
        while i<len(intervals):
            if i == len(intervals) -1:
                mergedintervals.append(intervals[i])
                i += 1
                continue
            try:
                merged = mergeIntervals(intervals[i], intervals[i+1])                
            except:
                mergedintervals.append(intervals[i])
                i += 1
            else:
                mergedintervals.append(merged)
                i += 2
            
        if intervals == mergedintervals:
            ExitLoop = True
        else:
            intervals = mergedintervals
            
    return mergedintervals
    
    

def insert(intervals, newint):
    '''Function takes two arguments, a list of non-overlapping intervals
       (i.e. any adjacent or overlapping intervals have been merged);
       and a single interval. The function inserts newint into intervals,
       merging the result if necessary. 
    '''
    intervals.append(newint)
    mergedintervals = mergeOverlapping(intervals)
    
    return mergedintervals