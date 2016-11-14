'''
Created on Nov 14, 2016

@author: Caroline
'''
from hw7_package import *

import functions as m
import interval_class as i

def compile_user_input():
    '''
    (1) Asks user for a list of intervals
    (2) Parses and merges that input
    (3) Asks user for one interval at a time to insert and merge
    '''
    
    user_input = ''
    successful_first_list = 0
    intervals = []
    merged_intervals = []
    parsed_input = []
    
    while successful_first_list == 0 and user_input != 'quit': #if user hasn't yet input a valid interval list or quit
        user_input = str(input("List of intervals? "))
        if user_input == 'quit':
            pass
        else:
            try:
                parsed_input = m.parse_interval_input(user_input)
                try:
                    intervals = m.Make_intervals(parsed_input)
                    try:
                        if intervals: #only try to merge intervals if you made valid intervals
                            merged_intervals = m.mergeOverlapping(intervals)
                            successful_first_list = 1
                    except:
                        if intervals: #only print merge errors if you made the intervals
                            print('Unable to merge intervals in the input')
                except AssertionError as err:
                    print({0}.format(err))
            except ValueError as err:
                print('Could not parse input. Error details: {0}'.format(err))
    else:
    
        newint = ''

        while newint != 'quit' and user_input != 'quit':
            newint = str(input("Interval? "))
            if newint == 'quit':
                break
            else:
                try:
                    new_interval = i.Interval(newint)
                    inserted_intervals = m.insert(merged_intervals, new_interval)
                    print(inserted_intervals)
                except AssertionError:
                    print('Invalid interval')

compile_user_input()