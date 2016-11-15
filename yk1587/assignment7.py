import sys
from interval import *

def promptInput():
    '''prompt the user for a list of intervals, reads a string from the user and creates a list containing these intervals.'''
    userInput = input('List of intervals? \n')
    intlist = []
    for int in list(userInput.split(', ')):
        intlist.append(str(interval(int)))
        intlist = mergeOverlapping(intlist)

#continue prompting for intervals from the user, insert the interval into the list and display it at the end of each operation.
    while True: 
        try:
            newInput = input('Intervals? \n')
            if newInput == 'quit':
                break
            else: 
                newint = str(interval(newInput))
                print(insert(intlist, newint))
        except ValueError:
            print('Invalid interval.')
    

if __name__ == '__main__':
    promptInput()