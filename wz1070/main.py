import interval

if __name__ == '__main__':
    list_of_intervals = input('List of intervals?')
    intervals = []
    temp = ''
    first = True
    for i in range(len(list_of_intervals)):
        if list_of_intervals[i] != ',':
            if list_of_intervals[i] != ' ':
                temp += list_of_intervals[i]
        elif first:
            first = False
            temp += list_of_intervals[i]
        else:
            print(temp)
            temp_int = interval(temp)
            intervals.append(temp_int)
            temp = ''
            first = True
    temp_int = interval(temp)
    intervals.append(temp_int)
    print(intervals)
    notQuit = True
    while notQuit:
        input_string = input('Interval?')
        if input_string == 'quit':
            break
        elif input_string[0] != '[' and input_string[0] != '(':
            print('Invalid interval0')
            continue
        lower_string = ''
        higher_string = ''
        first = True
        for i in range(1, len(input_string) - 1):
            if input_string[i] == ',':
                first = False
                continue
            if first:
                lower_string += input_string[i]
            elif input_string[i] != ' ':
                higher_string += input_string[i]
        lower = int(lower_string)
        higher = int(higher_string)
        if input_string[0] == '[' and input_string[len(input_string) - 1] == ']' and lower > higher:
            print('Invalid interval1')
            continue
        elif input_string[0] == '(' and input_string[len(input_string) - 1] == ')' and lower >= higher - 1:
            print('Invalid interval2')
            continue
        elif input_string[0] == '[' and input_string[len(input_string) - 1] == ')' and lower >= higher:
            print('Invalid interval3')
            continue
        elif input_string[0] == '(' and input_string[len(input_string) - 1] == ']' and lower >= higher:
            print('Invalid interval4')
            continue
        newint = interval(input_string)
        intervals = insert(intervals, newint)
        print(intervals)