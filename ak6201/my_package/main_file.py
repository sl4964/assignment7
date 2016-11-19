import re
class interval:
    valid_string = 1   #to check if the input interval is valid ornot
    to_form_list = 1   
    def __init__(self, x, to_print_or_not):  # the second argument (to_print_or_not) is to print the error message only when the function is called. It is not printed when it is run for test cases
        try: 
            x = "".join(x.split()) # to remove all the spaces in the input string 
            interval_values = list(map(int, re.findall("[-\d]+", x)))  # to extract all the values in integer  from the input string
            if len(interval_values) != 2:
                self.valid_string = 0
                raise ValueError
            elif x[0] == '[' and x[-1] == ']':
                if interval_values[0] > interval_values[1]:
                    self.valid_string = 0
                    raise ValueError
                else:
                    self.valid_string = 1
            elif x[0] == '(' and x[-1] == ']':
                if interval_values[0] >= interval_values[1]:
                    self.valid_string = 0
                    raise ValueError
                else:
                    self.valid_string = 1
            elif x[0] == '[' and x[-1] == ')':
                if interval_values[0] >= interval_values[1]:
                    self.valid_string = 0
                    raise ValueError
                else:
                    self.valid_string = 1
            elif x[0] == '(' and x[-1] == ')':
                if interval_values[0] >= (interval_values[1]-1):
                    self.valid_string = 0
                    raise ValueError
                else:
                    self.valid_string = 1
            else:
                self.valid_string = 0
        except ValueError:
            if to_print_or_not == 1:
                print("Invalid Input") # It raises the error and prints it. It doesnt print when it is run for unit tests
        
    def calc(self, int1, int2, values_int1, values_int2):  # calc method is to help execute the mergeIntervals function
        if values_int2[1] < values_int1[1]:
            st = int1[0] + str(values_int1[0]) + ',' + str(values_int1[1]) + int1[-1]
        elif values_int2[1] > values_int1[1]:
            if values_int1[0] == values_int2[0]:
                if int1[0] == '[' or int2[0] == '[':
                    a = '['
                else:
                    a = '('
            else:
                a = int1[0]
            st = a + str(values_int1[0]) + ',' + str(values_int2[1]) + int2[-1]
        else:
            if int1[-1] == ']' or int2[-1] == ']':
                st = int1[0] + str(values_int1[0]) + ',' + str(values_int2[1]) + ']'
            else:
                st = int1[0] + str(values_int1[0]) + ',' + str(values_int2[1]) + ')'
        return st
                    
    def  mergeIntervals(self, int1, int2, to_print_or_not):  # the second argument (to_print_or_not) is to print the error message only when the function is called. It is not printed when it is run for test cases
        int1 = "".join(int1.split())
        int2 = "".join(int2.split())
        values_int1 = list(map(int, re.findall("[-\d]+", int1)))
        values_int2 = list(map(int, re.findall("[-\d]+", int2)))
        try:
            if int1[-1] == ')' and int2[0] == '(' and values_int1[1] > values_int2[0]:
                return (self.calc(int1, int2, values_int1, values_int2))
            elif int1[-1] == ']' and int2[0] == '(' and values_int1[1] >= values_int2[0]:
                return (self.calc(int1, int2, values_int1, values_int2))
            elif int1[-1] == ')' and int2[0] == '[' and values_int1[1] >= values_int2[0]:
                return (self.calc(int1, int2, values_int1, values_int2))
            elif int1[-1] == ']' and int2[0] == '[' and values_int1[1] >= (values_int2[0]-1):
                return (self.calc(int1, int2, values_int1, values_int2))
            else:
                raise ValueError
        except ValueError:
            if to_print_or_not == 1:
                print("The two intervals cannot be overlapped") # It raises the error and prints it. It doesnt print when it is run for unit tests
            return -1
        
    def mergeOverlapping(self, intervals):
        if self.to_form_list == 1:
            list_of_intervals = []
            intervals = "".join(intervals.split())  # to remove all the spaces in the input string
            i = 0
            while i < len(intervals):
                new_interval = ''
                new_interval += intervals[i]
                i += 1 
                while (intervals[i] != ']' and intervals[i] != ')'):
                    new_interval += intervals[i]
                    i += 1   
                new_interval += intervals[i]
                list_of_intervals.append(new_interval)
                i +=2
            intervals = list_of_intervals   
        
        result = []
        i = 0
        while i < len(intervals):
            if i == 0:
                combined_interval = self.mergeIntervals(intervals[i], intervals[i+1], 0)
                i += 1
            else:
                combined_interval = self.mergeIntervals(result[-1], intervals[i], 0)
            
            
            if combined_interval == -1:
                if i == 1:
                    result.append(intervals[0])
                result.append(intervals[i])
                
            else:
                if len(result) > 0:
                    del result[-1]
                result.append(combined_interval)
                
            i += 1
        
        return(result)
                
    def insert(self, intervals, newint):
        self.__init__(newint, 0)
        if self.valid_string == 0:
            return ("Invalid Input")
        else:
            self.to_form_list = 0
            intervals = "".join(intervals.split())
            list_of_intervals = []
            i = 0
            while i < len(intervals):
                new_interval = ''
                new_interval += intervals[i]
                i += 1 
                while (intervals[i] != ']' and intervals[i] != ')'):
                    new_interval += intervals[i]
                    i += 1   
                new_interval += intervals[i]
                list_of_intervals.append(new_interval)
                i +=2
    
            i = len(list_of_intervals) - 1
            flag = 0
            while i >= 0 :
                
                values_int1 = list(map(int, re.findall("[-\d]+", list_of_intervals[i])))
                values_newint = list(map(int, re.findall("[-\d]+", newint)))
                if values_newint[0] >= values_int1[0]:
                    list_of_intervals.insert(i+1, newint)
                    flag = 1
                    break
                i -=1
                
            if flag == 0:
                list_of_intervals.insert(0, newint)
                
            return(self.mergeOverlapping(list_of_intervals))
            







