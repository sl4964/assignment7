class interval:
    def __init__(self, interval_string):
        
        #Checks the brackets of the interval to determine the inclusivity of the interval
        if interval_string[0] == "[" :
            self.lower_inclusive = True
        elif interval_string[0] == "(" :
            self.lower_inclusive = False
        else:
            raise NameError("Not proper interval")
            
        if interval_string[-1] == "]" :
            self.upper_inclusive = True
        elif interval_string[-1] == ")" :
            self.upper_inclusive = False
        else:
            raise NameError("Not proper interval")
        
        #Finds the comma in the interval and starts recording the upper and lower part of the interval
        if interval_string.find(",") == -1 :
            raise NameError("Not proper interval")
        else:
            self.lower = interval_string[:interval_string.find(",")]
            if self.lower_inclusive == True:
                self.true_lower = int(self.lower[1:])
            else:
                self.true_lower = int(self.lower[1:]) + 1
            
            self.upper = interval_string[interval_string.find(",") + 1:]
            if self.upper_inclusive == True:
                self.true_upper = int(self.upper[:-1])
            else:
                self.true_upper = int(self.upper[:-1]) - 1
        
        # Checks to see if the interval is actually valid interval
        if self.true_upper < self.true_lower:
            raise NameError("Not proper interval")
        
        # Determine what integers the interval represents
        self.contains = range(self.true_lower, self.true_upper + 1)
        
        # Used for priniting the interval
        self.string = interval_string
        
    def __repr__(self):
        return self.string
            
def mergeIntervals(int1, int2) :
    """ This function should take in two intervals and merge them into one interval. If a merge is not possible then it will             raise a NameError """
    # Gets the true upper and lower limits of the new interval as well as what it is expected to contain as well as what it does       contain
    true_lower = min(int1.true_lower, int2.true_lower)
    true_upper = max(int1.true_upper, int2.true_upper)
    actlly_contain = list(int1.contains) + list(int2.contains)
    should_contain = list(range(true_lower,true_upper))
    
    # Determines if the new interval contains what it should
    for number in should_contain :
        if number not in actlly_contain :
            mergeable = False
            break
        else :
            mergeable = True
            
    # If the intervals are mergeable starts building the new interval. If not raises a NameError
    if mergeable :
        if int1.true_lower == int2.true_lower :
            lower = max(int1.lower, int2.lower)
        else : 
            if true_lower == int1.true_lower :
                lower = int1.lower
            elif true_lower == int2.true_lower :
                lower = int2.lower

        
        if int1.true_upper == int2.true_upper :
            if not int1.upper_inclusive:
                upper = int1.upper
            else :
                upper = int2.upper
        else :
            if true_upper == int1.true_upper :
                upper = int1.upper
            elif true_upper == int2.true_upper :
                upper = int2.upper
    else :
        raise NameError("Not mergeable intervals")
    
    new_int_string = lower + "," + upper
    new_int = interval(new_int_string)
    return new_int
                     

def mergeOverlapping(intervals):
    """This function merges a list of ordered intervals as much as possible and then returns a list of the newly merged                  intervals."""
    
    # Start of the output list with the first interval in the input list
    new_intervals = [intervals[0]]
    i = 0
    
    # Trys to merge the latest interval in the output list with latest interval in the input list and if unsuccessful adds the       # latest input interval to output list and makes it the latest interval of the list.
    for ind in range(1,len(intervals)):
        try:
            new_intervals[i] = (mergeIntervals(new_intervals[i], intervals[ind]))
        except NameError :
            i = i + 1
            new_intervals.append(intervals[ind])
            
    return new_intervals

def insert(intervals, newint):
    """This function finds where to put a new interval into a list of ordered intervals and then merges the list """
    
    # Finds where in the list to place the new interval and places it there
    for some_int in intervals:
        if int(newint.lower[1:]) <= int(some_int.lower[1:]):
            insert_here = intervals.index(some_int)
            intervals.insert(insert_here, newint)
            break
    else :
        intervals.append(newint)
    
    # Merges the updated list of ordered intervals
    new_intervals = mergeOverlapping(intervals)
    return new_intervals

# My program starts here

def interval_translator():
    """This function takes in a list of intervals in string form from the user and then turns it into an actual list of intervals """
    
    # These are the characters that this function is allowed to use to build an interval
    white_list = "[(-0123456789)],"

    # Takes in the input from the user and gets it ready to be processed
    input_string = input("List of intervals? \n") + ","
    ind = 0
    intervals = []
    
    # Goes through the input string and starts building the list of intervals
    while ind < len(input_string):
        comma_count = 0
        temp_string = ""
        while comma_count < 2 :
            test = input_string[ind]
            if test == "," :
                comma_count += 1
            
            if (test in white_list) and comma_count < 2 :
                temp_string += test
            
            ind += 1
        else :
            intervals.append(interval(temp_string))
    print(intervals)
    return intervals

# This try statement determines whether or not the input is valid and then prompts the user for another if not.
is_proper_intervals = False
while is_proper_intervals == False:
    try:
        intervals = interval_translator()
    except NameError:
        print("One of the intervals is not a valid interval")
    except IndexError:
        print("Not a valid list of intervals")
    else: 
        is_proper_intervals = True

# Here the program continuely asks the user for an interval to be inserted and then merged into the list of intervals until         prompted to quit.        
quit = False
while quit == False :
    is_proper_input = False
    while is_proper_input == False:
        interval_string = input("Interval? \n")
        # Here the program determines if the interval can actually be made or if the user is quitting
        try:
            newint = interval(interval_string)
        except NameError:
            if interval_string == 'quit' :
                quit = True
                is_proper_input = True
            else: 
                print("Invalid interval")
        else: 
            is_proper_input = True
    else:
        if not quit:
            intervals = insert(intervals, newint)
            print(intervals)
            
   