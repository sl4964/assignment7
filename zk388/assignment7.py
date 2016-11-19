'''
Created on Nov 14, 2016
#Assignmnet7
##DS-GA-1007

This module contains the main program
@author: Zahra Kadkhodaie
'''



from interval import *
from mergers import *

def main():
    '''This function prompts the user for a list of intervals, [-10,-7], (-4,1], [3,6), (8,12), [15,23] reads a string from the user, and creates a list 
    containing these intervals. Once this string has been read, the program continues prompting for intervals from 
    the user, insert the interval into the list, and display the list at the end of each operation.'''
    
    #Get a list of intervals from the user. This input MUST be a sequence of intervals seperated by ", " Otherwise the program 
    #won't understand it and will break down.
    interval_list = input('''List of intervals, sepparated by ", "? 
    "Example [-10,-7], (-4,1], [3,6), (8,12), [15,23]" :
    ''')
    
    interval_list = interval_list.split(', ')
    
    
    while True:
        NewInterval = input('Interval? ' )
        NewInterval = NewInterval.replace(' ', '')
        if NewInterval.lower() == 'quit':
            break
        else:
            try:
                checkPoint = interval(NewInterval) 
                #Error handling for the interval: if the user enters invalid interval, an arror will be raised.
                if checkPoint.intervalNumbers() == 'Invalid interval':
                    raise TypeError
            
            #If the input is not in the form of an interval, this message will be thrown.
            except IndexError:
                print('Invalid Input. This is not an interval.')
            
            #If the input is in the form of an interval, but the values are not integers, this message will be thrown.
            except ValueError:
                print('Invalid Input. This is not an interval.')
            
            #This one handles the errors manually raised by the program with respect to the requirement of a valid interval. 
            except TypeError:
                print('Invalid Interval. Fix the upper and lower bounds of the interval')
            
            #If all the above exceptions are skipped, merge will take place through the insert function.
            else:
                try:
                    interval_list = insert(interval_list , NewInterval)
                    
                except:
                    print('The interval list must conform to the suggested fromat. Re-run the program with a correct interval list.')
                    break
                

            #Show the merged intervals to the user.                
            print(interval_list, end= '')
    return interval_list

main()