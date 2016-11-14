'''
Created on Nov 14, 2016

@author: sj238
'''
import re
import sys
import time
from interval import *


if __name__ == '__main__':
    while True:
        try:
            get_input = input('List of intervals?') # ask for input
            get_input = get_input.strip()#get rid of white space
            if get_input.lower() == 'quit':
                return 
            elif not re.match(r'[\[\(]-?\d+\,-?\d+[\]\)](\,[\[\(]-?\d+\,-?\d+[\]\)])*$', get_input):
                #input should match valid interval format
                raise ValueError('Input is not valid')
            else:
                #put the input from user in a list
                interval_list = re.findall(r'[\[\(]-?\d+\,-?\d+[\]\)]', get_input)
                intervals = mergeOverlapping(interval_list)
            except ValueError as e:
                print(e)
            
    while True:
        try:
            get_interval = input('Interval?')# ask for input
            get_interval = get_input.strip()#get rid of white space
            if get_interval.lower() == 'quit':
                return 
            merged = insert(intervals, get_interval)
            merged_interval = ', '.join(merged)
            print(merged_interval)
        except ValueError as e:
            print(str(e))
            
            
            
            
    except EOFError:
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()      
            
            
    
    