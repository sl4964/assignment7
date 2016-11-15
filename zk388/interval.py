'''
Created on Nov 14, 2016
This module contains the class interval, which creates interval objects

Assignmnet7
DS-GA-1007

@author: Zahra Kadkhodaie
'''


class interval():

    '''This class creates interval objects. In doing so, it checks for the requirments of valid intervals'''

    def __init__(self, interval_instance):
        '''variables are listed below'''
            
        self.interval_instance = interval_instance
        self.opening = interval_instance[0]
        self.closing = interval_instance.split(',')[1].strip('0,1,2,3,4,5,6,7,8,9, -')
        self.lower = int(interval_instance.strip('[] , ()').split(',')[0])
        self.upper = int(interval_instance.strip('[] , ()').split(',')[1])

    def __repr__(self):
        '''Overloading print method while making sure all the requirements are met.'''
        
        if self.opening == '[' and self.closing == ']' and self.lower > self.upper:
            return 'Invalid interval'
        
        
        elif self.opening == '[' and self.closing == ')' and self.lower >= self.upper:
            return 'Invalid interval'
   
        
        elif self.opening == '(' and self.closing == ']' and self.lower >= self.upper:
            return 'Invalid interval'
       
        
        elif self.opening == '(' and self.closing == ')' and self.lower >= self.upper - 1:
            return 'Invalid interval'
    
        else:
            return self.interval_instance

    def intervalNumbers(self):
        '''This method is defined because it is useful in mergeInterval function. 
        It returns all the values in the interval in a list object'''
        
        if self.opening == '[' and self.closing == ']':
            if self.lower > self.upper:
                return 'Invalid interval'
            else:
                return list(range(self.lower, self.upper + 1))
                
        elif self.opening == '[' and self.closing == ')':
            if self.lower >= self.upper:
                return 'Invalid interval'
            else:
                return list(range(self.lower , self.upper ))

        elif self.opening == '(' and self.closing == ']':
            if self.lower >= self.upper:
                return 'Invalid interval'
            else:
                return list(range(self.lower + 1 , self.upper + 1))
    
        elif self.opening == '(' and self.closing == ')':
            if self.lower >= self.upper - 1:
                return 'Invalid interval'
            else:
                return list(range(self.lower + 1 , self.upper))
            
            
            
            
