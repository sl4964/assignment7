"""Class called interval that represents the range of integers between a lower bound and an upper bound"""

#Question 1 of HW7
#input should be an interval in a string representation
class interval:
    def __init__(self, interval):
        self.interval = interval
        
        #Preprocessing the input interval
        pre_int = list(interval)
        
        #Exclude the input which does not contain '(' or '[' at the beginning or does not contain ')' or ']' at the end
        #Or does not contain ","
        if pre_int[0] in ('(','[') and pre_int[-1] in (')',']') and "," in pre_int:
            #Seek the lower-bound number and upper-bound number from the interval string
            numbers_str = interval[1:-1].split(",")
            lower_str = numbers_str[0]
            upper_str = numbers_str[1]
        else:
            lower_str = '9999'
            upper_str = '-9999'
        
        #Check whether the string "numbers" are the true integers
        #If not, return lower_int as a large number (e.g. 9999) which is bigger than upper_int
        #By doing this, we can exclude unexpected bound number input (e.g., "a", "b9", "1s4s*")
        if lower_str.lstrip('-').isdigit() and upper_str.lstrip('-').isdigit() is True:
            lower_int = int(lower_str)
            upper_int = int(upper_str)
        else:
            lower_int = 9999
            upper_int = -9999
        
        #Find lower bound and upper bound
        lower_bd = interval[0]
        upper_bd = interval[-1]

        #Explain the bounds and exclude unexpected bound input (e.g., "{2,3}", "*9,6]")
        if lower_bd == '(' and upper_bd == ')':
            self.lower_value = lower_int + 1
            self.upper_value = upper_int - 1
        elif lower_bd == '[' and upper_bd == ')':
            self.lower_value = lower_int
            self.upper_value = upper_int - 1
        elif lower_bd == '(' and upper_bd == ']':
            self.lower_value = lower_int + 1
            self.upper_value = upper_int
        elif lower_bd == '[' and upper_bd == ']':
            self.lower_value = lower_int
            self.upper_value = upper_int
        else:
            self.lower_value = 9999
            self.upper_value = -9999
                    
    def __repr__(self):
        # check input validation and print result 
        prompt = '%s represents the numbers %d through %d' % (self.interval, self.lower_value, self.upper_value)
       
        if self.lower_value > self.upper_value:
            return "Invalid interval"
        else:
            return prompt