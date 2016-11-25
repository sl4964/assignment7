'''
This module defines errors
@author: ShashaLin
'''
class Errors(Exception):
    pass

class InputError(Errors):
    def __init__(self, message):
        self.message = message


class MergeError(Errors):
    def __init__(self):
        self.message = 'The intervals cannot be merged: they are neither overlapping nor adjacent.'
    