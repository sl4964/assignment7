'''
Created on Nov 11, 2016

@author: Fanglin Chen
'''
from interval import *
from merge import *

while True:
    try:
        intervals_initial = input('List of intervals? \n> ')   # Prompt the user for a list of intervals
        if intervals_initial == 'quit': 
            break
        else:
            # Create a list containing these intervals
            intervals_part = [part.strip() for part in intervals_initial.split(',')]   # Reference: http://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python
            if len(intervals_part) % 2 == 1:
                raise InputError('Invalid input')
            intervals = []
            for i in range(0, len(intervals_part), 2):
                intervals.append(interval(intervals_part[i] + ', ' + intervals_part[i+1]))
            break
    except InputError:
        print('Invalid input')
    except KeyboardInterrupt:
        print('You have hit the interrupt key')
        

def new():
    '''
    The function 
    '''
    while True:
        try:
            interval_new = input('Interval? \n> ')   # Prompt the user for new intervals
            if interval_new == 'quit':
                break
            else:
                # Insert the interval into the list, and display the list at the end of each operation
                newint = interval(interval_new)
                print(str(insert(intervals, newint))[1:-1])
        except InputError:
            print('Invalid interval')
        except KeyboardInterrupt:
            print('You have hit the interrupt key')
        

if __name__ == '__main__':
    new()
