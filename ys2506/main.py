import exceptions
import interval 

def main():
    intervals = []
    try:
        intervals = [interval(e) for e in input('List of intervals? ').split(', ')]
    except InvalidException:
        print('Invalid interval')
    
    while(True):
        try:
            s = input('Interval? ')
            if s == 'quit':
                break
            newint = interval(s)
            #output [[-10,-7], (-4,1], [3,12), [15,23]] should be [-10,-7], (-4,1], [3,12), [15,23]
            print(*(insert(intervals, newint)))
        except InvalidException:
            print('Invalid interval')
        except KeyboardInterrupt:
            # Exit if the user enters Ctrl+C
            sys.exit(0)
        except EOFError:
            # Exit if the user enters Ctrl+D
            sys.exit(0)

if __name__ == "__main__":
        main()

