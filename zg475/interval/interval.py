'''Create an interval class '''

class interval(object):
    
    def __init__(self, string):
        
        self.string = string                                             #record the initial string from user
        self.back_sign = self.string[0]                                  #record the interval's left sign
        self.front_sign = self.string[-1]                                #record the interval's right sign
        self.cleaned_str = self.string.strip("[()]")                     #get rid of the brackets or parenthesis of string
        self.splitted_str = self.cleaned_str.split(',')                  #split the string by comma
        self.lower = int(self.splitted_str[0])                           #left bound of the interval
        self.upper = int(self.splitted_str[1])                           #right bound of the interval
        
        if len(self.splitted_str) != 2:
            raise ValueError('Invalid interval,plz fix')                 #the interval like (2,3,5) is invalid 
        
        '''
        Now convert all the interval to the format [num1,num2]
        For example,  (3,6) -->[4,5] ; (3,6] -->[4,6] ; [3,6) -->[3,5] 
        '''
        if self.back_sign =='(' and self.front_sign==')':
            self.lower_modified = self.lower+1
            self.upper_modified = self.upper-1
        elif self.back_sign =='(' and self.front_sign==']':
            self.lower_modified = self.lower+1
            self.upper_modified = self.upper
        elif self.back_sign =='[' and self.front_sign==')':
            self.lower_modified = self.lower
            self.upper_modified = self.upper-1
        else:
            self.lower_modified = self.lower
            self.upper_modified = self.upper
        
        '''
        Handling the error that the bounds doesn't meet requirement
        For example, lower <= upper should be hold if both bounds are inclusive 
        lower < upper   if one bound is exclusive and one inclusive
        '''
        if self.back_sign == '[' and self.front_sign == ']':
            if self.lower > self.upper:
                raise ValueError('Invalid interval')
        if self.back_sign == '[' and self.front_sign == ')':
            if self.lower >= self.upper:
                raise ValueError('Invalid interval')
        if self.back_sign == '(' and self.front_sign == ']':
            if self.lower >= self.upper:
                raise ValueError('Invalid interval')    
        if self.back_sign == '(' and self.front_sign == ')':
            if self.lower >= self.upper-1:
                raise ValueError('Invalid interval')
    
    def __repr__(self):
        return self.string


'''
Helper function which determine whether two intervals is mergeable or not
'''
def mergeable(int1,int2):
    if int1.upper_modified < int2.lower_modified-1 or int2.upper_modified < int1.lower_modified-1:
        return False 
    else:
        return True
 
'''
If the intervals overlap or are adjacent, returns a merged interval. 
If the intervals cannot be merged, an exception should be thrown.
'''
def mergeIntervals(int1, int2):
    #raise exception if two intervals are disjoint
    if mergeable(int1,int2) == False:
        raise ValueError('Those two intervals cannot be merged')
    
    if int1.lower <= int2.lower and int1.lower_modified <= int2.lower_modified:
        new_lower = int1.lower
        new_back_sign = int1.back_sign
    else:
        new_lower = int2.lower
        new_back_sign = int2.back_sign
    if int1.upper <= int2.upper and int1.upper_modified <= int2.upper_modified:
        new_upper = int2.upper
        new_upper_sign = int2.front_sign
    else:
        new_upper = int1.upper
        new_upper_sign = int1.front_sign
    new_interval = new_back_sign+str(new_lower)+','+str(new_upper)+new_upper_sign
    return interval(new_interval)



'''
Takes a list of intervals and merges all overlapping or adjacent intervals.
For example, given interval list[1,5], [2,6), (8,10], [8,18], function would return  [1,6), [8,18]
             given interval list[1,3], [2,6], [5,7], [10,12], function would return  [1,7], [10,12]
'''
def mergeOverlapping(intervals):
    intervals.sort(key = lambda x: x.lower)             #resulting list should be sorted according to their lower bounds 
    counter = 0                                         #counter for merging the list
    
    #merge list from beginning, if two adjacent interval can be merged, we merged into one and pop the second
    #if not, we move one step forward and check the remaining intervals 
    while counter < len(intervals)-1:
        merged = False                                  #tracker for merged status, if merged then we moved one step forward in the loop
        for i in range(counter+1,len(intervals)):
            if mergeable(intervals[counter],intervals[i]) == True:
                intervals[counter] = mergeIntervals(intervals[counter],intervals[i])
                intervals.pop(i) 
                merged = True
                break
            else:
                pass
        if not merged:
            counter+=1
     
    return intervals       



'''
The insert function insert newint into intervals, merged the result when necessary,
the intervals should be initially sorted according to their lower bounds.
'''
def insert(intervals, newint):
    intervals.append(newint) 
    intervals.sort(key = lambda x: x.lower)
    return mergeOverlapping(intervals)

                                                                        