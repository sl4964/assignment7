class interval:
    '''An 'interval' represents the range of integers between a lower bound and an upper bound.'''
    
    
    def __init__(self, string):
        '''This function takes a string and converts it into an interval. If the string cannot be
        converted into an interval, a ValueError exception is raised.'''
        
        self.lower_bracket = string[0] 
        self.upper_bracket = string[-1] 
        
        try:
            self.lower = int(string.split(',')[0][1:])
            self.upper = int(string.split(',')[1][:-1])
        except:
            raise ValueError('Input is not a valid interval')
    
        #If both brackets are inclusive, ensure that lower <= upper
        if self.lower_bracket == '[' and self.upper_bracket == ']':
            if self.lower > self.upper: 
                raise ValueError('Input is not a valid interval; if both brackets are inclusive, make sure that lower <= upper')
            
        #If one bracket is inclusive, the other exclusive, ensure that lower < upper
        if self.lower_bracket == '[' and self.upper_bracket == ')' or self.lower_bracket == '(' and self.upper_bracket == ']': 
            if self.lower >= self.upper: 
                raise ValueError('Input is not a valid interval; if one bracket is inclusive and the other is exclusive, make sure that lower < upper')

        #If both brackets are exclusive, ensure that lower < upper-1
        if self.lower_bracket == '(' and self.upper_bracket == ')':
            if self.lower >= self.upper-1: 
                raise ValueError('Input is not a valid interval; if both brackets are exclusive, make sure that lower < upper-1')

        #Ensure that brackets are either round '(' or square '['        
        if self.lower_bracket != '(' and self.lower_bracket != '[':  
            raise ValueError('Input is not a valid interval; make sure brackets are correct')
        if self.upper_bracket != ')' and self.upper_bracket != ']':
            raise ValueError('Input is not a valid interval; make sure brackets are correct')

    
    def __repr__(self):
        try: 
            return '%s%d, %d%s' % (self.lower_bracket, self.lower, self.upper, self.upper_bracket)
        except: 
            return 'Invalid interval'

            
def identify_first_element(lower, lower_bracket):
    '''This function identifies the first integer in a given interval.
    For example, identify_first_element( 3,'[' ) will be 3 since the square bracket is inclusive, 
    but identify_first_element(3, '(' ) will be 4 since the round bracket is exclusive.'''
    
    if lower_bracket == '(':
        return lower + 1
    else:
        return lower
    

def identify_last_element(upper, upper_bracket): 
    '''This function identifies the final integer in a given interval. '''
    
    if upper_bracket == ')':
        return upper - 1
    else:
        return upper
    

def mergeIntervals(int1, int2):
    '''This function takes two intervals and merges them into one interval if they are overlapping 
    or adjacent to each other. Otherwise, the function raises an exception indicating that the two 
    intervals are disjoint and cannot be merged.'''
    
    lower_end_1 = identify_first_element(int1.lower, int1.lower_bracket)
    lower_end_2 = identify_first_element(int2.lower, int2.lower_bracket)
    upper_end_1 = identify_last_element(int1.upper, int1.upper_bracket)
    upper_end_2 = identify_last_element(int2.upper, int2.upper_bracket)
    
    # Case where interval 1 covers all of interval 2
    if lower_end_1 <= lower_end_2 and upper_end_1 >= upper_end_2:
        return int1
        
    # Case where interval 1 starts below interval 2
    if lower_end_1 <= lower_end_2 and upper_end_1 < upper_end_2:
        if upper_end_1 < lower_end_2 - 1:
            raise ValueError('Intervals are disjoint')
        else:
            return interval(str(int1.lower_bracket)+str(int1.lower)+','+str(int2.upper)+str(int2.upper_bracket))
        
    # Case where int2 covers all of int1
    if lower_end_2 <= lower_end_1 and upper_end_2 >= upper_end_1:
        return int2
    
    # Case where int2 starts below int1 
    if lower_end_2 <= lower_end_1 and upper_end_2 < upper_end_1:
        if upper_end_2 < lower_end_1 - 1:
            raise ValueError('Intervals are disjoint')
        else:
            return interval(str(int2.lower_bracket)+str(int2.lower)+','+str(int1.upper)+str(int1.upper_bracket))

      
def sort_intervals(intervals):
    '''This function sorts a list of intervals according to their lower bound'''
    i=0
    while i < len(intervals)-1:
        if identify_first_element(intervals[i].lower, intervals[i].lower_bracket) > identify_first_element(intervals[i+1].lower, intervals[i+1].lower_bracket):
            intervals[i], intervals[i+1] = intervals[i+1], intervals[i]
            i = 0
            continue
        else: 
            i = i + 1
    return intervals


def lower_bound_is_equal(int1, int2):
    '''This function determines if the lower bounds of two intervals are equal. This is slightly 
    counterintuitive, but this function will assert that (2,8] and [3,5) have equal lower bounds, since
    the first integer in each interval is 3.'''
    
    if identify_first_element(int1.lower, int1.lower_bracket) == identify_first_element(int2.lower, int2.lower_bracket):
        return True
    else:
        return False
    
def upper_bound_is_equal(int1, int2):
    if identify_last_element(int1.upper, int1.upper_bracket) == identify_last_element(int2.upper, int2.upper_bracket):
        return True
    else:
        return False
    
def intervals_are_equal(int1, int2):
    '''This function determines if two intervals are equal to each other. It considers [3,6] to be equal
    to (2,7).'''
    
    if lower_bound_is_equal(int1, int2) and upper_bound_is_equal(int1,int2):
        return True
    else:
        return False


def mergeOverlapping(intervals):
    '''This function takes a list of intervals and merges all overlapping or adjacent intervals, eventually placing the intervals in a new list.'''
    
    intervals = sort_intervals(intervals)
    new_intervals = [] 
    
    for i in range(len(intervals)): #for each interval 'i' in the list of intervals
        if intervals_are_equal(intervals[i], interval('[0,0]')) == True: #see lines 152-156 below for context
            continue
        
        for k in range(i+1, len(intervals)): #for each interval 'k' to the right of interval 'i'... 
            try:
                intervals[i] = mergeIntervals(intervals[i], intervals[k]) #try merging the two intervals
                intervals[k] = interval('[0,0]') 
                #if merge is successful, drop interval[k] down to [0,0].
                #Say a merge happens when i = 1, k = 3. Then once i=3, you'll encounter a [0,0] interval,
                #so you'll 'continue' on to i = 4.
            except:
                break   #if merging is not possible, move from i to i+1

        new_intervals.append(intervals[i]) #only append intervals that are not equal to [0,0]
            
    return new_intervals      


def insert(intervals, newint):
    '''This function takes two arguments: 1) a list of non-overlapping intervals and 2) a single interval.
    The function inserts the single interval into the existing list, and merges the result if necessary.'''
    
    intervals.append(newint)
    intervals = sort_intervals(intervals)
    return mergeOverlapping(intervals)