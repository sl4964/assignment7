'''
Created on Nov 15, 2016

@author: muriel820
'''
import sys
from interval_assignment7.interval import *

def main():
    '''
    As integers and intervals are both separated by comma,
    I split them into pieces and recombine together to make intervals
    if exceptions occur, it will ask for a new input
    and break when get one interval list correctly
    '''
    while True:
        try:
            user_input = []    
            user_input = input("Please enter a list of intervals separated by ',':")
            if user_input == "quit":
                sys.exit(0)
            else:
                half_interval = user_input.split(',')
                intervals = []
                for i in range(0, len(half_interval),2):
                    newInt = Interval('%s,%s'%(half_interval[i],half_interval[i+1]))
                    insert(intervals, newInt)
                print(intervals)
                break
        except InputNotString and MissingBracket and CommaError and IntervalNoExistence and ValueError:
            print("Invalid input, please try again")
    
    '''
    keep asking for new interval input until told to quit
    '''
    while True:
        try:
            user_input_int = input("Interval? ")
            if "quit" in user_input_int:
                sys.exit(0)
            new_int = Interval(user_input_int)
            new_intervals = insert(intervals, new_int)
            print (new_intervals)
 
        except InputNotString and MissingBracket and CommaError and IntervalNoExistence and ValueError:
            print("Invalid interval, please try again")
            continue

        
if __name__ == '__main__':
    main()