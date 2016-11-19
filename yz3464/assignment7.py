'''
Created on Nov 13, 2016

@author: twff
'''
import sys
from interval import *
import re


def main():
    while True:
        
        try:
            user_input = input("List of intervals? ")
            if user_input.lower() =='quit':
                break
        except EOFError:
            sys.exit(0)    
        break   
       
    intervals = []               
    user_input=user_input.replace(' ', '')
    strlist = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\)\]]+', user_input)
    
    for i in strlist:
        j = i.index(',')
        intervals.append(Interval(int(i[1:j]), int(i[j+1:-1])))
    intervals = mergeOverlapping(intervals)


    while True:
        try:
            user_input = input("interval? ")
            temp = user_input.index(',')
            try:
                if user_input == 'quit':
                    break 
                else:
                    intervals = insert(intervals, Interval(int(user_input[1:temp]), int(user_input[temp+1:-1])))
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