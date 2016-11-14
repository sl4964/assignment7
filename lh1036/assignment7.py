from interval import *
from IPython.core.debugger import prompt

class QuitError(Exception):
    pass

def quittingInput(prompt):
    '''
    Program will stop running if user types "quit" and raises QuitError
    '''
    userinput = input(prompt)
    
    if userinput == "quit":
        raise QuitError()
    
    return userinput

def promptForList():
    '''
    Prompt for keyboard input of initial list of intervals until valid list is input
    Raises ValueError if list is invalid
    '''
    while True:
        try:
            userinput = quittingInput("List of intervals? ")
            return interval.parseList(userinput)
        
        except ValueError:
            print("Invalid list")

def promptForInterval():
    '''
    Continue prompting user for additional intervals
    Raises ValueError if user input is invalid interval
    '''
    while True:
        try:
            return interval(quittingInput("Interval? "))
        
        except ValueError:
            print("Invalid interval")
    
if __name__ == "__main__":
    try:
        intervals = promptForList()
        
        while True:
            intervals = insert(intervals, promptForInterval())
            print(intervals)
    
    except QuitError:
        pass

