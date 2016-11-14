'''
Created on Fri Nov 11 12:51:28 2016

@author: wxy
'''

class interval:
    
    def __init__(self, string):
        
        digits = [int(s) for s in string[1:-1].split(",")]
        self.left = string.split(",")[0]
        self.right = string.split(",")[1]
            
        if (string[0] == "[" and string[-1]=="]"):
            self.lower = digits[0]
            self.upper = digits[1]
        elif (string[0] == "[" and string[-1]==")"):
            self.lower = digits[0]
            self.upper = digits[1]-1
        elif (string[0] == "(" and string[-1]=="]"):
            self.lower = digits[0]+1
            self.upper = digits[1]
        elif (string[0] == "(" and string[-1]==")"):
            self.lower = digits[0]+1
            self.upper = digits[1]-1
        
    @staticmethod 
    def mergeIntervals(int1,int2):
        '''
        for two interval, function compares lower and upper bounds of two intervals and returns merged interval 
        ''' 
        string = ""
        if int1.upper > int2.lower :
            if int1.upper >= int2.upper:
                string = string + int1.left+ "," + int1.right
            else:
                string = string + int1.left+ "," + int2.right
            return interval(string)
         
        elif int1.upper == int2.lower-1:
            string = string + int1.left + "," + int2.right
            return interval(string)
        else:
            raise Exception("There's no overlap")
    
    
    @staticmethod
    def mergeOverlapping(intervals):
        '''
        the function takes list of intervals and merged them in pairs
        ''' 
        result = []
        for i in range(0, len(intervals)):
            try:
                intervals = intervals.sort(key= lambda x: x.lower)
                intervals[i+1] = interval.mergeIntervals(intervals[i], intervals[i+1])
            except Exception:
                result.append(intervals[i])
        return result
    
    
    @staticmethod
    def insert(intervals, newint):
        '''
        the function first insert the new interval at the end, then call the merge overlap function to complete the merge 
        '''
        intervals.append(newint)
        merged_intervals = interval.mergeOverlapping(intervals)
        return merged_intervals