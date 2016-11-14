'''
Created on Nov 13, 2016

@author: sunevan
'''

import functools

class interval():
    '''
    input a 2 values here for an interval. () represents exclusive, [] represents inclusive value. 
    a valid input should be like "[4,5]" or "(4,5)"
    output: in some cases, there the inclusive or exclusive will be interchangeable when there are two intervals  
            for example: "[1,5]","[2,6)" will be merged as [1,5] but not [1,6). 
    '''
    def __init__(self, interval_input):
        '''
        initizalize the interval input
        '''
        self.interval_input = interval_input
        #change the input to a list
        self.all_integers_list = list(self.interval_input)
        
        # validate lower bound
        # Also, set the lower_bound_value. My idea is to represent an interval with a list of all the values in the interval. 
        #   thus, when the lower bound is "(", the minimum value in the integer should raise 1. eg.(1,5] means a list of 2,3,4,5. 
        if self.all_integers_list[0] not in ("[","("):
            raise ValueError ("Wrong lower bound symbol")
        elif self.all_integers_list[0] == "[":
            self.lower_bound_value = 0
        else: 
            self.lower_bound_value = +1 
        
        # validate upper bound:
        # same idea as mentioned above. when the upper bound is ")", the max. value in the list should decrease 1. 
        if self.all_integers_list[-1] not in ("]",")"):
            raise ValueError ("Wrong upper bound symbol")
        elif self.all_integers_list[-1] == "]":
            self.upper_bound_value = 0
        else: 
            self.upper_bound_value = -1 
            
        # validate comma: 
        # also, find the index of comma, which will be used to spilt the lower and upper bound. 
        self.value_integers_list = self.all_integers_list[1:-1]
        
        if self.value_integers_list.count(",") > 1:
            raise ValueError("Too many commas")
        elif self.value_integers_list.count(",") ==0:
            raise ValueError ("Missing a comma")
        else: 
            self.comma_index = self.value_integers_list.index(",")
            
            
            
        # process lower bound value by concanating all the variables in front of the comma 
        self.lower_bound_input = functools.reduce((lambda x,y: x+y),self.value_integers_list[0:self.comma_index])

        # validate if the lower bound is an integer  
        try: 
            int(self.lower_bound_input)
        except ValueError:
            raise  ValueError("Lower bound input is not an integer")

        # process lower bound in the list: (the original interval + adjustment when the symbol is "("  ) 
        self.lower_bound = int(self.lower_bound_input)+self.lower_bound_value

        # process upper bound value by concanating all the variables after the comma 
        self.upper_bound_input = functools.reduce((lambda x,y: x+y),self.value_integers_list[self.comma_index+1:])
        
        # validate if the upper bound is an integer 
        try: 
            int(self.upper_bound_input)
        except ValueError:
            raise  ValueError("Upper bound input is not an integer")
        #process upper bound in the list
        self.upper_bound = int(self.upper_bound_input)+self.upper_bound_value
        
        # validate if lower bound and upper bound meet the requirement:
        # since i have processed the value in previous steps, i only need to make sure lower bound is smaller 
        # than upper bound
        if self.lower_bound > self.upper_bound: 
            raise ValueError ("Upper bound is not large enough") 
        
        #generate a list of all the integer included in the interval     
        self.range_list = [i for i in range(self.lower_bound,self.upper_bound+1)]
        
        # with respect to the original input format 
        self.lower_bound_symbol = self.all_integers_list[0]
        self.upper_bound_symbol = self.all_integers_list[-1]
        # output a validate interval 
        self.clean_interval = self.lower_bound_symbol +self.lower_bound_input+","+\
                                self.upper_bound_input+self.upper_bound_symbol
        
        
    def range_list(self):
        return self.range_list 
        
    def __repr__(self):
        return (self.clean_interval)
    
    def lower_bound_symbol(self):
        return self.lower_bound_symbol
    
    def upper_bound_symbol(self):
        return self.upper_bound_symbol
    
    def lower_bound_input(self):
        return self.lower_bound_input
    
    def upper_bound_input(self):
        return self.upper_bound_input


