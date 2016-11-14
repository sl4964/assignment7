from interval import *
####program to run the code and test
if __name__ == "__main__":
    quit = False
    intervals = input('Could you provide a list of intervals?')
    inter = mergeOverlapping(intervals)
    printout = []
    newall = inter
    while quit == False:
        try:
            newinter = input('Could you provide another interval?')
            if(newinter=='quit'):
                break
            interval(newinter)       
            printout = insert(inter,newinter)
            print(printout)
            inter = printout
        except:
            print('Invalid interval')


