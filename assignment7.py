import sys
from interval import *

'''Main program with self-defined "interval" package'''

def main():
    while True:
        try:
            user_inp = input('List of intervals? ')
            user_inp = user_inp.replace(' ','').lower()
            if user_inp == 'quit':
                break
            else:
                inp_list = user_inp.split(',')
                lis = []
                for i in range(0, len(inp_list), 2):
                    lis.append(interval(inp_list[i] + ',' + inp_list[i+1]))
                    lis = mergeOverlapping(lis)
                break
        except (KeyboardInterrupt, SystemExit):
            raise
        except (EOFError, SystemExit):
            raise

    while True:
        try:
            inserted_inp = input("Intervals?")
            if inserted_inp.lower() == 'quit':
                break
            else:
                inserted_inp = interval(inserted_inp)
                lis = insert(lis,inserted_inp)
                print(lis)
        except (KeyboardInterrupt, SystemExit):
            raise
        except (EOFError, SystemExit):
            raise

if __name__ == '__main__':
    main()