def mergeIntervals(int1,int2):
    '''
    convert the interval to a list of all intergers and store it as a set 
    '''
    interval1 = interval(int1)
    interval2 = interval(int2) 

    # determine if 2 intervals are overlapped. Code ref: http://stackoverflow.com/questions/3170055/test-if-lists-share-any-items-in-python
    if set(interval1.range_list).isdisjoint(set(interval2.range_list)) is True: 
        raise ValueError ("There is a gap between 2 intervals")
    else: 
        # determine the new lower bound value and symbol. 
        # If 2 intervals have the same min value but different symobl eg. {"[1", "(2"}, I will pick the 2nd interval.
        if min(interval1.range_list) < min(interval2.range_list): 
            merged_lower_value = interval1.lower_bound_input
            merged_lower_symbol = interval1.lower_bound_symbol
        else:
            merged_lower_value = interval2.lower_bound_input
            merged_lower_symbol = interval2.lower_bound_symbol
            
        # determine the new upper bound value and symbol. 
        # If 2 intervals have the same max value but different symobl eg. {"1]", "2)"}, I will pick the 2nd interval.
        if max(interval1.range_list) > max(interval2.range_list): 
            merged_upper_value = interval1.upper_bound_input
            merged_upper_symbol = interval1.upper_bound_symbol
        else:
            merged_upper_value = interval2.upper_bound_input
            merged_upper_symbol = interval2.upper_bound_symbol
            
    return ((merged_lower_symbol+str(merged_lower_value)+","+str(merged_upper_value)+merged_upper_symbol)) 

# **Citation: code below is copied from stackflow: 
# **http://stackoverflow.com/questions/2154249/identify-groups-of-continuous-numbers-in-a-list
def group(L):
    '''
    this function take a list like (1,2,3,4,9,10,15,16)
    to (1,2,3,4),(9,10),(15,16)
    '''
    first = last = L[0]
    for n in L[1:]:
        if n - 1 == last: # Part of the group, bump the end
            last = n
        else: # Not part of the group, yield current group and start a new
            yield first, last
            first = last = n
    yield first, last # Yield the last group
# code above is used to merge overlap or adjacent intervals 


def mergeOverlapping(intervals):
    # One of the challeneges of my method is the format of output. For example, when the input is (1,4) will be output as [2,3]
    #   becasue of using the list of all integers. 
    # a list of all  lower bound values. this list will be used to respect the original input format.    
    lower_bound = list()
    for x in intervals:
        lower_bound.append(interval(x).lower_bound_input)
        
    # a list of all upper bound values   
    upper_bound = list()
    for x in intervals:
        upper_bound.append(interval(x).upper_bound_input) 
    # this will be a list to store all the intergers that were included in either intervals 
    all_integer = list()
    
    if len(intervals)==0:
        raise ValueError ("No interval list")
    else: 
        for interval_item in intervals:
            all_integer.extend(interval(interval_item).range_list) 
    # below function will split any discontinous integers (see explaination for function of "group") 
              
    sorted_all_integer = list(group(sorted(list(set((all_integer))))))
    merged_overlap_interval = list()
    
    # iterate through every sub-intervals produced by function
    # when the lower bound is not in the original lower bound list, it will tweak the number to respect the original input format 
    # for example, if the original input is (3,7), there is a 3 in the original lower bound value. However, my output would be "[4"
    # in this case, I will decrease 1 and change it to an exclusive symbol like "(3". same logic applied to upper bound.  
    for x in sorted_all_integer:
        if str(x[0]) in lower_bound:
            if str(x[1]) in upper_bound:
                merged_overlap_interval.append("["+str(x[0])+","+str(x[1])+"]") 
            else:
                merged_overlap_interval.append("["+str(x[0])+","+str(x[1]+1)+")") 
        else: 
            if str(x[1]) in upper_bound:
                merged_overlap_interval.append("("+str(x[0]-1)+","+str(x[1])+"]") 
            else:
                merged_overlap_interval.append("("+str(x[0]-1)+","+str(x[1]+1)+")") 

    return merged_overlap_interval 


def insert(intervals,newint):
    '''
    change the initial interval list to a list of all sub intervals 
    append the new initerval to the list 
    apply the mergerOver function
    ''' 
    intverals_list = [x for x in intervals]
    intverals_list.append(newint)
    return mergeOverlapping(intverals_list)


        
        