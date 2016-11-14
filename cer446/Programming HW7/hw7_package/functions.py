'''
Created on Nov 14, 2016

@author: Caroline
'''
import interval_class as i

def Merge_intervals(int1, int2):
    
    assert isinstance(int1, i.Interval), 'first input is not an Interval'
    assert isinstance(int2, i.Interval), 'second input is not an Interval'
    
    def establish_validity(int1, int2):
        overlapping = False
        adjacent = False
    
        for i in int1.interval_list:
            if (i in int2.interval_list): #if any value found in the first interval 
                overlapping=True
        if int1.upper_inclusive + 1 in int2.interval_list or int1.lower_inclusive - 1 in int2.interval_list:
            adjacent = True
        if overlapping != True and adjacent != True:
            raise Exception('Intervals are not overlapping or adjacent')
            
    establish_validity(int1,int2)
    
    def create_interval_input(int1,int2):
        new_interval = str()
        if int1.lower < int2.lower or (int1.lower == int2.lower and int1.interval[0] == '['): #one integer is strictly less than another (doesn't matter whether open or close)
            new_interval = new_interval + str(int1.interval[0]) + str(int1.lower) + ',' #take lower bound from int1
        elif int1.lower > int2.lower or (int1.lower == int2.lower and int2.interval[0] == '['):
            new_interval = new_interval + str(int2.interval[0]) + str(int2.lower) + ',' #take lower bound from int2     
        if int1.upper > int2.upper or (int1.upper == int2.upper and int1.interval[0] == ']'):
            new_interval = new_interval + str(int1.upper) + int1.interval[-1]
        elif int2.upper > int1.upper or (int1.upper == int2.upper and int2.interval[0] == ']'):
            new_interval = new_interval + str(int2.upper) + int2.interval[-1]
        return new_interval
        
    merged_interval = i.Interval(create_interval_input(int1,int2))
    
    return merged_interval

def mergeOverlapping(intervals_input):
    
    intervals = intervals_input #copy of input to avoid side effecting
    
    def find_possible_pairs(intervals):
    
        pairs = []
    
        for i in range(0, len(intervals)):
            for k in range(i, len(intervals)):
                if i != k:
                    pairs.append([intervals[i],intervals[k]])                
        return pairs
    
    pairs = find_possible_pairs(intervals)

    pair = 0

    while pair < (len(pairs)): #as long as we have one more pair to try
        try:
            merged_interval = (Merge_intervals(pairs[pair][0], pairs[pair][1])) #merge        
            intervals.pop(intervals.index(pairs[pair][0])) #get rid of the interval that was merged
            intervals.pop(intervals.index(pairs[pair][1])) #get rid of the other interval that was merged
            intervals.append(merged_interval) #add the merged interval      
            pairs = find_possible_pairs(intervals)
            pair = 0 #if you found a merge, we want to try again starting at pair 0
        except Exception:
            pass
            pair = pair + 1 #then advance to the next pair
    
    return intervals

def insert(intervals, newint):
    starting_intervals = intervals
    try:
        starting_intervals.extend(newint)
    except TypeError:
        starting_intervals.append(newint)
    merged = mergeOverlapping(starting_intervals)
    merged = sorted(merged, key=lambda interval: interval.lower)
    return merged

#helper functions for the game itself

def recombine_split_input(split_input):
    
    recombined_input = split_input
    
    for i in range(0, len(recombined_input)):
        if recombined_input[i-1] == '(' or recombined_input[i-1]=='[': #if it's a beginning
            recombined_input[i] = recombined_input[i-1] + recombined_input[i] #add it to the next entry
    return recombined_input

def clean_after_interval(split_input):
    condensed_input = split_input
    for i in range(0, len(condensed_input) - 1):
        if ']' in condensed_input[i]:
            condensed_input[i] = condensed_input[i][:condensed_input[i].find(']')+1]
        if ')' in condensed_input[i]:
            condensed_input[i] = condensed_input[i][:condensed_input[i].find(')')+1]
    return condensed_input

def parse_interval_input(interval_input): #put this change in eclipse
    import re
    if interval_input == '': #raise error if empty string
        raise ValueError('empty string')
    else:
        split_input = re.split('(\[|\()', interval_input)
        del split_input[0]
        if split_input == []: #raise error if no beginnings found
            raise ValueError('no [ or ( to identify beginning of interval')
        else:
            split_input = recombine_split_input(split_input)
            split_input = [value for value in split_input if value != '(' and value != '[']
            split_input = clean_after_interval(split_input)
            return split_input

def Make_intervals(split_input):
    
    intervals = []
    
    for interval in split_input:
        try:
            intervals.append(i.Interval(interval))
        except AssertionError as err:
            print('Invalid input for interval \'{0}\' Error = {1}'.format(interval,err))
            intervals = [] #clear intervals if not all the intervals parse correctly
        
    if intervals:
        return intervals