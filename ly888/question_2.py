def mergeIntervals(int1, int2):
    #Find the left and right bracket for the two input intervals
    bracket1=list(int1);
    b_left1=bracket1[0];
    b_right1=bracket1[-1];
    bracket2=list(int2);
    b_left2=bracket2[0];
    b_right2=bracket2[-1];
    #Find the lower and upper value of the two input intervals
    lower1=int(int1[1:-1].split(",")[0]);
    upper1=int(int1[1:-1].split(",")[1]);
    lower2=int(int2[1:-1].split(",")[0]);
    upper2=int(int2[1:-1].split(",")[1]); 
    
    #Find the smallest and largest integers in these two intervals separately
    if b_left1=='(':
        lower1_inter=lower1+1;
    else:
        lower1_inter=lower1;
    if b_left2=='(':
        lower2_inter=lower2+1;
    else:
        lower2_inter=lower2;
    if b_right1==')':
        upper1_inter=upper1-1;
    else:
        upper1_inter=upper1;
    if b_right2==')':
        upper2_inter=upper2-1;
    else:
        upper2_inter=upper2; 
        
    #Do the intersection for these two input intervals
    try:
        if lower1_inter-upper2_inter<=1 and lower2_inter-upper1_inter<=1:
            #The intervals have overlap
            seq=[lower1_inter,lower2_inter,upper1_inter,upper2_inter];
            merge_lower=min(seq);
            merge_upper=max(seq);
            #Print the merged interval 
        else:
            raise ValueError('No overlap for the intervals')
        return ([merge_lower,merge_upper])
    except:
        return 'No overlap for the intervals'