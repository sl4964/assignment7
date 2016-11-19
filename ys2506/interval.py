from exceptions import InvalidException, MergeException

class interval:
    LOWER_EXCLUSIVE_MAP = {'(': True, '[': False}
    UPPER_EXCLUSIVE_MAP = {')': True, ']': False}
    #constructor，for object construction
    def __init__(self, string):
        s = string.strip()
        if len(s) == 0:
            raise InvalidException
        
        try:
            self.le = interval.LOWER_EXCLUSIVE_MAP[s[0]]
            self.ue = interval.UPPER_EXCLUSIVE_MAP[s[-1]]
            self.lower, self.upper = [int(e.strip()) for e in s[1:-1].split(',')]
        
        except (KeyError, ValueError):
            raise InvalidException
        
        # to make sure (3,4) is 'Invalid interval'
        if ((self.le and self.ue and self.upper <= self.lower + 1) or
            (not self.le and not self.ue and self.upper < self.lower) or
            (self.upper < self.lower)):
            raise InvalidException
    #Printing an object
    def __str__(self):
        return '{}{},{}{}'.format(
                                  '(' if self.le else '[',
                                  self.lower,
                                  self.upper,
                                  ')' if self.ue else ']'
                                  )
    #when printed or converted to a string
    def __repr__(self):
        return self.__str__()





def mergeIntervals(int1, int2):
    int3 = interval('(-1,1)')
    '''
        if (int1.lower > int2.upper + 1 and not int1.le and not int2.ue or
        int2.lower > int1.upper + 1 and not int2.le and not int1.ue or
        int1.lower >= int2.upper and int1.le and int2.ue or
        int2.lower <= int1.upper and int1.ue and int2.le or
        int1.lower > int2.upper and int1.le or int2.ue
        int2.lower > int1.upper and int2.le or int1.ue):
        raise ValueError("these two intervals cannot be merged")
        if (int1.lower >= int2.upper and int1.le and int2.ue or
        int2.lower <= int1.upper and int1.ue and int2.le)
        '''
    #check whether the two intervals could be merge
    if int1.upper < int2.lower:
        if not int1.ue and not int2.le and int1.upper + 1 == int2.lower:
            pass
        else:
            raise MergeException
    if int2.upper < int1.lower:
        if not int2.ue and not int1.le and int2.upper + 1 == int1.lower:
            pass
        else:
            raise MergeException
    if int1.upper == int2.lower:
        if not (int1.ue or int2.le):
            raise MergeException
    if int1.upper == int2.lower:
        if not (int1.ue or int2.le):
            raise MergeException

#merge the lower and lower exclusive
    int3.lower = int1.lower if int1.lower <= int2.lower else int2.lower
    
    if int1.lower == int2.lower:
            if not(int1.le and int2.le):
                int3.le = False
            else:
                int3.le = True
    else:
        int3.le = int1.le if int1.lower < int2.lower else int2.le
        
    #merge the upper and upper exclusive
    int3.upper = int1.upper if int1.upper >= int2.upper else int2.upper
    if int1.upper == int2.upper:
        if not(int1.ue and int2.ue):
            int3.ue = False
        else:
            int3.ue = True
    else:    
        int3.ue = int1.ue if int1.upper > int2.upper else int2.ue
    return int3


def mergeOverlapping(intervals):
    intervals.sort(key = lambda i: (i.lower, -i.upper))
    results = [intervals[0]]
    for elem in intervals[1:]:
        try:
            results[-1] = mergeIntervals(results[-1], elem)
        except MergeException:
            results.append(elem)
    return results

def insert(intervals, newint):
    intervals.append(newint)
    return mergeOverlapping(intervals)


