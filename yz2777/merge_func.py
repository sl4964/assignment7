""" Defined merge functions """

#Question 2 of HW7
#int1 and int2 should be interval in a string representation
def mergeIntervals(int1, int2):
    int1_str = int1[1:-1].split(",")
    int2_str = int2[1:-1].split(",")
    
    #Get int1 and int2 lower and upper bound integers
    lower_int1 = int(int1_str[0])
    upper_int1 = int(int1_str[1])
    lower_int2 = int(int2_str[0])
    upper_int2 = int(int2_str[1])
    
    #Get int1 and int2 lower and upper bound symbols
    lb_int1 = int1[0]
    ub_int1 = int1[-1]
    lb_int2 = int2[0]
    ub_int2 = int2[-1]
    
    #Get the actual lower and upper bound values based on the bound symbols 
    if lb_int1 == '[':
        lowerV_int1 = lower_int1
    else:
        lowerV_int1 = lower_int1 + 1
    
    if lb_int2 == '[':
        lowerV_int2 = lower_int2
    else:
        lowerV_int2 = lower_int2 + 1
    
    if ub_int1 == ']':
        upperV_int1 = upper_int1
    else:
        upperV_int1 = upper_int1 - 1
    
    if ub_int2 == ']':
        upperV_int2 = upper_int2
    else:
        upperV_int2 = upper_int2 - 1
   
    #Create new interval based on the overlap
    #The lower-bound symbol is decided by the minimum lower-bound value's lower bound symbol between two intervals
    #The upper-bound symbol is decided by the maximum upper-bound value's upper bound symbol between two intervals
    #And throw exception when the two intervals have no overlap
    try:
        if upperV_int1 - lowerV_int1 >= 0 and upperV_int2 - lowerV_int2 >= 0:      #make sure upper number >= lower number
            if lowerV_int1 - lowerV_int2 <= 0 and upperV_int1 - upperV_int2 >= 0:
                new_int = int1
            elif lowerV_int1 - lowerV_int2 < 0 and upperV_int1 - upperV_int2 < 0 and upperV_int1 - lowerV_int2 >= -1:
                new_int = lb_int1 + int1_str[0] + ',' + int2_str[1] + ub_int2
            elif lowerV_int1 - lowerV_int2 > 0 and upperV_int1 - upperV_int2 > 0 and lowerV_int1 - upperV_int2 <= 1:
                new_int = lb_int2 + int2_str[0] + ',' + int1_str[1] + ub_int1
            elif lowerV_int1 - lowerV_int2 >= 0 and upperV_int1 - upperV_int2 <= 0:
                new_int = int2
            else:
                raise ValueError ("No overlap between two intervals")
            return new_int
        else:
            raise ValueError ("No overlap between two intervals")
    except:
        return "No overlap between two intervals"




#Question 3 of HW7
#input should be a list of intervals with string representation for each
def mergeOverlapping(intervals):
    
    #Get length and range of input interval list
    #And, initialize an interval list for later use
    num_int = len(intervals)
    range_int = range(num_int)
    incl_int = intervals
    
    for idx in range_int:
        intx = intervals[idx]
        intx_str = intx[1:-1].split(",")
        lower_intx = int(intx_str[0])    #lower bound number
        upper_intx = int(intx_str[1])    #upper bound number
        lb_intx = intx[0]                #lower bound symbol
        ub_intx = intx[-1]               #upper bound symbol
    
        #Get the actual lower and upper bound values based on the bound symbols
        #i.e., standardize to inclusive bounds [] 
        if lb_intx == "(":
            lowerV_intx = lower_intx + 1
        elif lb_intx == "[":
            lowerV_intx = lower_intx  
        if ub_intx == ")":
            upperV_intx = upper_intx - 1
        elif ub_intx == "]":
            upperV_intx = upper_intx    
        incl_int[idx] = [lowerV_intx, upperV_intx]
    
    #Sort the standardized intervals in ascending order based on the each interval's lower bound value 
    sort_incl = sorted(incl_int, key = lambda z:z[0])
    
    #Merge the overlapping or adjacent intervals
    #initialize an empty merged intervals list
    merge_incl = []                                 
    
    for intl in sort_incl:
        
        #If there is nothing in the merge_incl,the first interval from the sorted list will be added in the merge_incl
        if merge_incl == []:                                                                       
            merge_incl.append(intl)
        
        #Involve Q2's mergeIntervals(int1,int2) to check if there is overlap between the last interval in merge_incl and one interval from the sorted intervals list (i.e., sort_incl)
        #If not, add the interval from sort_incl to merge_incl 
        elif mergeIntervals(str(merge_incl[-1]),str(intl)) == 'No overlap between two intervals':
            merge_incl.append(intl)                 
        
        #Otherwise, compare the pper bound values between the last interval from the
        #merge_incl and the interval from the sorted list and use the maximum one
        else:
            merge_incl[-1][1] = max(intl[1], merge_incl[-1][1])  
                                                                 
    return merge_incl




#Question 4 of HW7
#input intervals should be a list of intervals with string representation for each
#input newint should be an interval in a string representation
def insert(intervals, newint):
    newint_str = newint[1:-1].split(",")
    
    #Get newint lower and upper bound integers
    lower_newint = int(newint_str[0])
    upper_newint = int(newint_str[1])
    
    #Get int1 and int2 lower and upper bound symbols
    lb_newint = newint[0]
    ub_newint = newint[-1]

    #Get the actual lower and upper bound values based on the bound symbols
    #i.e., standardize to inclusive bounds [] 
    if lb_newint == '[':
        lowerV_newint = lower_newint
    elif lb_newint == '(':
        lowerV_newint = lower_newint + 1
    if ub_newint == ']':
        upperV_newint = upper_newint
    elif ub_newint == ')':
        upperV_newint = upper_newint -1
    
    #Coverted newint
    newint_convt = [str([lowerV_newint, upperV_newint])]
    
    #New intervals list
    new_list = intervals + newint_convt
    
    #Call Q3's mergeOverlapping(intervals), we get the result
    result = mergeOverlapping(new_list)
    return result