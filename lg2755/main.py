'''
This is the main program.
'''

from Interval import InputTypeException, InputValueException, MergeException, Interval, mergeIntervals, mergeOverlapping, insert

# Takes user input with a string of intervals
intervalStr = input('List of intervals? ')
intervalStr = intervalStr.replace(" ", "")

# Parse the input string into intervals
try:
    intervalStrSplit = intervalStr.split(',')
    intervals = []
    for i in range(0, len(intervalStrSplit), 2):
        singleInterval = intervalStrSplit[i] + ',' + intervalStrSplit[i+1]
        intervals.append(Interval(singleInterval)) 
except InputTypeException:
    print('Invalid interval list')
except InputValueException:
    print('Invalid interval list')
except Exception:
    print('Invalid interval list')

# Insert intervals in the correct position
while True:
    inputStr = input('Interval? ')
    if inputStr == 'quit':
        break
    try:
        interval = Interval(inputStr)
    except InputTypeException:
        print('Invalid interval')
        continue
    except InputValueException:
        print('Invalid interval')
        continue
    except Exception:
        print('Invalid interval')
        continue
    intervals = insert(intervals, interval)
    print(intervals)

