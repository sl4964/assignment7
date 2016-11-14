'''
Created on 2016年11月10日

@author: bz866
'''
'''
Module introduction:
1. Class:
    a. Interval
    b. ValueError: handle exceptions
2. Functions:
    a. mergeable
    b. mergeIntervals
    c. mergeOverlapping
    d. insert   
'''


class interval(object):
    
    def __init__(self, s):
        '''
        Constructor
        '''
        self.s=s.strip()
        left_bound=['(','[']
        right_bound=[')',']']
        
        '''check if intervals are valid'''
        if s=='':
            raise ValueError('Invalid Input: Need an input')
        if self.s[0] not in left_bound or self.s[-1] not in right_bound:
            raise ValueError ('Invalid Input: bounds of interval must be [] or ()')
        try:
            self.comma_interval=list(map(int,self.s[1:-1].split(",")))
            if len(self.comma_interval) %2 != 0:
                raise ValueError('Invalid Input: Intervals must be input as valid brackets and value, like[a,b)')
            
            self.left_inclusive=self.comma_interval[0]-left_bound.index(self.s[0])+1
            self.right_inclusive=self.comma_interval[1]+right_bound.index(self.s[-1])-1
            if self.left_inclusive>self.right_inclusive:
                raise ValueError ('Invalid Input: empty intervals are not allowed')
                    
            self.left=(self.s[0],self.comma_interval[0])
            self.right=(self.s[-1],self.comma_interval[1])
            
        except ValueError: 
            raise ValueError('Invalid Input: Values must be integer')
        
    def __repr__(self, *args, **kwargs):
        ''' print intervals '''
        return str(self.left[0])+str(self.left[1])+","+str(self.right[1])+str(self.right[0])
    
    def __eq__(self,other):
        ''' 
        check if intervals are equal
        especially to the situation like (8,10] equals to [9,10]
         '''
        
        if isinstance(other, interval):
            return True
        else:
            return False
        
        if (self.left_inclusive==other.left_inclusive):
            if (self.right_inclusive==other.right_inclusive):
                return True
        else: 
            return False

def mergeable (int1, int2):
    ''' check if intervals can be merged '''
    if (int1.left_inclusive<int2.left_inclusive):
        if (int1.right_inclusive+1<int2.left_inclusive):
            return False
    elif (int2.left_inclusive<int1.left_inclusive): 
        if (int2.right_inclusive+1<int1.left_inclusive):
            return False
    else:
        return True

def mergeIntervals(int1, int2):
    '''
    Merge intervals which are overlapping or adjacent   
    '''
    

    '''check if intervals can be merged'''
    if mergeable(int1, int2)==False:
            raise ValueError ('Cannot Merge Intervals: Two intervals are not overlapped or adjacent')
        
    #Merge
    if int1.left_inclusive<=int2.left_inclusive:
        new_left=int1.left
    else: new_left=int2.left
    
    if int1.right_inclusive>=int2.right_inclusive:
        new_right=int1.right
    else: new_right=int2.right
    
    #Set merged interval as a new one
    newintervalstr=str(new_left[0])+str(new_left[1])+","+str(new_right[1])+str(new_right[0])
    return interval(newintervalstr)

def mergeOverlapping(intervals):
    '''
     Output merged intervals
    '''
    #sort interval list based on left bound
    intervals.sort(key= lambda x: x.left_inclusive)
    
    #merge all mergeable intervals
    result=[intervals[0]]
    for i in range(1, len(intervals)):
        if mergeable(result[-1],intervals[i]):
            result[-1]=mergeIntervals(result[-1],intervals[i])
        else:
            result.append(intervals[i])      
    return result

def insert(intervals, newint):
    '''
    insert the new interval if it can be done    
    '''
    intervals.append(newint)
    return mergeOverlapping(intervals)


        