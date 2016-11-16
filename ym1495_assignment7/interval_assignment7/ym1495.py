'''
Created on Nov 15, 2016

@author: muriel820
'''
import sys
from interval_assignment7.interval import *

def main():
    user_input = []    
    user_input = input("Please enter a list of intervals separated by ',':")
    if user_input == "quit":
        pass
            
    else:
        half_interval = user_input.split(',')
#        if len(half_interval)/2 !=0:
#            raise IntervalErrors('Please check your input ')
        intervals = []
        for i in range(0, len(half_interval),2):
            newInt = Interval('%s,%s'%(half_interval[i],half_interval[i+1]))
            insert(intervals, newInt)
    
    while True:
        try:
            user_input_int = input("Interval? ")
            if "quit" in user_input_int:
                pass
            new_int = Interval(user_input_int)
            new_intervals = insert(intervals, new_int)
            print (new_intervals)
 
        except IntervalErrors:
            print("Invalid interval, please try again")
            continue
        
            
        
#    except ValueError:
 #       print('/')
if __name__ == '__main__':
    main()