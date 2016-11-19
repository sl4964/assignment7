

class MergeError(Exception):
    def __str__(self):
        return 'Cannot merge intervals: gap between two intervals.'

class Interval():

    def __init__ (self, user_input):

 #       user_input=user_input.replace(' ','')
        
        ''' check the validity of the user input string,
        take input strings and transform to bounds and numbers.'''
        self.user_input=user_input.strip()

        lbd_sign =['(','[']
        rbd_sign =[')',']']
        if self.user_input[0] in lbd_sign and self.user_input[-1] in rbd_sign:
            self.lbd=user_input[0] #left bound symbol
            self.rbd=user_input[-1] #right bound symbol
            self.num_range=list(map(int,self.user_input[1:-1].split(','))) #the number range in list format
            self.lnum=self.num_range[0] #lower bound number 
            self.unum=self.num_range[-1] #upper bound number

            if len(self.num_range)!=2:
                raise ValueError("Please input valid bounds.")
            
            '''check validity mathematically.'''
        
            if  (self.lbd=='[' and self.rbd ==']' and self.lnum<=self.unum) or (self.lbd=='(' and self.rbd ==']' and self.lnum <self.unum) or (self.lbd=='[' and self.rbd ==')' and self.lnum <self.unum) or (self.lbd=='(' and self.rbd ==')' and self.lnum <self.unum -1):
                

                '''list of numbers the interval represents.'''
                self.bg_num=self.lnum #beginning number
                self.ed_num=self.unum #ending number

                if self.lbd=='(':
                    self.bg_num=self.lnum+1 
                if self.rbd==')':
                    self.ed_num=self.unum-1
                    
                self.lowerpt=(self.user_input[0],self.lnum)
                self.upperpt=(self.user_input[-1],self.unum)

            else:
                raise ValueError('Invalid number input.')
        else:
            raise ValueError('Invalid interval input.')



    def __repr__(self):
        return '%s%d,%d%s' % (self.lbd, self.lnum,self.unum,self.rbd)
    
'''The function is to check the validity of the input string in format. '''

'''def isValidInput(user_input):

    user_input=user_input.replace(' ','')
    

    if (user_input[0] in ['(','[']) and (user_input[-1] in [')',']']) and (',' in user_input):
         return True
    else:
         return False 
 '''      
        
'''Merge functions.'''
'''First check if two intervals are mergeable or not: we take the number list
of two intervals, if one's smallest number is small than the other's biggest number,
and its biggest number is bigger than the other's smallest, then they
are mergeable. 
'''
def IsMergeable (int1, int2):
    if (int1.bg_num< int2.bg_num and int1.ed_num+1<int2.bg_num) or (int2.bg_num<int1.bg_num and int2.ed_num+1<int1.bg_num):
        return False
    return True

'''If two intervals can be merged, we then merge them accordingly.'''
def mergeIntervals(int1, int2):
    result=""
    if IsMergeable (int1, int2) == False:
        raise MergeError

    if int1.bg_num>=int2.bg_num:
        new_lbd=int1.lowerpt
        
    else:
        new_lbd=int2.lowerpt
    if int1.ed_num>=int2.ed_num:
        new_rbd=int1.upperpt
    else:
        new_rbd=int1.upperpt

    newint=str(new_lbd[0])+str(new_lbd[1])+","+str(new_rbd[1])+str(new_rbd[0])
    return Interval(newint)        
 
'''We first sort the interval list by their lower bound number, then choose the first one 
as base and merge others with the former iteratedly if applicable.'''
def mergeOverlapping(intervals):
    if intervals ==0:
        return []

    intervals = sorted(intervals, key=lambda user_input: user_input.bg_num)
    result=[intervals[0]]

    for i in range (1, len(intervals)):
        if IsMergeable(intervals[i],result[-1]):
            result[-1]=mergeIntervals(intervals[i],result[-1])
        else:
            result.append(intervals[i])
    return result
    
    
    
'''the insert function is just to add one more interval to the list and redo the 
overlap function.'''
    
def insert (intervals, newint):
    
        intervals.append(newint)
        return mergeOverlapping(intervals)
        



