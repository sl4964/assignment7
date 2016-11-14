class interval: 
    #constructor, create a new interval
    def __init__(self, string_rep):
        lower_string = ''
        higher_string = ''
        first = True
        for i in range(1, len(string_rep) - 1):
            if string_rep[i] == ',':
                first = False
                continue
            if first:
                lower_string += string_rep[i]
            elif string_rep[i] != ' ':
                higher_string += string_rep[i]
        lower = int(lower_string)
        higher = int(higher_string)
        if string_rep[0] == '[' and string_rep[len(string_rep) - 1] == ']' and lower > higher:
            raise NameError('Invalid interval')
        elif string_rep[0] == '(' and string_rep[len(string_rep) - 1] == ')' and lower >= higher - 1:
            raise NameError('Invalid interval')
        elif string_rep[0] == '[' and string_rep[len(string_rep) - 1] == ')' and lower >= higher:
            raise NameError('Invalid interval')
        elif string_rep[0] == '(' and string_rep[len(string_rep) - 1] == ']' and lower >= higher:
            raise NameError('Invalid interval')
        self.left = string_rep[0]
        self.right = string_rep[len(string_rep) - 1]
        self.low = lower
        self.high = higher

    #print override
    def __repr__(self):
        return self.left + str(self.low) + ',' + str(self.high) + self.right

#a = interval('(-11,12]')
#print(a)

#check if two intervals are seperate
def _isSeperate(int1, int2):
    if int1.high < int2.low or int1.low > int2.high:
        return True
    elif int1.high == int2.low and int1.right == ')' and int2.left == '(':
        return True
    elif int1.low == int2.high and int2.right == ')' and int1.left == '(':
        return True
    return False

#merge to intervals if possible
def mergeIntervals(int1, int2):
    if _isSeperate(int1, int2):
        raise NameError('Can not merge')
    else:
        new_high = max(int1.high, int2.high)
        new_low = min(int1.low, int2.low)
        if int1.high == int2.high:
            if int1.right == int2.right:
                new_right = int1.right
            else:
                new_right = ']'
        elif new_high == int1.high:
            new_right = int1.right
        else:
            new_right = int2.right
        if int1.low == int2.low:
            if int1.left == int2.left:
                new_left = int1.left
            else:
                new_left = '['
        elif new_low == int1.low:
            new_left = int1.left
        else:
            new_left = int2.left
    ret = interval(new_left + str(new_low) + ',' + str(new_high) + new_right)
    return ret

#a = interval('[5, 6]')
#b = interval('(4, 7]')
#c = mergeIntervals(a, b)
#print(c)

#merge all possible intervals in a list
def mergeOverlapping(intervals):
    ret = []
    previous = intervals[0]
    for i in range(1, len(intervals)):
        if _isSeperate(previous, intervals[i]):
            ret.append(previous)
            previous = intervals[i]
        else:
            previous = mergeIntervals(previous, intervals[i])
    ret.append(previous)
    return ret

#a = interval('[1, 5]')
#b = interval('[2, 6)')
#c = interval('(8, 10]')
#d = interval('[8, 18]')
#e = mergeOverlapping([a, b, c, d])
#print(e)

#insert a new interval to a list of intervals and merge when possible
def insert(intervals, newint):
    for i in range(len(intervals)):
        if intervals[i].low > newint.low:
            intervals[i - 1] = mergeIntervals(intervals[i - 1], newint)
            ret = mergeOverlapping(intervals)
            return ret
    mergeIntervals(intervals[len(intervals) - 1], newint)
    ret = mergeOverlapping(intervals)
    return ret

#a = interval('[1, 2]')
#b = interval('(3, 5)')
#c = interval('[6, 7)')
#d = interval('(8, 10]')
#e = interval('[12, 16]')
#f = interval('[4, 9]')
#g = insert([a, b, c, d, e], f)
#print(g)