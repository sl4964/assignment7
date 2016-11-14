'''
Created on Nov 14, 2016

@author: sunevan
'''

from interval import * 

import sys 

print ("""Instruction: "[1,3]" is a valid interval. ["[1,2]", "(3,5)"] is a valid interval list. "quit" to quit the program.""")

print ("""Notes: In some cases,(3,7) will be represented as [4,6]""")

program_interval_list = []
      
    
while len(program_interval_list)== 0: 
    user_input = eval(input("List of intervals?")) 
    if user_input == "quit":        
        break
    else:         
        program_interval_list = mergeOverlapping(user_input)

while True: 
    try:
        user_input = eval(input("Interval?"))
        if user_input == "quit":
            
            break
            
        program_interval_list = insert(program_interval_list,user_input)
        print (program_interval_list)
    except Exception:
        print ("Invalid interval")

if __name__ == '__main__':

    pass