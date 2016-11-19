'''
Created on Nov 14, 2016

@author: Caroline
'''
class Interval():
    def __init__(self, interval):
        assert isinstance(interval, str), "input is not a string"
        assert interval.find(',') != -1, "need a comma to divide lower and upper bounds"
        assert interval[0] in ('(','['), "interval must start with ( or [ to signify inclusive or exclusive lower bound"
        assert interval[-1] in (')', ']'), "interval must finish with ) or ] to signify inclusive or exclusive upper bound"
        assert interval[1:interval.index(',')].lstrip(' ').lstrip('-').isdigit(), "lower bound is not one integer"
        assert interval[interval.index(',') + 1:len(interval)-1].lstrip(' ').lstrip('-').isdigit(), "upper bound is not one integer"
        self.interval = interval
        self.lower = int(interval[1:interval.index(',')])
        self.upper = int(interval[interval.index(',') + 1:len(interval)-1])
        self.lower_inclusive = self.lower + 1*(interval[0] == '(')
        self.upper_inclusive = self.upper - 1*(interval[-1] == ')')
        assert self.lower_inclusive <= self.upper_inclusive, "lower limit must be less than upper limit"
        self.interval_list = list(range(self.lower_inclusive, self.upper_inclusive+1))
    
    def __repr__(self):
        return '%s' % (self.interval)