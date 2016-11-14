from question_2 import mergeIntervals

def mergeOverlapping(intervals):
    #Count the length of the input interval list
    n=len(intervals);
    intervals_2=list(range(n));
    #Change all the intervals into format []
    for i in range(n):
        inter=intervals[i];
        bracket=list(inter);
        b_left=bracket[0];
        b_right=bracket[-1];
        lower=int(inter[1:-1].split(",")[0]);
        upper=int(inter[1:-1].split(",")[1]);
        if b_left=='(':
            lower_inter=lower+1;
        else:
            lower_inter=lower;
        if b_right==')':
            upper_inter=upper-1;
        else:
            upper_inter=upper;
        intervals_2[i]=[lower_inter,upper_inter];
    
    #Sort these intervals by their first element (smallest integer in this interval)
    intervals_2=sorted(intervals_2,key=lambda x:x[0]);
    
    #Merge the intervals one by one
    merge_intervals=[];
    s=intervals_2[0];
    for i in range(1,n):
        merge_before=s;
        s=mergeIntervals(str(s), str(intervals_2[i]));
        if s=="No overlap for the intervals" and i<n-1:
            #If current interval i is not the last one and cannot merge with next interval, we will save current merge and start next one
            merge_intervals.append(merge_before);
            s=intervals_2[i];
        elif s!="No overlap for the intervals" and i==n-1:
            #If current interval i is the last one and can merge with before, we will save after merge
            merge_intervals.append(s);
        elif s=="No overlap for the intervals" and i==n-1:
            #If current interval i is the last one and cannot merge with before, we will save current merge and the last interval separately
            merge_intervals.append(merge_before);
            merge_intervals.append(intervals_2[i]);
    return merge_intervals