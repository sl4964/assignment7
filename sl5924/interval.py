'''

This module contains:
 
Class: 
Interval: Define a group of intervals, creation and display  

Methods:
(1) mergeIntervals
(2) mergeOverlapping
(3) insert
(4) isOverlap: To determine whether two intervals are overlapped or not
(5) isAdjacent: To determine whether two intervals are adjacent or not
(6) interval2str: Convert intervel objects to string 

Created on 2016/11/08
Version: 1.0
@author: liusheng
ShengLiu Copyright 2016
'''


class interval:
    '''
    classdocs
    '''


    def __init__(self, s):
        '''
        Constructor
        '''
        try:
            if (type(s) is str) and (s[0] == '(' or s[0] == '[') and \
                    (s[-1] == ')' or s[-1] == ']') and \
                    (len(s[1:-1].split(',')) == 2) and \
                    int(s[1:-1].split(',')[0]) - int(s[1:-1].split(',')[1]) <= 0:
                self.Lower = s[0]
                self.Upper = s[-1]
                self.Lowerbound = int(s[1:-1].split(',')[0]) + (0 if s[0]=='[' else 1)
                self.Upperbound = int(s[1:-1].split(',')[1]) - (0 if s[-1] == ']' else 1)
                self.LowerNum = int(s[1:-1].split(',')[0])
                self.UpperNum = int(s[1:-1].split(',')[1])
            else:
             raise ValueError('Invalid Input, Please put string like [1,3) etc.') 
            if self.Lowerbound > self.Upperbound:
                raise ValueError('Invalid Input, Please put string like [1,3) etc.') 
        except Exception:
            raise              
    
    def isOverlap(int1, int2):
        if (int1.Upperbound >= int2.Lowerbound) and (int2.Upperbound >= int1.Lowerbound) :
            return 1
        else:
            return 2
        
    def isAdjacent(int1, int2):
        if (int1.Upperbound - int2.Lowerbound == -1) or (int2.Upperbound - int1.Lowerbound == -1):
            return 1
        else:
            return 2
    def interval2str(self):
        result =''
        if self.Lower == '[':
            result = self.Lower + str(self.Lowerbound)
        else:
            result = self.Lower + str(self.Lowerbound - 1)
        if self.Upper == ']':
            result += ',' + str(self.Upperbound) + self.Upper
        else:
            result += ',' + str(self.Upperbound + 1) + self.Upper 
        return  result  
    def mergeIntervals(int1 ,int2): 
        interval_str =''
        if interval.isAdjacent(int1, int2) ==1:
            if int1.Lowerbound <= int2.Upperbound:
                interval_str = interval_str + int1.Lower + str(int1.Lowerbound - (1 if int1.Lower == '(' else 0)) + ',' + str(int2.Upperbound + (1 if int2.Upper == ')' else 0)) + int2.Upper
            elif int2.Lowerbound <= int1.Upperbound:   
                interval_str += int2.Lower + str(int2.Lowerbound - (1 if int2.Lower == '(' else 0)) + ',' + str(int1.Upperbound + (1 if int1.Upper == ')' else 0)) + int1.Upper
            return interval(interval_str) 
        elif interval.isOverlap(int1,int2) ==1:
            #if int1.Lowerbound < int2.Upperbound and int1.Upperbound > int2.Lowerbound:
            if int1.Lowerbound <= int2.Lowerbound:
                interval_str += int1.Lower +str(int1.LowerNum) +','
                if int1.Upperbound == int2.Upperbound:
                    interval_str += str(int1.UpperNum)+ int1.Upper
                elif int1.Upperbound > int2.Upperbound:
                    interval_str += str(int1.UpperNum) + int1.Upper
                else:
                    interval_str += str(int2.UpperNum) + int2.Upper
            else:
                interval_str += int2.Lower +str(int2.LowerNum) +','
                if int1.Upperbound == int2.Upperbound:
                    interval_str += str(int1.UpperNum)+ int1.Upper
                elif int1.Upperbound > int2.Upperbound:
                    interval_str += str(int1.UpperNum) + int1.Upper
                else:
                    interval_str += str(int2.UpperNum) + int2.Upper
            return interval(interval_str)  
        else:
             return Exception(" There is no overlap") 
     
    def mergeOverlapping(intervals):
        intervals = intervals.replace(" ","")
        s_list = intervals.split(",")
        #print(s_list)
        new_list_intervals = []
        if len(s_list) == 2:
            return intervals
        else:
            for d in range(0,len(s_list),2):
                new_list_intervals.append(interval(s_list[d] + ',' + s_list[d+1]))

            i = 0
            j = 1
            LengthOfList = len(new_list_intervals)
            while (i < LengthOfList-1):
                if interval.isOverlap(new_list_intervals[i], new_list_intervals[j]) == 1 \
                    or interval.isAdjacent(new_list_intervals[i] , new_list_intervals[j]) ==1:
                    new_list_intervals[i] = interval.mergeIntervals(new_list_intervals[i], new_list_intervals[j])
                    new_list_intervals.pop(j)
                    j = i + 1
                else:
                    j = j + 1
                if j >= len(new_list_intervals):
                    i = i + 1
                    j = i + 1 
                LengthOfList = len(new_list_intervals)
            result = ''
            for i in range(0 , len(new_list_intervals) - 1):
                result += new_list_intervals[i].interval2str() + ', '
            result = result + new_list_intervals[-1].interval2str() 
            return result
    
    def insert(intervals, newint):
        if intervals == '':
            return newint
        else: 
            return interval.mergeOverlapping(intervals + ', ' + newint)