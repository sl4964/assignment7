from question_1 import interval
from question_2 import mergeIntervals
from question_3 import mergeOverlapping
from question_4 import insert

#Define a function to transform the input intervals string into list
def transform(string_intervals):
    if len(string_intervals)>0:
    #The length of input interval string cannot be 0 
        pre_check=list(string_intervals);
        #Exclude the interval list that does not contain '(' or '[' at the beginning of the first interval or does not contain ')' or ']' at the end of the last interval or does not contain ","
        if pre_check[0] in ('(','[') and pre_check[-1] in (')',']') and "," in pre_check:
            #Divide the string and make it a list
            string_intervals=string_intervals.split(",");
            #If the length after division is not even number, the input is not valid
            m=len(string_intervals);
            if m%2==0:
                interval_list=[]
                for i in range(0,m-1,2):
                    interval_list.append(string_intervals[i]+','+string_intervals[i+1]);
                return interval_list;
            else:
                return ['[1,-1]']
        else:
            return ['[1,-1]']
    else:
        return ['[1,-1]']

#Let the user input a list of intervals
user_list=input("A list of intervals? Quit the program by entering quit\n");
#If the input is not quit, we will justify the validity of the interval list
if user_list!='quit':
    interval_list=transform(user_list);
    #Justify if the intervals are valid
    n=len(interval_list);
    for i in range(n):
        s=interval(interval_list[i])
        if str(s)=='The interval is not valid':
            break
#If the input is not quit and not valid interval list, the user will re-input
while user_list!='quit' and str(s)=='The interval is not valid':
    user_list=input("The input intervals are not valid, please input again. A list of intervals? Quit the program by entering quit\n");
    if user_list!='quit':
        interval_list=transform(user_list);
        #Justify if the intervals are valid
        n=len(interval_list);
        for i in range(n):
            s=interval(interval_list[i])
            if str(s)=='The interval is not valid':
                break
                
#The next process will be ignored if no valid interval list has been inputed
if user_list!='quit':
    #Change the interval list to a list of interval strings
    merge_int=interval_list;
    d=len(merge_int);
    #Let the author input the insert interval
    user_insert=input("Interval? Quit the program by entering quit\n");
    #If we do not input quit, we will check the validity of the input interval
    while user_insert!='quit':
        #If the interval is correct, we will merge the interval and ask next one
        s=interval(user_insert);
        if str(s)!='The interval is not valid':
            merge_int=insert(merge_int,user_insert);
            print(merge_int);
            d=len(merge_int);
            for i in range(d):
                merge_int[i]=str(merge_int[i]);
            user_insert=input("Please input next interval. Intervals? Quit the program by entering quit\n");
        #If the interval is not correct, we will ask the user to re-input until correct or quit
        while str(s)=='The interval is not valid':
            user_insert=input("The interval is not valid, please input again. Intervals? Quit the program by entering quit\n");
            if user_insert=='quit':
                break;
            s=interval(user_insert);