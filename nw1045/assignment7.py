'''
Created on Nov 7, 2016

@author: Nan Wu
'''
from interval import Interval, mergeOverlapping, insert, InputError

def loop():
    # loop for input of the first list
    while True:   
        try:
            init_IntervalList = input("List of intervals? ")
            init_IntervalList = init_IntervalList.replace(' ', '')
            if init_IntervalList.upper() == 'QUIT':
                exit('End')
            else:
                Intervals=init_IntervalList.split(',')
                IntervalList=[]
                i=0
                if len(Intervals)%2:
                    raise InputError
                else:
                    while (i<len(Intervals)):
                        interval=Intervals[i]+','+Intervals[i+1]
                        i=i+2
                        IntervalList.append(Interval(interval))
                    IntervalList = mergeOverlapping(IntervalList)  
                    break
        except InputError:
            print('Invalid interval!')
            pass
    #loop for Input Interval
    while True:   
        try:
            init_Interval = input("Interval? ")
            init_Interval = init_Interval.replace(' ', '')
            if init_Interval.upper() == 'QUIT':
                exit('End')
            else:
                new_interval = Interval(init_Interval)
                IntervalList = insert(IntervalList,new_interval)
                print (*IntervalList,sep=',')
        except InputError:
            print('Invalid interval!')
            pass

if __name__ == "__main__":
    try:
        print('This is for you to input a list of intervals and other intervals to insert in the list, only integers accepted')
        print('Hint: Exit by QUIT')
        print('Begin')
        loop()
    except EOFError:
        pass