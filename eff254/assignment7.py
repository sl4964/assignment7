# -*- coding: utf-8 -*-

import Utils as ut
import sys

def InitialInterval():
    
    ''' Ask and pass the initial interval list '''
    
    userIntervals = str(input("List of intervals? "))
    userIntervals = [userIntervals]
    userIntervals = userIntervals[0].split(",")
    
    if len(userIntervals)<2:
        raise ut.invalidArrayException()
    
    secondList = []
    
    for item in range(0,len(userIntervals)):
        if item%2 == 0:
            myInterval = ut.interval(userIntervals[item].strip() + "," + userIntervals[item + 1].strip())
            secondList.append(myInterval)
            
    return secondList

IntervalList = None
# This piece of code came from http://stackoverflow.com/questions/4606919/in-python-try-until-no-error
while IntervalList is None:
    try:
        IntervalList = InitialInterval()
    except  ut.invalidArrayException:
        print("Sorry, invalid interval list")
        pass

IntervalList = ut.mergeOverlapping(IntervalList)   

Quit = None
while Quit is None:
    int1 = input("Interval? ")
    if int1 == "quit":
        Quit = True
    else: 
        try: 
            int1 = ut.interval(int1)
            IntervalList = ut.insert(IntervalList, int1)
            print(IntervalList)
        except  ut.invalidArrayException:
            print("Invalid interval")
            pass
        
if Quit == True:
    sys.exit()

""" A note: 
 The instructions for the homework were unclear and contradictory. 
 When ask to define the "insert()" functions, the instructions state that "[[1,2], (3,5), [6,7), (8,10], [12,16]" inserted with "[4,9]" should yield "[[1,2], (3,10], [12,16]]"
 But in the example below, when "[12,13)" is insterted into "[-10,-7], (-4,1], [3,12), [15,24]", it binds into "[-10,-7], (-4,1], [3,13), [15,24]"
 
 So, in one part of the instructions, it is said that we should treat (_,X) join [X,_) as separate, in other, as if we should join them. ([1,2] - (3,10] VS [3,12) - [12,13)
 
 This code joins those intervals into a single one. 
"""

