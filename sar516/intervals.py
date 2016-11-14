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