class interval(object):
    '''represents the range of intergers between a lower bound and an upper bound.'''
    def __init__(self, intervalInput):
        '''outputs only valid intervals'''
        if (intervalInput[0] == '[' or '(') and (intervalInput[-1] == ']' or ')'):
            self.lower = int(intervalInput[1:-1].split(',')[0])
            self.upper = int(intervalInput[1:-1].split(',')[1])
            self.lowerbound = intervalInput[0]
            self.upperbound = intervalInput[-1]
            if self.lowerbound == '[' and self.upperbound == ']' and self.lower <= self.upper:
                self.validInterval = intervalInput
            elif (self.lowerbound == '(' and self.upperbound == ']') or (self.lowerbound == '[' and self.upperbound == ')') and self.lower < self.upper:
                self.validInterval = intervalInput
            elif self.lowerbound == '(' and self.upperbound == ')' and self.lower < self.upper - 1:
                self.validInterval = intervalInput
            else:
                raise ValueError('Invalid interval.')
                #throws an error if the interval is invalid
        else:
            raise ValueError('Invalid interval.')
            #throws an error if the interval is invalid
        
    def __repr__(self):
        return self.validInterval

def mergeIntervals(int1, int2):
    '''take two intervals and merge if they overlap or are adjacent, return a merged interval'''
    interval1 = interval(str(int1))
    interval2 = interval(str(int2))
    if interval1 == interval2:
        mergedInterval = interval1
    elif (interval1.upper > interval2.lower and interval1.upper < interval2.upper) or (interval1.upper == interval2.lower and (interval1.upperbound == "]" or interval2.lowerbound == "[")):
        mergedInterval = interval1.lowerbound + str(interval1.lower) + ',' + str(interval2.upper) + interval2.upperbound
    elif interval1.upper > interval2.upper:
        mergedInterval = interval1
    elif interval1.upper == interval2.upper:
        if interval1.upperbound == ']':
            mergedInterval = interval1
        elif interval2.upperbound == ']':
            mergedInterval = interval1.lowerbound + str(interval1.lower) + ',' + str(interval2.upper) + interval2.upperbound
        elif interval1.upperbound == interval2.upperbound == ')':
            mergedInterval = interval1
    else:
        raise ValueError('Intervals cannot be merged.')
    return mergedInterval

def mergeTrue(int1, int2):
    '''test if two intervals can be merged'''
    interval1 = interval(str(int1))
    interval2 = interval(str(int2))
    if interval1 == interval2:
        merged = True
    elif (interval1.upper > interval2.lower and interval1.upper < interval2.upper) or (interval1.upper == interval2.lower and (interval1.upperbound == "]" or interval2.lowerbound == "[")):
        merged = True
    elif interval1.upper > interval2.upper:
        merged = True
    elif interval1.upper == interval2.upper:
        if interval1.upperbound == ']':
            merged = True
        elif interval2.upperbound == ']':
            merged = True
        elif interval1.upperbound == interval2.upperbound == ')':
            merged = True
    else:
        merged = False
    return merged

def mergeOverlapping(intervals):
    '''take a list of intervals and merge all overlapping or adjacent intervals'''
    intervals.sort(key=lambda x: interval(x).lower)
    newList = []
    initialInterval = intervals[0]
    for i in range(1, len(intervals)):
        newInterval = intervals[i]
        if mergeTrue(initialInterval, newInterval) == True:
            initialInterval = mergeIntervals(initialInterval, newInterval)
        else:
            newList.append(str(initialInterval))
            initialInterval = newInterval
        if i == len(intervals)-1:
            newList.append(str(initialInterval))
    return newList
    
def insert(intervals, newint):
    '''take a list of non-overlapping intervals and a single interval and insert the interval into the list of intervals, merging the result if necessary'''
    intervals.append(newint)
    return mergeOverlapping(intervals)
             