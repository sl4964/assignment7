'''
Created on 2016.11.9

@author: xulei
'''

from exceptionClass import intervalException
'''An interesting thing is that if this sentence was written in the class, then it would say There is no such thing
named this.'''

class Interval:
    
    
    def __repr__(self):
        return "'{}' represents the number of {} through {}".format(self.name, self.lower, self.upper)

    def __init__(self, interval):
        self.name=interval
        if len(interval.split(','))==2:
            if ((interval[0]=='[' or interval[0]=='(') and (interval[-1]==')' or interval[-1]==']')):
                self.int_left=interval.split(',')[0]
                self.int_right=interval.split(',')[1]
            else:
                raise intervalException()
        else:
            raise intervalException()
        
        # detect if the interval is inclusive or exclusive
        if self.int_left[0]=='[':
            self.int_left_type= 'inclusive'
        else:
            self.int_left_type='exclusive'
        if self.int_right[-1]==']':
            self.int_right_type='inclusive'
        else:
            self.int_right_type='exclusive'
            
        #get the lower bound of the interval
        if self.int_left_type=='inclusive':
            self.lower=int(self.int_left[1:])
        else:
            self.lower=int(self.int_left[1:])+1
        #get the upper bound of the interval   
        if self.int_right_type == 'inclusive':
            self.upper=int(self.int_right[:-1])
        else:
            self.upper=int(self.int_right[:-1])-1
            
            
        if self.lower > self.upper:
            raise intervalException()
            
    
#print(Interval('[8,9]'))
#((interval[0]=='[' or interval[0]=='(') and (interval[1]==')' or interval[1]==']'))
#'[8,9]'[0]