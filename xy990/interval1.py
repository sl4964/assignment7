
# coding: utf-8

# In[ ]:

class InputError(Exception):
    pass

class invalidinterval(Exception):
    pass

class MergeException(Exception):
    pass

#This a class to initilize and how to represent the interval.

class interval(object):
    def __init__(self, input_list):
        
        input_list = input_list.strip()
        input_list = input_list.split(',')

        lower_symbols = ['[', '(']
        upper_symbols =[']', ')']
        
        if len(input_list[0]) <2 or len(input_list[1]) <2:
            raise InputError("")
        if input_list[0][0] not in lower_symbols or input_list[1][-1] not in upper_symbols:
            raise InputError("")
        
        def isInt(num):
            try:
                int(num)
                return True
            except InputError:
                return False
        
            

        self.lower_symbol = input_list[0][0]
        self.lower_bound = input_list[0][1:]
        self.upper_bound = input_list[1][:-1]
        self.upper_symbol = input_list[1][-1]
        try:
            
            if isInt(self.upper_bound) == False or isInt(self.lower_bound) == False:
                raise InputError
            else:
                
                if self.lower_symbol =='[':
                    self.lower_bound = int(self.lower_bound)
                else:
                    self.lower_bound = int(self.lower_bound) 

                if self.upper_symbol ==']':
                    self.upper_bound = int(self.upper_bound)
                else:
                    self.upper_bound = int(self.upper_bound)
        except:
            raise invalidinterval("Invalid interval")
            

    #string representation
    def __repr__(self):
        return self.lower_symbol + str(self.lower_bound) +',' + str(self.upper_bound) +self.upper_symbol

# check two intervals whether can merge.
def mergeableInterval(int1, int2):
    if isinstance(int1, interval) is False:
        raise InputError
    if isinstance(int2, interval) is False:
        raise InputError
    if int1.upper_bound < int2.lower_bound -1 or int1.lower_bound > int2.upper_bound +1:
        return False
    if int1.upper_symbol != ']' and int2.lower_symbol != '[' and int1.upper_bound <= int2.lower_bound-1:
        return False
    if int1.lower_symbol != '[' and int2.upper_symbol != ']' and int1.lower_bound >int2.upper_bound +1:
        return False
    return True

#define how to merge two intervals.
def mergeIntervals(int1, int2):
    #check whether int1 and int2 can merge or not
    if mergeableInterval(int1, int2):
        if int1.lower_bound <= int2.lower_bound:
            if int1.upper_bound >= int2.lower_bound -1:
                if int1.upper_bound > int2.upper_bound:
                    return(int1)
                else:
                    return( interval(str(int1)[0] + str(int1.lower_bound) +"," + str(int2.upper_bound) + str(int2)[-1]))
            else:
                raise MergeException("Cannot merge")
        else:
            if int1.lower_bound <= int2.upper_bound +1:
                if int1.upper_bound > int2.upper_bound:
                    return ( interval(str(int2)[0] + str(int2.lower_bound) +"," + str(int1.upper_bound) + str(int1)[-1]))
                else:
                    return(int2)
            else:
                raise MergeException("Cannot merge")
       
#Merge more than two intervals    
def mergeOverlapping(intervals):
    #for inter in intervals:
    #    if isinstance(inter, interval) is False:
    #        raise InputError
    if len(intervals)==0:
        return []
    intervals.sort(key = lambda inter: inter.lower_bound)
            
    overlapping_intervals =[]
    new_merged = intervals[0]
    
    for next_interval in intervals[1:]:
        if mergeableInterval(new_merged, next_interval):
            new_merged = mergeIntervals(new_merged, next_interval)
        else:
            overlapping_intervals.append(new_merged)
            new_merged = next_interval
    overlapping_intervals.append(new_merged)
    return overlapping_intervals

#How to insert one new interval to an exist interval
def insert(intervals, newint):
    
    if isinstance(newint, interval) is False:
        raise InputError("Invalid input")
    return mergeOverlapping(intervals + [newint])


import sys


def list_interval(user_init_input):
    if isinstance(user_init_input, str) is False:
        raise InputError
        
    user_init_input = user_init_input.strip()
    intervals =[]
    interval_list = user_init_input.split(",")
    
    if len(interval_list)%2 !=0:
            raise InputError
    for i in range(0, len(interval_list),2):
        one_interval =",".join([interval_list[i].strip(), interval_list[i+1].strip()])
        intervals.append(interval(one_interval))
    return mergeOverlapping(intervals)

#This is a main program that the user can interact.    
def main():
    while True:
        try:
            user_init_input = input("List of intervals?")
            
            if user_init_input.lower() =="quit":
                    return
                
            new_merged = list_interval(user_init_input)
            break
        except:
            print("invalid interval")
    while True:
            try:
                user_init_input = input("Interval?")
                
                if user_init_input.lower()=="quit":
                    return
                
                new_merged = insert(new_merged, interval(user_init_input))
                print(new_merged)
            except:
                print("invalid interval")
            
            
            



if __name__ == "__main__":
    main()

            
                
                
    
    
    

