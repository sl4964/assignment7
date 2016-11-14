'''
Created on Nov 13, 2016

@author: Jingyi Su (js5991)
'''
from Interval.Interval import *
import sys

def interface():
    #Asking for the initial list of intervals
    while True:
        try:
            initial_list=input("List of intervals?")      
            
            if initial_list.lower()=='quit':
                sys.exit(0)
        
            interval_list=initial_list.split(", ")
            intervals=[]
            for interval_item in interval_list:
                intervals.append(interval(interval_item))
            break
        except ValueError as msg:
            print(msg)
        except EOFError:
            sys.exit(0)

    
    #Asking for intervals to insert in the interval one by one  
    while True:
        try:
            next_interval=input('Interval?')
            if next_interval=='quit':
                break
            new_interval_list=insert(intervals,interval(next_interval))
            print(str(new_interval_list)[1:-1])
        except ValueError as msg:
            print(str(msg))
        except EOFError:
            sys.exit(0)
        
if __name__ == '__main__':
    interface()


