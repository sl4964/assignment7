'''
This is the main module which allows users to realize merging the inserted intervals into original interval list.

NetID: xc965
'''

import re
import sys
import time
from interval import *

def user_insert_merge():
    """
    This function allow users to enter input interval values, sort and merge the intervals, \
    and insert a new interval to merge into the old interval list.
    """
    # welcome message
    print('Hello! Welcome to use this tool to merge overlapping integer intervals.')
    time.sleep(.5)

    # allow user to enter inputs as interval list
    while True:
        try:
            initial_input = input('Please enter a list of intervals with comma as separation.\nExample: [6,19), (10,33], [50,100)\nEnter \'q\' to quit.\nEnter here: ')
            # remove all whitespaces from the input string
            initial_input = initial_input.replace(' ', '')


            # allow user to quit the program
            if initial_input.lower() == 'q':
                return

            elif not re.match(r'[\[\(]-?\d+\,-?\d+[\]\)](\,[\[\(]-?\d+\,-?\d+[\]\)])*$', initial_input):
                raise InputFormatError

            else:
                # convert the initial input intervals into list
                # sort the intervals with increasing value of lower bounds
                # merge the overlapping intervals
                string_list = re.findall(r'[\[\(]-?\d+\,-?\d+[\]\)]', initial_input)
                intervals = mergeOverlapping(string_list)
                break

        # pop the invalid input from the interval list
        # ask user to enter again, if input:
        #     1) is empty
        #     2) is invalid (lower greater than upper)
        #     3) is in wrong format
        #     4) includes non-numeric values
        except EmptyInputError as x:
            intervals.pop()
            print(x)
        except InvalidIntervalError as x:
            intervals.pop()
            print(x)
        except FormatError as x:
            intervals.pop()
            print(x)
        except InputFormatError as x:
            print(x)



    while True:
        try:
            insert_int = input('Please enter an interval to insert: ')
            # remove all whitespaces from the input string
            insert_int = insert_int.replace(' ', '')

            # allow user to quit the program
            if insert_int.lower() == 'q':
                return

            stack = insert(intervals, insert_int)
            stack_string = ', '.join(stack)
            print(stack_string)

        except EmptyInputError as x:
            intervals.pop()
            print(x)
        except InvalidIntervalError as x:
            intervals.pop()
            print(x)
        except FormatError as x:
            intervals.pop()
            print(x)



if __name__ == '__main__':
    try:
        user_insert_merge()
    except EOFError:
        # Allow force quit command to quit the program while no input entered
        sys.exit()
    except KeyboardInterrupt:
        # Allow user to quit the program using ctrl+c command
        sys.exit()
