from exceptions import *

class interval:
#read interval string from input and check if it is valid
    def __init__(self,interval):
        if interval[0]!='[' and interval[0]!='(':
            raise InvalidInterval
        if interval[-1]!=')' and interval[-1] != ']':
            raise InvalidInterval
            
        self.bound_lower = interval[0]
        self.bound_upper = interval[-1]
        
        try:
            self.lower = int(interval[1:-1].split(',')[0])
        except:
            raise InvalidInterval
        try:
            self.upper = int(interval[1:-1].split(',')[1])
        except:
            raise InvalidInterval
        # check if bounds meet requirements
        if self.bound_lower =='[':
            real_lower = self.lower
        else:
            real_lower = self.lower+1
        if self.bound_upper == ']':
            real_upper = self.upper
        else:
            real_upper = self.upper-1
        if real_lower > real_upper:
            raise InvalidInterval
        self.interval = interval
    def __repr__(self):
        return self.interval

