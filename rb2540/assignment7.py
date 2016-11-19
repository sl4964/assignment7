"""
This is a program you can run that takes user input and merges intervals.
"""
from interval import interval, IntervalError
def main() :
    """
    Prompts user for intervals, which it merges. Exits on "quit".
    """
    intlist = []
    while True :
        try :
            inp = input('List of intervals? ')
            if inp == "quit":
                return
            intlist = interval.parseList(inp)
            intlist = interval.mergeOverlapping(intlist)
            interval.printList(intlist)
            break
        except (IntervalError, ValueError):
            print('Error inputting intervals')
    while True :
        istr = input('interval? ')
        if istr == "quit" :
            break
        try :
            val = interval(istr)
            intlist = interval.insert(intlist,val)
            interval.printList(intlist)
        except (IntervalError, ValueError) :
            print('Invalid interval')
    

if __name__ == "__main__" :
    main()
