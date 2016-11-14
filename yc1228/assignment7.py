import sys
from interval import *
def main():
    '''
    A program that uses interval class and functions to prompts the user 
    for a list of intervals, reads a string from the user, and creates a list 
    containing these intervals
    '''
    while True:
        try:
            user_input = input("List of intervals? ") #Take user input
            user_input = user_input.replace(' ','')
            if user_input.lower() == 'quit':
                break
            else:
                input_list = user_input.split(",")
                list_intervals = []
                for i in range(0, len(input_list), 2):
                    list_intervals.append(interval(input_list[i] + ',' + input_list[i+1]))
                list_intervals = mergeOverlapping(list_intervals)
                break
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)
    
    while True:
        try:
            add_input = input("Intervals?") #Insert additional intervals
            if add_input.lower() == 'quit':
                break
            else:
                add_input = interval(add_input)
                list_intervals = insert(list_intervals,add_input)
                print(list_intervals)
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            sys.exit(0)

if __name__ == '__main__':
    main()
            