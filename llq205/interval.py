from assignment7 import *
class interval(object):
    
    def __init__(self, inputs):
        """Check whether inputs are valid, and create the class"""
        #splitting into two parts and do initial checks
        sep = inputs.split(",")
        if len(sep) != 2:
            raise ValueError("This is an invalid input.")
        if len(sep[0]) < 2 or len(sep[1]) < 2:
            raise ValueError("This is an invalid input.")
        if sep[0][0] != '[' and sep[0][0] != '(':
            raise ValueError("This is an invalid input.")
        if sep[1][-1] != ')' and sep[1][-1] != ']':
            raise ValueError("This is an invalid input.")

        def isInt(num):
            """Check if it is a valid number"""
            try:
                int(num)
                return True
            except ValueError:
                return False
        #storing the numbers, avoiding strings or blanks
        try:
            if isInt(sep[0][-1]):
                self.left = int(sep[0][1:])
            else:
                self.left = int(sep[0][1:-1])
            if isInt(sep[1][0]) or sep[1][0] == '-':
                self.right = int(sep[1][0:-1])
            else:
                self.right = int(sep[1][1:-1])
        except ValueError:
            raise ValueError("This is an invalid input.")
            
        #saving lower and upper bounds, check for invalid ranges
        self.lower = sep[0][0]
        self.upper = sep[1][-1]
        if self.left > self.right and self.lower == '[' and self.upper == ']':
            raise ValueError("This is an invalid input.")
        if self.left >= self.right - 1 and self.lower == '(' and self.upper == ')':
            raise ValueError("This is an invalid input.")
        if self.left >= self.right and self.lower == '(' and self.upper == ']':
            raise ValueError("This is an invalid input.")
        if self.left >= self.right and self.lower == '[' and self.upper == ')':
            raise ValueError("This is an invalid input.")
    
    
    def __repr__(self):
        """String representation"""
        return self.lower + str(self.left) + "," + str(self.right) + self.upper
        
def convert_list(inputs):
    """convert user input into list of intervals"""
	#Check if input is string
    if not isinstance(inputs, str):
        raise ValueError("You need to input a string")
    inputs = inputs.strip()
    intervals = []
    sep = inputs.split(",")
    #the length of sep should be a multiple of two, since every interval can be split into two parts
    if len(sep) % 2 != 0:
        raise ValueError("Input intervals not valid.")
    #create a new intervals list
    for i in range(0, len(sep), 2):
        each = ",".join([sep[i].strip(), sep[i + 1].strip()])
        intervals.append(interval(each))
    return mergeOverlapping(intervals)
        

def mergeIntervals(int1, int2):
    """Merging two intervals"""
    if mergeable(int1, int2) == False:
        raise ValueError("These two can't be merged.")
    #first check for lower bound numbers, then upper bounds
    if int1.left <= int2.left:
        if int1.right >= int2.left - 1:
            if int1.right > int2.right:
                return int1
            else:
                return (interval(str(int1)[0] + str(int1.left) + ', ' + str(int2.right) + str(int2)[-1]))
        else:
            raise Exception('The intervals cannot be merged')
    else:
        if int1.left <= int2.right + 1:
            if int1.right > int2.right:
                return (interval(str(int2)[0] + str(int2.left) + ', ' + str(int1.right) + str(int1)[-1]))
            else:
                return (int2)
        else:
            raise Exception('The intervals cannot be merged')
    


def mergeable(int1, int2):
    """Check whether two intervals are mergeable"""
    if not isinstance(int1, interval):
        raise ValueError("Please enter valid intervals.")
    if not isinstance(int2, interval):
        raise ValueError("Please enter valid intervals.")
    if (int1.left == int2.right + 1) and (int1.lower == '[') and (int2.upper == ']'):
        return True
    if (int2.left == int1.right + 1) and (int2.lower == '[') and (int1.upper == ']'):
        return True
    if int1.right < int2.left or int2.right < int1.left:
        return False
    if int1.upper == ')' and int2.lower == '(' and int1.right == int2.left:
        return False
    if int2.upper == ')' and int1.lower == '(' and int2.right == int1.left:
        return False
    return True


def mergeOverlapping(intervals):
    """merging a list of intervals"""
    if len(intervals) == 0:
        return []
    #if not isinstance(intervals, list):
    #    raise ValueError("Please input a list")
    try:
        intervals.sort(key = lambda x: x.left)
    except AttributeError:
        raise ValueError("They can't be merged.")

    merged_Intervals = []
    merging = intervals[0]
    
    #iterate through the list, merging two by two
    for inter in intervals[1:]:
        if mergeable(merging, inter):
            merging = mergeIntervals(merging, inter)
        else:
            merged_Intervals.append(merging)
            merging = inter
    merged_Intervals.append(merging)

    return merged_Intervals


def insert(intervals, newint):
    """inserting new interval into lists of intervals"""
    if not isinstance(intervals, list):
        raise ValueError("Please input a valid list.")
    if not isinstance(newint, interval):
        raise ValueError("Please input a valid interval.")
    return mergeOverlapping(intervals + [newint])

