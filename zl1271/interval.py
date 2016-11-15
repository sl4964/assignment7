



import re


def is_int(s):
    return re.match(r"[-+]?\d+$", s) is not None
    # adapted from http://stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except

def is_interval_format(int_str):
    if not re.match(r"(\(|\[)-?\d+,\s?-?\d+(\)|\])", int_str):
        return False
    else:
        return True

def is_interval_content(int_str):
    lower_str,higher_str = int_str.split(",")
    lower_value = int(lower_str[1:])
    higher_value = int(higher_str[:-1])
    lower_brac = lower_str[0]
    higher_brac = higher_str[-1]
    
    if lower_brac == '(':
        lower_value = lower_value + 1
    if higher_brac == ')':
        higher_value = higher_value - 1
        
    if lower_value <= higher_value:
        return True
    else:
        return False
    
def is_interval(int_str):
    if is_interval_format(int_str):
        return is_interval_content(int_str)
    
class interval(object):
    '''
    classdocs
    '''
    def __init__(self, int_str):
        lower_str,higher_str = int_str.split(",")
        self.lower_value = int(lower_str[1:])
        self.higher_value = int(higher_str[:-1])
        self.lower_brac = lower_str[0]
        self.higher_brac = higher_str[-1]
        if self.lower_brac == '(':
            self.lowest_value = self.lower_value + 1
        else:
            self.lowest_value = self.lower_value
        if self.higher_brac == ')':
            self.highest_value = self.higher_value - 1
        else:
            self.highest_value = self.higher_value
        self.str = int_str

def mergeIntervals(int1, int2):
    if can_merge(int1, int2):
        lower_value = min([int1.lower_value,int2.lower_value])
        higher_value = max([int1.higher_value,int2.higher_value])
        
        if lower_value == int1.lower_value:
            lower_brac = int1.lower_brac
        elif lower_value == int2.lower_value:
            lower_brac = int2.lower_brac
            
        if higher_value == int1.higher_value:
            higher_brac = int1.higher_brac
        elif higher_value == int2.higher_value:
            higher_brac = int2.higher_brac

        new_int_str = lower_brac + str(lower_value) + ',' + str(higher_value) + higher_brac
    else:
        raise Exception('Merge failed')
    new_int = interval(new_int_str)
    return new_int

def sort_intervals(intervals_list):
    new_interval_list = sorted(intervals_list, key=lambda x: x.lowest_value)
    return new_interval_list

def can_merge(int1, int2):
    sorted_list = sort_intervals([int1, int2])
    former = sorted_list[0]
    later = sorted_list[1]
    return (former.highest_value >= later.lowest_value - 1)

def get_can_merge_list(intervals):
    can_merge_list = []
    if len(intervals) == 1:
        can_merge_list = [0]
    else:
        for ii in range(0,len(intervals)-1):
            if can_merge(intervals[ii],intervals[ii+1]):
                can_merge_list.append(1)
            else:
                can_merge_list.append(0)     
    return can_merge_list

def mergeOverlapping(intervals):
    sorted_intervals = sort_intervals(intervals)
    if len(sorted_intervals) == 1:
        return sorted_intervals
    else: 
        to_be_merged_list = list(sorted_intervals)
        merged_list = []
        can_merge_list = get_can_merge_list(to_be_merged_list)
        
        if sum(can_merge_list) == 0:
            merged_list = list(to_be_merged_list)

        while sum(can_merge_list) > 0:
            merged_list = []
            for jj in range(0,len(can_merge_list)):
                if can_merge_list[jj] == 1:
                    merged_list.append(mergeIntervals(to_be_merged_list[jj],to_be_merged_list[jj+1]))
                elif can_merge_list[jj] == 0:
                    if jj == 0:
                        merged_list.append(to_be_merged_list[jj])
                    elif jj > 0:
                        if can_merge_list[jj-1] == 0:
                            merged_list.append(to_be_merged_list[jj])
                       
                    
            if can_merge_list[-1] == 0:
                merged_list.append(to_be_merged_list[-1])

            can_merge_list = get_can_merge_list(merged_list)
            to_be_merged_list = list(merged_list)

        return merged_list
    
def insert(intervals, newint):
    intervals.append(newint)
    not_sorted_all = list(intervals)
    final_intervals = mergeOverlapping(not_sorted_all)
    return final_intervals

def print_intervals(intervals):
    if intervals == []:
        out_str = 'None'
    else:
        out_str = intervals[0].str
        for intval in intervals[1:]:
            out_str = out_str +', '+ intval.str
    print(out_str)
        
        
        
        
        
        