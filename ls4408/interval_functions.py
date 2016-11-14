
class interval(object):
    '''This is a class used to create an valid interval object, if an valid interval could not be created
        an ValueError exception would be raised'''
    def __init__(self,input_string):
        self.left=input_string[0]
        self.right=input_string[-1]
        if self.left not in ["[","("]:
            raise ValueError("interval has invalid left-end symbol")
        if self.right not in ["]",")"]:
            raise ValueError("interval has invalid right-end symbol")
        #make sure the bound symbols of the interval are valid
        
        filter_input_string=input_string.replace('[',' ').replace(']',' ').replace('(',' ').replace(')',' ').split(',')
        filter_input_string=[int(i) for i in filter_input_string]
        if len(filter_input_string) != 2:
            raise ValueError("interval is invalid")
        #make sure the interval only has two intergers after replacing brackets or parenthesis
        
        self.left_value=filter_input_string[0]
        self.right_value=filter_input_string[-1]
        #return values of two intergers in an interval
        
        '''the commands below make sure the interval is not empty'''
        if (self.left=="[") and (self.right=="]"):
            if self.left_value > self.right_value:
                raise ValueError('invalid [] interval')
                #checks [] interval
        elif (self.left=="(") and (self.right==")"):
            if self.left_value >= self.right_value-1:
                raise ValueError('invalid () interval')
                #check () interval
        else:
            if self.left_value >= self.right_value:
                raise ValueError('invalid [) or (]) interval')
                #check [) and (] interval
           
    #methods:
    def __repr__(self):
        string=self.left+str(self.left_value)+","+str(self.right_value)+self.right
        return string
    #returns string of the interval

class MergeError(Exception):
    def __str__(self):
        return 'Unable to merge!\n'
# Define a new exception called MergeError when two intervals could not be merged.

'''mergeInterval function is used to merge two intervals''' 
def mergeInterval(int1,int2):
    '''It first raise errors for unadjacent intervals'''
    if int1.right_value < int2.left_value:
        if int1.right_value+1==int2.left_value and int1.right=="]" and int2.left=="[":
            merge=int1.left+str(int1.left_value)+int2.right+str(int2.right_value)
        else:
            raise MergeError
            #raise MergeError for unadjacent intervals
    if int2.right_value < int1.left_value:
        if int2.right_value+1==int1.left_value and int2.right=="]" and int1.left=="[":
            merge=int2.left+str(int2.left_value)+int1.right+str(int1.right_value)
        else:
            raise MergeError
            #raise MergeError for unadjacent intervals
    elif int1.right_value == int2.left_value:
        if int1.right==")" and int2.left=="(":
            raise MergeError 
        else:
            merge=int1.left+str(int1.left_value)+int2.right+str(int2.right_value)
            #raise MergeError for unadjacent intervals with (),() conditions
    elif int2.right_value == int1.left_value:
        if int2.right==")" and int1.left=="(":
            raise MergeError 
        else:
            merge=int2.left+str(int2.left_value)+int1.right+str(int1.right_value)
               #raise MergeError for unadjacent intervals with (),() conditions
    
    else:
        merge_left_value = min(int1.left_value, int2.left_value)
        #determine the lower bound
        if int1.left_value==int2.left_value:
            if int1.left != int2.left:
                merge_left="["
            else:
                merge_left=int1.left
        else:
            if int1.left_value<int2.left_value:
                merge_left=int1.left
            else:
                merge_left=int2.left
        #detemine the lower bound symbol
        
        merge_right_value = max(int1.right_value, int2.right_value)
        #determine the higher bound
        if int1.right_value==int2.right_value:
            if int1.right != int2.right:
                merge_right="]"
            else:
                merge_right=int1.right
        else:
            if int1.right_value<int2.right_value:
                merge_right=int2.right
            else:
                merge_right=int1.right
        merge=merge_left+str(merge_left_value)+','+str(merge_right_value)+merge_right
        #determin higher bound symbol
    return(interval(merge))

'''mergeOverlapping is used to merge a list of intervals
  We first use the interval with lowest left bound value and try to merge with other intervals 
  in orders of left bound value of other intervals.When it could not merge with an interval, en exception is raised.
  We handled the exception by using that unmerging interval to merge with other interval in a way similar to the previous 
  merging process. We iterare the merging process until last interval is handled.

'''
def mergeOverlapping(intervals):
        intervals = sorted(intervals, key=lambda x: x.left_value)
        i=0 
        #sort the intervals by its left bound
        merge2=[]
        while(i+1<=len(intervals)):
            s=intervals[i]
            while (i+1 <= len(intervals)):
                try:
                    s=mergeInterval(s,intervals[i])
                    i=i+1
                    merge=s
                except MergeError:
                    i=i
                    merge2.append(merge)
                    break
        merge2.append(merge)
        return merge2

'''insert function is achieved by appending the new interval to the existing interval list 
    and merge
'''
def insert(intervals, newint):
    intervals.append(newint)
    return mergeOverlapping(intervals)
    