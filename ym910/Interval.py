

class MergeError(Exception):
    def __str__(self):
        return 'Cannot merge intervals: gap between two intervals.'

class Interval():

    def __init__ (self, user_input):

        user_input=user_input.replace(' ','')
        
        ''' check the validity of the user input string,
        take input strings and transform to bounds and numbers.'''
        
        if (user_input[0] in ['(','[']) and (user_input[-1] in [')',']']) and (',' in user_input):
            lbd=user_input[0] #left bound symbol
            rbd=user_input[-1] #right bound symbol
            lnum=int(user_input[1:-1].split(',')[0]) #lower bound number 
            unum=int(user_input[1:-1].split(',')[-1]) #upper bound number
            
            '''check validity mathematically.'''
        
            if  (lbd=='[' and rbd ==']' and lnum<=unum) or (lbd=='(' and rbd ==']' and lnum <unum) or (lbd=='[' and rbd ==')' and lnum <unum) or (lbd=='(' and rbd ==')' and lnum <unum -1):
                self.lbd=lbd
                self.rbd=rbd
                self.lnum=lnum
                self.unum=unum

                '''list of numbers the interval represents.'''
                beginning_num=lnum
                ending_num=unum

                if lbd=='(':
                    beginning_num=lnum+1
                if rbd==')':
                    ending_num=unum-1
                    
                self.list=range(beginning_num,ending_num+1)

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
    if int1.list[-1]+1 < int2.list[0] or int1.list[0] > int2.list[-1]+1:
        return False
    return True

'''If two intervals can be merged, we then merge them accordingly.'''
def mergeIntervals(int1, int2):
    result=""
    if IsMergeable (int1, int2) == False:
        raise MergeError

    if (int1.list[0]<=int2.list[0] and int1.lnum <= int2.lnum):
        result=result+int1.lbd+str(int1.lnum)+','
    else:
        result=result+int2.lbd+str(int2.lnum)+','
    if (int1.list[-1]>=int2.list[-1] and int1.lnum >= int2.lnum):
        result=result+str(int1.lnum)+int1.lbd
    else:
        result=result+str(int2.lnum)+int2.lbd
           
 
'''We first sort the interval list by their lower bound number, then choose the first one 
as base and merge others with the former iteratedly if applicable.'''
def mergeOverlapping(intervals):
    if intervals ==0:
        return []

    intervals = sorted(intervals, key=lambda user_input: user_input.lnum)
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
        



