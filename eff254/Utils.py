# -*- coding: utf-8 -*-
import numpy as np

class invalidArrayException(Exception):
    def __str__(self):
        return "Invalid interval"

class interval():
    
    def __init__(self, StringRepresentation):
        self.StringRepresentation = StringRepresentation
        
        self.lowType = self.StringRepresentation[0]
        
        self.highType = self.StringRepresentation[len(self.StringRepresentation)-1] 
        
        if self.lowType != "[" and self.lowType != "(":
            raise invalidArrayException()
            
        if self.highType != "]" and self.highType != ")":
            raise invalidArrayException()    
                
        if self.lowType=="[":
            self.isLowInclusive = True
        elif self.lowType=="(":
            self.isLowInclusive = False
            
        if self.highType=="]":
            self.isHighInclusive = True
        elif self.highType==")":
            self.isHighInclusive = False    
            
        self.lowLimit = int(self.StringRepresentation[1 : self.StringRepresentation.index(",")])
        self.highLimit = int(self.StringRepresentation[self.StringRepresentation.index(",") + 1 : self.StringRepresentation.index(self.highType)])
 
        if self.lowLimit>self.highLimit:
            raise invalidArrayException() 
        
        if self.lowLimit == self.highLimit - 1:
            if (self.isLowInclusive == False and self.isHighInclusive == False):
                raise invalidArrayException() 
                        
        if self.isLowInclusive:
            if self.isHighInclusive:
                self.sequenceArray = np.arange(self.lowLimit, self.highLimit + 1)
            else: 
                self.sequenceArray = np.arange(self.lowLimit, self.highLimit)
        else:
            if self.isHighInclusive:
                self.sequenceArray = np.arange(self.lowLimit + 1, self.highLimit + 1)
            else: 
                self.sequenceArray = np.arange(self.lowLimit + 1, self.highLimit) 
    def __repr__(self):
        string = self.lowType + str(self.lowLimit) + " , " + str(self.highLimit) + self.highType
        return string
    
class mergeIntervalsException(Exception):
    def __str__(self):
        return "Empty interval in mergeIntervals()"
    
def mergeIntervals(int1, int2) :
    arrayIntersection = np.intersect1d(int1.sequenceArray, int2.sequenceArray, assume_unique=True)
    
    if (arrayIntersection.size > 0):
        firstElementMergedArray = arrayIntersection[0]
        lastElementMergedArray = arrayIntersection[len(arrayIntersection) - 1]       
        
        # Match the parethesis, if one has "(" and touches and the other one doesn't touches, give preference to "(". Otherwise, use "[": 
        
        typeLowParenthesis = "[" # Default is inclusive set.        
        if int1.isLowInclusive==False and firstElementMergedArray==int1.lowLimit + 1:
            if int2.isLowInclusive==False or (int2.isLowInclusive==True and firstElementMergedArray!=int2.lowLimit):
                typeLowParenthesis = "("
        
        if int2.isLowInclusive==False and firstElementMergedArray==int2.lowLimit + 1:
            if int1.isLowInclusive==False or (int1.isLowInclusive==True and firstElementMergedArray!=int1.lowLimit):
                typeLowParenthesis = "("
                
        typeHighParenthesis = "]" # Default is inclusive set.        
        if int1.isHighInclusive==False and lastElementMergedArray==int1.highLimit - 1:
            if int2.isHighInclusive==False or (int2.isHighInclusive==True and lastElementMergedArray!=int2.highLimit):
                typeHighParenthesis = ")"
        
        if int2.isHighInclusive==False and lastElementMergedArray==int2.highLimit - 1:
            if int1.isHighInclusive==False or (int1.isHighInclusive==True and lastElementMergedArray!=int1.highLimit):
                typeHighParenthesis = ")"          
       
        # Adjust the interval according to parenthesis:
        if typeLowParenthesis == "(":
            firstElementMergedArray = firstElementMergedArray - 1
            
        if typeHighParenthesis == ")":    
            lastElementMergedArray = lastElementMergedArray + 1
        
        StringRepresentationMergedArray = typeLowParenthesis +  str(firstElementMergedArray) + " , " + str(lastElementMergedArray) + typeHighParenthesis        
        intevalMergedArray = interval(StringRepresentationMergedArray)
        
        return intevalMergedArray
        
    else:
        
        # This is set to include weird cases when the array is zero but limits touch.  For example (_,X) and [X,_) or 
        # It returns an interval with [X,X]
        
        intervals = [int1, int2]
        intervals.sort(key = lambda interval:interval.sequenceArray[0])
        if (intervals[0].highLimit == intervals[1].lowLimit):
            if (intervals[0].isHighInclusive == True and intervals[1].isLowInclusive == False) or (intervals[0].isHighInclusive == False and intervals[1].isLowInclusive == True):
                StringRepresentationMergedArray = "[" +  str(intervals[0].highLimit) + " , " + str(intervals[0].highLimit) + "]"  
                intevalMergedArray = interval(StringRepresentationMergedArray)
                
                return intevalMergedArray
            
        elif (intervals[0].highLimit == intervals[1].lowLimit - 1):
            if (intervals[0].isHighInclusive == True) and (intervals[1].isHighInclusive == True):
                StringRepresentationMergedArray = "[" +  str(intervals[0].highLimit) + " , " + str(intervals[1].lowLimit) + "]"      
                intevalMergedArray = interval(StringRepresentationMergedArray)
                
                return intevalMergedArray
            
        else:
            raise mergeIntervalsException()

def mergeOverlapping(intervals):
    
    intervals.sort(key = lambda interval:interval.sequenceArray[0])
    
    intervalsLen = len(intervals)
    
    myBaseIntervalList = [intervals[0]]
    
    for x in range(1,intervalsLen):
        
        try:
            mergeIntervals(myBaseIntervalList[len(myBaseIntervalList) - 1], intervals[x])
            
            # Here, I assume that the intervals come in order. 
            lowType = myBaseIntervalList[len(myBaseIntervalList) - 1].lowType
            lowLimit = myBaseIntervalList[len(myBaseIntervalList) - 1].lowLimit
            
            possibleHighLimit1 = myBaseIntervalList[len(myBaseIntervalList) - 1].highLimit
            possibleHighLimit2 =  intervals[x].highLimit
            
            highLimitBetween = max(possibleHighLimit1, possibleHighLimit2)
            
            if highLimitBetween == possibleHighLimit1:
                highType = myBaseIntervalList[len(myBaseIntervalList) - 1].highType
                highLimit = myBaseIntervalList[len(myBaseIntervalList) - 1].highLimit
            else: 
                highType =intervals[x].highType
                highLimit = intervals[x].highLimit    
                
            intervalToReplace = lowType + str(lowLimit) + "," + str(highLimit) + highType
            intervalToReplace = interval(intervalToReplace)
            
            myBaseIntervalList[len(myBaseIntervalList) - 1] = intervalToReplace 
    
        except mergeIntervalsException:
            myBaseIntervalList.extend([intervals[x]])

    return myBaseIntervalList

def insert(intervals, newint):
    
    ''' Arguments of this function is a list "intervals" and an item of class interval() "newint"'''
       
    intervals.append(newint)
    intervals.sort(key = lambda interval:interval.sequenceArray[0])
    mergedIntervals = mergeOverlapping(intervals)    
    
    return mergedIntervals
        