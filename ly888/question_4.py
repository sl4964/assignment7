from question_2 import mergeIntervals
from question_3 import mergeOverlapping

def insert(intervals,newint):
    #Combine all the intervals together
    intervals.append(newint);
    #Merge all the intervals
    merge_intervals=mergeOverlapping(intervals);
    #Order the merged intervals
    merge_intervals=sorted(merge_intervals,key=lambda x:x[0]);
    return merge_intervals