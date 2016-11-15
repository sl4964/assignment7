'''
Created on Nov 14, 2016

@author: muriel820
'''
class IntervalErrors(Exception):
    '''Superclass of Exceptions'''
    pass
class MissingBracket(Exception):
    def __str__(self):
        return 'Your input should state either inclusive or exclusive with [] or ().\n '
class CommaError(Exception):
    def __str__(self):
        return 'Your input should include only one comma, separating the lower bound and upper bound.\n '
class IntervalNoExistence(Exception):
    def __str__(self):
        return 'Your interval has a non positive size, please check\n'
#class Unmergeable(Exception):
#    def __str__(self):
#        return 'Your interval has a non positive size, please check\n'

class Interval(object):
    '''
    classdocs
    '''


    def __init__(self, interval_input):
        '''
        Constructor
        '''
        self.input = interval_input.replace(" ","")
        self.left_bracket = self.input[0]
        self.right_bracket = self.input[-1]
        if (self.left_bracket != '(' and self.left_bracket != '[' ) or (self.right_bracket != ')' and self.right_bracket != ']' ):
            raise MissingBracket()
        self.inner = self.input[1:-1].split(",")
        if len(self.inner) != 2 :
            raise CommaError()
        self.left_end = int(self.input[1:-1].split(",")[0])
        self.right_end = int(self.input[1:-1].split(",")[1])
        if self.left_bracket == '(':
            self.left_end = self.left_end + 1
        if self.right_bracket == ']':
            self.right_end += 1
        if self.left_end >= self.right_end:
            raise IntervalNoExistence()
        self.integerlist = []
        for x in range(self.left_end,self.right_end):
            self.integerlist.append(x)
    
    def __repr__(self):
        str =  '%s ' % self.input
        return str
    
    def __eq__(self, other):
        return (self.left_end == other.left_end and self.right_end == other.right_end)
    
def mergeIntervals(int1,int2):
    if (int1.left_end >int2.right_end or int2.left_end >int1.right_end):
        print('Unable to merge')
        return int1,int2
    else:
        left_end = min(int1.left_end, int2.left_end)
        right_end = max(int1.right_end, int2.right_end)
        strM =  '[ %d , %d )'% (left_end, right_end) 
        merged = Interval(strM)
        return merged

def mergeOverlapping(intervals):
    for int1 in intervals:
        for int2 in intervals:
            if mergeIntervals(int1, int2) != (int1, int2):
                intervals.remove(int1)
                intervals.remove(int2)
                intervals.append(mergeIntervals(int1,int2))
     