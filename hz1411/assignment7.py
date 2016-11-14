import exceptions
from interval import *
from functions import *


interval_input = input('List of Intervals?')
intervals = [] 
for i in list(interval_input.split(', ')):  #read input
    intervals.append(interval(i))

while True:
    newint_input = input('Interval?')
    if newint_input == 'quit':
        break
    else:
        try:
            newint = interval(newint_input)
            insert(intervals,newint) 
            intervals = mergeOverlapping(intervals)
            print(intervals)
        except InvalidInterval:
            print('Invalid Interval')