'''
Created on 2016.11.14

@author: xulei
'''
from assignment7 import Interval
from Merge import *
from exceptionClass import *


def main():
    #The first loop get a list of intervals
    while True:        
        try: 
            input_str=input('List of Intervals? use comma then space to separate them')
            if input_str.upper()== 'QUIT':
                print('End of game')
                raise SystemExit()
            else:
                input_str_list=input_str.split(', ') 
                print(input_str_list)
                input_list= [Interval(i) for i in input_str_list]
                break
        except KeyboardInterrupt:
            print('End of game')
            raise SystemExit()
        except intervalException:
            print('Invalid Interval')   
    #The loop of keeping getting new interval
    
    list_to_merge=input_list
    while True:
        try: 
            input_int_str=input('Interval?')
            if input_int_str.upper()== 'QUIT':
                raise SystemExit()
            else:
                new_int=Interval(input_int_str)
                list_to_merge=insert(list_to_merge,new_int)
                list_to_merge_name=[i.name for i in list_to_merge]
                print(list_to_merge_name)
        except KeyboardInterrupt:
            print('End of game')
            raise SystemExit()
        except intervalException:
            print('Invalid Interval')   
    

if __name__ == "__main__":
    try:
        print('')
        print('Hint: Exit by QUIT')
        main()
    except EOFError:
        print()
        print('End of Game') # 
        raise SystemExit()