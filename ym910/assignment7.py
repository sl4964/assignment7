from Interval import Interval, IsMergeable, mergeIntervals, mergeOverlapping, insert, MergeError
import sys

def loop():

    '''initial input interval list'''
    while True:
        try:
            int_list=input("List of intervals?")
            

            if int_list.lower()=='quit':
                sys.exit(0)

            int_list=int_list.split(', ')
            intervals=[]

            for intv in int_list:
                intervals.append(Interval(intv))
            intervals=mergeOverlapping(intervals)
            

        except ValueError as message:
            print(message)
        except EOFError:
            sys.exit(0)

            
       '''newly input intervals'''
        while True:
            try:
                new_int=input("Interval?")
                if new_int=='quit':
                    break
                else:
                    new_intlist=insert(intervals,Interval(new_int))
                    print (str(new_int_list)[1:-1])
            except ValueError as message:
                print(message)
            except EOFError:
                sys.exit(0)
        
if __name__ == "__main__":
    loop()


            

            
            
