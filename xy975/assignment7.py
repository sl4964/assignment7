from interval import *
import sys

def main():
    # Run this loop to check out whether the input intervals is valid. 
    while True:
        intervals = input('List of Intervals?')
        if intervals == 'quit':
            sys.exit(0)
        else:
            # If the input is invalid, turn to the next step
            try:
                intervals = intervals.split(', ')
                intervals = mergeOverlapping(intervals)
                break
            # If the input is invalid, try another intervals
            except ValueError:
                print('Invalid Intervals.')
                
    # Run this loop to merge the intervals with a new interval. 
    while True:
        newint = input('Interval?')
        if newint == 'quit':
            break
        else:
            try:
                interval(newint)
                intervals = intervals.split(', ')
                intervals = insert(intervals, newint)
                print(intervals)
            except ValueError:
                print('Invalid Interval.')
                
    sys.exit(0)
    
if __name__ == '__main__':
  main()
