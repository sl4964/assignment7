'''
Created on Nov 14, 2016

@author: ChuanYa Hsu
'''

import sys
import signal
from Interval import *

def main():
    
    """
    function main:
        Taking a list of intervals as inputs and asking users to 
        input intervals. Then try to merge it into the list of the 
        interval.
    """
    
    """ Let users input a list of intervals and handle exceptions """
    while True:
        try:
            inputlist = input("List of intervals?")
            if isIntervalListValid(inputlist):
                break
            else:
                raise InvalidIntervals('At least one interval is invalid')
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)
            
    #split the input list of intervals by regular expression.
    inputlist = inputlist.replace(' ', '')
    strlist = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\)\]]+', inputlist)
    interval_list = []
    
    #making a non=overlap interval list 'interval_list' by calling the mergeOverlapping function. 
    for item in strlist:
        interval_list.append(interval(item))
    interval_list = mergeOverlapping(interval_list)
    
    #let users input an interval and insert this interval to non-overlap interval list, and handle exceptions.
    while True:
        try:
            input_string = input("Interval?")
            try:
                if input_string == 'quit':
                    return
                else:
                    interval_list = insert(interval_list, interval(input_string))
                    print(interval_list)
            except:
                print('Invalid interval')
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)
            
    
if __name__ == '__main__':
    main()
            
