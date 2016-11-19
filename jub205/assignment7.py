from interval.interval import interval, insert

def startProgram():
    '''Function runs the program to take list of intervals and then new interval
    each time from the user and inserts the new interval to the list of intervals
    and merges if overlapping or adjacent then returns the new list of intervals.
    Program terminates when the user inputs quit.
    '''
    
    ExitProgram = False
    
    intervals = input("List of intervals? ")
    
    if intervals == 'quit':
        ExitProgram = True
    else:
        intervals = intervals.split(', ')
        intervals = [interval(i) for i in intervals]
    
    while not ExitProgram:
        int1 = input("Interval? ")
        if int1 == 'quit':
            break
        try:
            int1 = interval(int1)
        except Exception as e:
            print(e)
        else:
            intervals = insert(intervals, int1)
            print(', '.join([i.interval for i in intervals]))
            
if __name__ == "__main__":
    startProgram()