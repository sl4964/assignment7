from interval import *
import sys

def main():
    
    intervals = []
    while True:
        
        try:
            intervalListInput = raw_input("List of intervals? ")
            if intervalListInput == "quit":
                sys.exit(0)
            else:    
                intervalList = intervalListInput.split(', ')
            
                for intervalElement in intervalList:
                    intervals.append(interval(intervalElement))
                intervals = mergeOverlapping(intervals)
                break
            
        except EOFError:
            sys.exit(0)
            
        except InvalidIntervalError:
            print("Invalid Input")
    
    while True:
        
        try:
            intervalInput = raw_input("Interval? ")
            
            if intervalInput == "quit":
                sys.exit(1)
            
            intervalInput = interval(intervalInput)
            print(insert(intervals, interval))
        
        except EOFError:
            sys.exit(0)
        
        except InvalidIntervalError:
            print("Invalid Input")
        

if __name__=="__main__":
    main()