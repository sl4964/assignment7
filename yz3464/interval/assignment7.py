'''
Created on Nov 13, 2016

@author: twff
'''
import sys
from interval import *
import re

intervals = []
def main():
    while True:
        try:
            user_input = input("List of intervals? ")
            if user_input.lower() =='quit':
                break
        except EOFError:
            sys.exit(0)    
        except ValueError as e:
            print(str(e))
        
                    
    user_input=user_input.replace(' ', '')
    strlist = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\)\]]+', user_input)
    
    for i in strlist:
        intervals.append(Interval(i))
    intervals = mergeOverlapping(intervals)

    #let users input an interval and insert this interval to non-overlap interval list, and handle exceptions.
    while True:
        try:
            user_input = input("interval? ")
            try:
                if user_input == 'quit':
                    break 
                else:
                    intervals = insert(intervals, Interval(user_input))
                    print(intervals)
            except:
                print('Invalid interval')
        except EOFError:
            sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(0)
        except ValueError as e:
            print(str(e))

if __name__ == '__main__':
    main()  