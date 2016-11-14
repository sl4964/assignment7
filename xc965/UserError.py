'''
This module defines user's self-defined exceptions.

NetID: xc965
'''

# Error: Input is empty.
class EmptyInputError(Exception):
    def __str__(self):
        return 'Input Error! Empty input.\n'


# Error: Input does not match interval format.
class FormatError(Exception):
    def __str__(self):
        return 'Format Error! Each interval should include two numbers with one comma as separation.\n'


# Error: Main module input does not match interval format.
class InputFormatError(Exception):
    def __str__(self):
        return 'Input Format Error! Each valid interval should include two numbers with one comma as separation.\n'


# Error: Interval is invalid.
class InvalidIntervalError(Exception):
    def __str__(self):
        return 'Interval Error! The lower bound should be less than or equal to the upper.\n'


# Error: Intervals have no overlaps
class NoOverlapError(Exception):
    def __str__(self):
        return 'Input interval values have no overlaps!\n'
