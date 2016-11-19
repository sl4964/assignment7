'''
Created on Nov 14, 2016

@author: Yovela
'''
from interval import *
if __name__ == '__main__':

    # read the input of a string, and transforming it into a interval list

    while True:

        try:
            input_string = input("List of intervals?")
            input_string_list = input_string.split(', ')
            interval_list = []
            for input_string in input_string_list:
                interval_list.append(interval(input_string))
            break

        except InputError:
            print("Invalid Interval")

    # read a new interval, if valid input, do the merge; if invalid input, raise an error

    while True:
        try:
            new_int = input("Interval?")
            if new_int.lower() == 'quit':
                break

            new_interval = interval(new_int)

        except InputError:
            print("Invalid Interval")
            continue

        merged_interval_list = insert(interval_list, new_interval)
        interval_list = merged_interval_list
        print(merged_interval_list)
