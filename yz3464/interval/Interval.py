'''
Created on Nov 09, 2016

@author: twff
'''
class Interval(object):
    def __init__(self, lower, upper):
        '''
        lower should be smaller than upper, if not switch.
        int
        '''
        if lower > upper:
            a = lower
            lower = upper
            upper = a
        self._lower = lower
        self._upper = upper

  
    def __str__(self):
        return '[%d, %d]' % (self._lower, self._upper)
    
    def __repr__(self):
        return 'interval(%d, %d)' % (self._lower, self._upper)
    
    '''
      below are class method
     '''
    @classmethod
    def stringRep(cls, s):
        s = s
        if s == '':
            raise ValueError("input is empty")

        if s[0] == '(':
            left_bound = True
        elif s[0] == '[':
            left_bound = False
        else:
            raise ValueError("invalid lower bound input")

        try:
            comma_index = s.index(',')
        except ValueError:
            raise ValueError("missing comma")

        left_value = int(s[1:comma_index])
        right_value = int(s[comma_index+1:-1])

        if s[-1] == ')':
            right_bound = True
        elif s[-1] == ']':
            right_bound = False
        else:
            raise ValueError("invalid upper bound input")
        
        
        if left_bound:
            b = left_value + 1
        else:
            b = left_value
        
        if right_bound:
            c = right_value -1
        else:
            c = right_value
        
        if b>=c:
            raise ValueError("invalid input, since lower is bigger than upper")

        return Interval(b, c)

    def __or__(self, value):
        return mergeIntervals(self, value)

    def __eq__(self, value):
        return (self._lower == value._lower) and (self._upper == value._upper)

    def __ne__(self, value):
        return (self._lower != value._lower) or (self._upper != value._upper)





def overlapOrAdjacent(int1, int2):
    '''
    Determines whether two intervals int1 and int2 are adjacent to each other
    '''
    if int1._lower > int2._lower:
        int_lower = int2
        int_upper = int1
    else:
        int_lower = int1
        int_upper = int2
    if int_lower._upper < int_upper._lower - 1:
        return False
    else:
        return True


def mergeIntervals(int1, int2):
    if not overlapOrAdjacent(int1, int2):
        raise ValueError('intervals are not overlapping or adjacent')
    lower = min(int1._lower, int2._lower)
    upper = max(int1._upper, int2._upper)
    return Interval(lower, upper)


def mergeOverlapping(intervals):
    '''
    Merges a list of intervals
    '''
    if len(intervals) == 0:
        return []
    n = len(intervals)
    intervals = sorted(intervals, key=lambda x: x._lower)
    merged = [intervals[0]]
    for i in range(1, n):
        if overlapOrAdjacent(merged[-1], intervals[i]):
            merged[-1] = mergeIntervals(merged[-1], intervals[i])
        else:
            merged.append(intervals[i])
    return merged


def insert(intervals, newint):
    intervals = intervals + [newint]
    result = mergeOverlapping(intervals)
    return result