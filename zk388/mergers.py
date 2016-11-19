'''
Created on Nov 14, 2016
This module contains all the functions that use interval class
Assignmnet7
DS-GA-1007
@author: Zahra Kadkhodaie
'''

from interval import *


def by_lower(interv):
    '''This will be used to sort the interval lists.
    This function returns the interger value of the lower bound of an interval'''
    lower , upper  = interv.strip('[],()').split(',')
    return int(lower)
    
    
    
def mergeIntervals(int1, int2):
    '''Takes two intervals. If the intervals overlap or are adjacent, returns
    a merged interval. If the intervals cannot be merged, an exception should be thrown.'''
    
    #First sort the intervals based on their lower bounds
    int1 , int2 = sorted((int1, int2), key=by_lower)
  
    #Turns the inputs into interval class objects
    int1 = interval(int1) 
    int2 = interval(int2)
    
    #If the input intervals are not valid print out an error message.
    if int1.intervalNumbers() == 'Invalid interval' or int2.intervalNumbers() == 'Invalid interval':
        return('Invalid interval')

    #If the input intervals are valid continue.
    else:
        #Find out if the two interval are overlapping not.
        if list(set(int1.intervalNumbers()) & set(int2.intervalNumbers())) == []:

            #If they are not overlapping, find out if they are adjacent or not
            if max(int1.intervalNumbers()) + 1 == min(int2.intervalNumbers()):

                #If they are adjacent, merge them
                return int1.opening + str(int1.lower) + ',' + str(int2.upper) + int2.closing

            #If they are not overlapping or adjacent, return the following message
            else:
                return 'Error: The two lists cannot be merged'

        #If they are overlapping, merge them. Using conditionals to form the right interval.
        else:    
            if max(int1.intervalNumbers()) > max(int2.intervalNumbers()):
                if int1.lower == int2.lower and int2.opening == '[':
                    return int2.opening + str(int1.lower) + ',' + str(int1.upper) + int1.closing
                else:
                    return int1.opening + str(int1.lower) + ',' + str(int1.upper) + int1.closing
            
            elif max(int1.intervalNumbers()) < max(int2.intervalNumbers()):
                if int1.lower == int2.lower and int2.opening == '[':
                    return int2.opening + str(int1.lower) + ',' + str(int2.upper) + int2.closing
                else:
                    return int1.opening + str(int1.lower) + ',' + str(int2.upper) + int2.closing
            else:
                if int1.upper >= int2.upper:
                    return int1.opening + str(int1.lower) + ',' + str(int1.upper) + int1.closing
                else:
                    return int1.opening + str(int1.lower) + ',' + str(int2.upper) + int2.closing





                    
                    
                    
def mergeOverlapping(intervals): 
    '''It takes a list of intervals and merges all overlapping or adjacent intervals.'''
    
    #First of all, check if all the intervals meet the requirements.
    try:
        for interv in intervals:
            if interval(interv).intervalNumbers() == 'Invalid interval':
                raise TypeError
    except TypeError:
        print('Invalid Interval')
    
    #If all the intervals are valid, then continue.
    else:
        #First sort the intervals based on their lower bounds
        intervals = sorted(intervals, key = by_lower)                    
        
        #Take the first interval in the list as mergedSoFar
        mergedSoFar = [intervals[0]]
        
        #Now, for all the intervals do the followings.
        for j in range(len(intervals)):
            
            #If the mergedSoFar and the next interval are overlapping, merge them.
            if list(set(interval(mergedSoFar[-1]).intervalNumbers()) & set(interval(intervals[j]).intervalNumbers())) != []:
                mergedSoFar[-1] = mergeIntervals( mergedSoFar[-1], intervals[j])
            
            #If the mergedSoFar and the next interval are not overlapping, check if they are adjacent.
            else:
                #If the mergedSoFar and the next interval are adjacent, merge them
                if max(interval(mergedSoFar[-1]).intervalNumbers()) + 1 == min(interval(intervals[j]).intervalNumbers()):
                    mergedSoFar[-1] = mergeIntervals(mergedSoFar[-1], intervals[j])
                
                #If the mergedSoFar and the interval are not overlapping nor adjacent, start a new interval in the mergedSoFar.
                else:
                    mergedSoFar.append(intervals[j])
        
        return mergedSoFar
 
 
 
 
def insert(intervals, newint):
    '''It takes two arguments: a list of non-overlapping intervals (i.e. any adjacent or overlapping intervals have been 
    merged); and a single interval. The function should insert newint into intervals, merging the result if necessary. '''
    
    #First add the newint into the interval list.
    intervals.append(newint)
    
    #Then use the mergeOverLapping function to do the rest. 
    return mergeOverlapping(intervals)
