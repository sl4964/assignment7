'''
Created on Fri Nov 11 12:51:28 2016

@author: wxy
'''

import sys
from class_interval import interval
 
if __name__=="__main__":
     
    while True:
        try:
            user_input = input("List of intervals? ")
            
            user_input = user_input.replace(" ","")
            interval_list = user_input.split(",")
            empty_list_interval=[]
            for i in range(0, len(interval_list), 2):
                empty_list_interval.append(interval(interval_list[i] + "," + interval_list[i+1]))
            new_list_interval = empty_list_interval
            print (new_list_interval)
            break
        
        except KeyboardInterrupt:
            sys.exit(1)
        except Exception:
            print ("Invalid list of intervals")
            pass
    
    while True:
        try:
            input_interval = input("Interval?")
            if input_interval == "quit":
                sys.exit(1)
                break
            else:
                input_interval = interval(input_interval)
                new_list_interval = interval.insert(new_list_interval, input_interval)
                print (new_list_interval)
        
        except KeyboardInterrupt:
            sys.exit(1)
        except Exception:
            print ("Invalid interval")