
from interval import interval
import sys

def main():
    """ This is the main function that take user's input and give output """
    i = interval()
    while 1:
        #print("first while")
        try:
            input_string = input('Enter the interval: ')
        except EOFError:
            sys.exit(0)
            
        try:
            initial = i.make_intervals(input_string)
            i.list_print(initial)
            break
        except ValueError as e:
            print(e)
        except:
            print('Other unexpected errors.')
        
        # if encounter a error, except, prompt message and take a new input.
    #print("out of first while")
    while 1:
        #print("in second while")
        try:
            input_string=input('Interval?')
        except EOFError:
            sys.exit(0)
            
        if input_string == 'quit':
            break
        # if input is quit, break the program.
        
        try:
            new_int = i.make_interval_helper(input_string) # merge new interval into the original interval list
        except ValueError as e:                        # check invalid interval format
            print(e)
        except:
            print('Other unexpected errors.')
        
        try:
            i.check_adjcent(initial, new_int) # if the new interval won't merge into the original interval list, prompt message
        except ValueError as e:
            print(e)
        except:
            print('Other unexpected errors.')
            
            
        initial = i.insert(initial, new_int)
        i.list_print(initial)     

if __name__ == "__main__":
    main()
