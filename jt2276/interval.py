'''
Interval Class 
@author: jonathanatoy
'''

class interval(object):
    '''
    Class represents an interval of integers, i.e. [1,4) represents {1,2,3}
    '''


    def __init__(self, lower_bound, upper_bound, exclusive_lower, exclusive_upper):
        '''
        Constructor for interval class
        inputs:
                lower_bound: integer representing lower bound of interval
                upper_bound: integer representing upper bound of interval
                exclusive_lower: boolean representing whether lower bound is exclusive
                exclusive_upper: boolean representing whether upper bound is exclusive
                
        inputs must be specified so that at least one integer falls within the interval
        '''
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.exclusive_lower = exclusive_lower
        self.exclusive_upper = exclusive_upper
        
        if (self.lower_bound >= self.upper_bound - 1) & (self.exclusive_lower + self.exclusive_upper == 2):
            raise IntervalException()
        if (self.lower_bound >= self.upper_bound) & (self.exclusive_lower + self.exclusive_upper == 1):
            raise IntervalException()
        if (self.lower_bound > self.upper_bound) & (self.exclusive_lower + self.exclusive_upper == 0):
            raise IntervalException()
        

    def __repr__(self): # overloads printing
        if self.exclusive_lower == True:
            l_bound = '('
        else:
            l_bound = '['
        
        if self.exclusive_upper == True:
            r_bound = ')'
        else:
            r_bound = ']'
        out = l_bound + str(self.lower_bound) + ',' + str(self.upper_bound) + r_bound
        return out