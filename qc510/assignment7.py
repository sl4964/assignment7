from interval import *
####program to run the code and test
'''
1.use class and functions that we just defined 
2.prompts the user for a list of intervals like ('[-10,-7], (-4,1], [3,6), (8,12), [15,23]')
->so put into merge overlapping list?
3.reads a string from the user: like ('(3,7]')
-> put into insert(merged, newint)
4.display the list at each operation. 
so quit? after that? 
'''
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


