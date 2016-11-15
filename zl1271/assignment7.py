

from interval import *

def loop():
    user_input_str = input('Intervals?\n')
    user_input_str = re.sub(r'\s+', '', user_input_str)
  
    list_of_intervals = []
    while user_input_str.upper() != 'QUIT': 
            try:
                splited_user_input = user_input_str.split(",")
                if len(splited_user_input) % 2 == 0: # If input correct, there should be even number of splits
                    list_of_interval_str = []
                    for counter in range(0,int(len(splited_user_input)/2)): # Every two splits should be a valid interval
                        this_interval_str = splited_user_input[counter*2]+','+splited_user_input[counter*2+1]
                        if is_interval(this_interval_str): 
                            list_of_interval_str.append(this_interval_str) 
                        else:
                            raise Exception('Invalid interval')
                    # all tests passed, do the program
                    for ii in range(0,len(list_of_interval_str)):
                        list_of_intervals = insert(list_of_intervals,interval(list_of_interval_str[ii]))
                        
                    print_intervals(list_of_intervals)
                    user_input_str = input('Intervals?\n')
                    user_input_str = re.sub(r'\s+', '', user_input_str)
                else:
                    raise Exception('Invalid interval')
            except:
                print('Invalid interval')
                user_input_str = input('Intervals?\n')
                user_input_str = re.sub(r'\s+', '', user_input_str)
    exit('The end')            

if __name__ == '__main__':
    try:
        print('Please input intervals')
        loop()
    except EOFError:
        pass