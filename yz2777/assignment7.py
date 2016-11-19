"""A program using a created class called "interval" (in separate module) and some defined merge functions (in separate module) that 
   prompts the user for a list of intervals, reads a string from the user, and creates a list containing these intervals after merging"""

from class_interval import interval
from merge_func import insert

#Question 5 of HW7
#Convert user intervals string input to a list of string intervals  
def user_input_str(intervals_string):
    
    if len(intervals_string) != 0:
        #Pre-processing the input intervals list
        pre_int_li = list(intervals_string)
    
        #Exclude the input which does not contain '(' or '[' at the beginning of the first interval or 
        #does not contain ')' or ']' at the end of the last interval 
        #Or does not contain ","
        if pre_int_li[0] in ('(','[') and pre_int_li[-1] in (')',']') and "," in pre_int_li:
            ne = intervals_string.split(",")
        
            #the length after spliting must be even number
            if len(ne)%2 == 0:
                map1=[]
                for i in range(0,len(ne),2):
                    new = ne[i]+','+ne[i+1]
                    map1.append(new)
                return map1
            else:
                map1 = ['(9999, -9999)']
                return map1
        else:
            map1 = ['(9999, -9999)']
            return map1
    else:
        map1 = ['(9999, -9999)']
        return map1

#### Part 1, input intervals list
#User input for a string of intervals
def inpt():
    user_input = input('List of intervals? Or enter quit to quit\n')

    flag=1   # Given an indicator for input, 0 means incorrect input, 1 means correct

    #If user doesn't input quit, we first convert the string input to what we need
    #Then, check whether the input intervals are correct
    #If the input is incorrect, break the for loop and then go to the next while loop
    if user_input != 'quit':
        convert_input = user_input_str(user_input)
        for i in range(len(convert_input)):
            intel = convert_input[i]
            if str(interval(intel)) == "Invalid interval":
                flag = 0  
                break

    #This while loop will check whether the user input is correct again until the user enter the correct intervals list
    while user_input != 'quit' and flag == 0:
        user_input = input('You have entered wrong interval list. Please input again or enter quit to quit\n')
    
        if user_input != 'quit':
            convert_input = user_input_str(user_input)
            for i in range(len(convert_input)):
                intel = convert_input[i]
                if str(interval(intel)) == "Invalid interval":
                    flag = 0
                    break
                else:
                    flag = 1

    #### Part 2 input one more interval to merge with given intervals list
    #While the user input the correct intervals list
    #He/she will be asked to add one more interval again and agian until input quit
    if user_input != 'quit':
        merge_li = convert_input    #Geting the intervals list from part 1
    
        user_input = input('Interval? Add one more interval or enter quit to quit\n')
    
        while user_input != 'quit':
            one_int = user_input
            check_int = interval(one_int)
        
            #Given user input is not quit, the user will be asked to enter the interval until correct
            #Or user can enter quit to quit
            while str(check_int) == 'Invalid interval':
                print ('Invalid interval')
                user_input = input('Interval? Add one more interval or enter quit to quit\n')
                if user_input == "quit":
                    break
                else:
                    one_int=user_input
                    check_int = interval(one_int)
        
            #If user entered the correct interval,
            #the the interval will be merged to the given intervals list
            #and then ask to enter another interval
            if str(check_int) != 'Invalid interval':
                merge_li = insert(merge_li, one_int)
                
                #since the new merge_li using list to present inclusive for each interval, 
                #we need to convert back to string
                initial = []
                for li in merge_li:
                    initial.append(str(li))
                merge_li = initial
                print (",".join(merge_li))
            
                user_input = input('Interval? Input one more interval or enter quit to quit\n')

if __name__ == '__main__':
    inpt()