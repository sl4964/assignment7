'''
Created on Nov 11, 2016

@author: Fanglin Chen
'''

class interval(object):
    '''
    The interval class represents the range of integers between a lower bound and an upper bound. 
    Either of the bounds of an interval can be inclusive or “exclusive and can be positive or negative.

    '''
    def __init__(self, interval):
        '''
        The constructor takes a string representation of the interval, 
        and ensures that the interval in this string includes at least one integer.
        It defines instance variables lower_inclusive, upper_inclusive, 
        lower, upper, lower_integer and upper_integer.
        '''
        # Check the first and last character of the string
        if interval == '':
            raise InputError('Invalid input')
        if interval[0] == '[':
            self.lower_inclusive = True
        elif interval[0] == '(':
            self.lower_inclusive = False
        else:
            raise InputError('Invalid input')
        
        if interval[-1] == ']':
            self.upper_inclusive = True
        elif interval[-1] == ')':
            self.upper_inclusive = False
        else:
            raise InputError('Invalid input')
        
        # Transform the middle characters of the string into a list
        try:
            values = eval(interval[1:-1])
        except:
            raise InputError('Invalid input')
        
        # Check the length of the list
        if len(values) != 2:
            raise InputError('Invalid input')
        
        self.lower = values[0]
        self.upper = values[1]
        
        # Check that both bounds are integers
        if type(self.lower) != int or type(self.upper) != int:
            raise InputError('Invalid input')
        
        self.lower_integer = self.lower + (1 - self.lower_inclusive)
        self.upper_integer = self.upper - (1 - self.upper_inclusive)
        
        # Check that the interval includes at least one integer
        if self.lower_integer > self.upper_integer:
            raise InputError('Invalid input')
        
    def __repr__(self):
        '''
        The function prints the interval using “[ ]” for inclusive bounds or “( )” for exclusive bounds.
        '''
        if self.lower_inclusive:
            if self.upper_inclusive:
                return "[" + str(self.lower) + ", " + str(self.upper) + "]"
            else:
                return "[" + str(self.lower) + ", " + str(self.upper) + ")"
        else:
            if self.upper_inclusive:
                return "(" + str(self.lower) + ", " + str(self.upper) + "]"
            else:
                return "(" + str(self.lower) + ", " + str(self.upper) + ")"
            
    def __eq__(self, other):
        '''
        The function compares two instances of the interval class for equality. 
        Reference: http://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes-in-python
        '''
        return self.__dict__ == other.__dict__


class InputError(Exception):
    '''
    Exception raised for errors in the input.
    '''
    def __str__(self):
        return 'Invalid input'

    

        