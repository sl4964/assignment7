'''
Created on 2016.11.13.

@author: xulei
'''

class mergeException(Exception):
    def __str__(self):
        return 'These two intervals cannot be merged'
    
class intervalException(Exception):
    def __str__(self):
        return 'The interval is invalid'