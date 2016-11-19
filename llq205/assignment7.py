from interval import *

def main():
    """main program to run by user"""
    intervals = []
    while True:
        try:
            lists = input("List of intervals? ")
            if lists.lower() == 'quit':
                return
            intervals = convert_list(lists)
            break
        except ValueError:
            print("Invalid Intervals")
    while True:
        try:
            newstring = input("Interval? ")
            if newstring.lower() == 'quit':
                return
            intervals = insert(intervals, interval(newstring))
            print(", ".join([str(x) for x in intervals]))
        except ValueError:
            print("Invalid Interval")
            
if __name__ == "__main__":
    main()

