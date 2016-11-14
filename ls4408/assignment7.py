from interval_functions import *
'''this is the main function which used functions from interval functions.
  It encourages users to firstly input correct lists of correct intervals, 
   and then merge new interval entered by the user'''

if __name__ == '__main__':
        i=0
        interval_list = input("List of intervals?:")
        #prompt user to enter a list of intervals
        interval_list = interval_list.split(',')
        combined_list=[]
        while (i+1<= len(interval_list)):
                try:
                    left_join=interval_list[i]
                    right_join=interval_list[i+1]
                    new_element=left_join+','+right_join
                    i=i+2
                    try:
                        combined_list.append(interval(new_element))
                    except ValueError:
                        i=0
                        interval_list = input("List of intervals?:")
                        interval_list = interval_list.split(',')
                        combined_list=[]
                        #this try-except trys to make sure user enters correct intervals.
                except IndexError:
                    i=0
                    interval_list = input("List of intervals?:")
                    interval_list = interval_list.split(',')
                    combined_list=[]
                    #this try-except trys to make sure user enters only list of intervals without anything else
                #commands above parse the string of 'interval list' input by the user 
        merge_intervals=mergeOverlapping(combined_list)
        merge_intervals_string=[str(item) for item in merge_intervals]
        print(','.join(merge_intervals_string))
        # return the merged intervals from a list to a string.
            
        while(True):
            interval_single=input("Interval? Or input quit:")
            if interval_single=="quit":
                break
                #if user entered quit, then the programming ends
            else:
                try:
                    insert_intervals=insert(merge_intervals,interval(interval_single))
                    insert_intervals_string=[str(item) for item in insert_intervals]
                    print(','.join(insert_intervals_string))
                    # return the inserted intervals from a list to a string.
                except ValueError:
                    print("Invalid Interval")
            