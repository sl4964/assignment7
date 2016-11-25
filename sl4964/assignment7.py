'''
This is the main program that interacts with the user.

@author: ShashaLin
'''
from funcs import interval, mergeIntervals, mergeOverlapping, insert
from Errors import InputError, MergeError
i = 0
while i < 1:
    interv = input('List of intervals?')
    
    try: 
        intv = []
        inter2 = interv.split(', ')
        for i in inter2:
            intv.append(interval(i))
        i =+ 1
    except:
        print('List of intervals does not follow the right format. Make sure every item is a correct interval, and each item is joined by a comma and space')
        
inp = 0 
 
    

while inp != 'quit':
    inp = input('Interval?')
    if inp != 'quit':
        try:
            interval(inp)
            interv = insert(interv, inp)
            print(interv)
        
        except InputError:
            print('Interval of incorrect format. Input has to include two numbers, with a comma and no space in between.')
    
   

