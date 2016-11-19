class interval():
    #lower <= upper if both inclusive
    #lower < upper if one inclusive one exclusive
    #lower < upper -1 if both exclusive 
    def __init__(self,interv):
        #Stores the attributes as: lower,front,upper,end,interv.
        try:
            first, second = interv.split(',')
            self.lower = int(first[1:])
            self.front = first[0]
            self.upper = int(second[:-1])
            self.end=second[-1]
            self.interv = interv
            if (interv.startswith("[")) & (interv.endswith("]")):
                if not(self.lower <= self.upper):
                    raise Exception('Invalid Interval')
            if ((interv.startswith("(")) & (interv.endswith("]")))|((interv.startswith("[")) & (interv.endswith(")"))) :
                if not(int(self.lower) < int(self.upper)):
                    raise Exception('Invalid Interval')   
            if (interv.startswith("(")) & (interv.endswith(")")):
                if not(int(self.lower) < (int(self.upper) - 1)):
                    raise Exception('Invalid Interval')
            #handle exception when input is a invalid string
        except:
            raise Exception('Invalid Interval')

def mergeIntervals(int1,int2):
    #Several things to consider when merging two interval
    #i.e. (2,5] and (2,6) kept 6) cuz that's what shows in example
        #first interval
    int1 = interval(int1)
    lower1 = int1.lower
    front1 = int1.front
    upper1 = int1.upper
    end1 = int1.end
    interv1 = int1.interv
        #second interval 
    int2 = interval(int2)
    lower2 = int2.lower
    front2 = int2.front
    upper2 = int2.upper
    end2 = int2.end
    interv2 = int2.interv
    #If i.e. int1 = (1,3] and int2 = [4,5) then it's (1,5) for this case. 
    if((end1=="]")&(front2=="[")&(lower2==upper1+1)):
        return("{}{},{}{}".format(front1,lower1,upper2,end2))
    if((end2=="]")&(front1=="[")&(lower1==upper2+1)):
        return("{}{},{}{}".format(front2,lower2,upper1,end1))
    #For the case cannot merge:
    if((lower1>upper2) | (lower2 > upper1)):
        raise Exception('cannot merge.')
    if((lower1 == upper2)&(end2==")")&(front1=='(')):
        raise Exception('cannot merge.')
    if((lower2 == upper1)&(end1==")")&(front2=='(')):
        raise Exception('cannot merge.')
    #First instance: lower1 < lower2 i.e. int1 = (1,.. int2 = (2,..
    #for example, (2,5) and [3,4) save [3,5)
    if((lower2==lower1+1)&(front1=='(')&(front2=='[')):
        if(upper2<upper1):
            return("[{},{}{}".format(lower2,upper1,end1))
        #if upper2 > upper1 i.e. int1=(1,4) int2 = [2,5) save[2,5)
        elif(upper2>upper1):
            return(int2.interv)
        #if upper1 = upper2, i.e. int2=(1,4) int1= (2,4), keep 4) 
        elif(end1 == end2):
            return(int2.interv)
        #if int1 = (1,4] int2 = 4)
        elif(end1 != end2):
            return("{}{},{}]".format(front2,lower2,upper2))
        #if lower1 = lower2, then compare upper
    #for example, (2,5) and [3,4) save [3,5)
    if((lower1==lower2+1)&(front2=='(')&(front1=='[')):
        if(upper1<upper2):
            return("[{},{}{}".format(lower1,upper2,end2))
        #if upper2 > upper1 i.e. int1=(1,4) int2 = [2,5) save[2,5)
        elif(upper1>upper2):
            return(int1.interv)
        #if upper1 = upper2, i.e. int2=(1,4) int1= (2,4), keep 4) 
        elif(end2 == end1):
            return(int1.interv)
        #if int1 = (1,4] int2 = 4)
        elif(end2 != end1):
            return("{}{},{}]".format(front1,lower1,upper1))
        #if lower1 = lower2, then compare upper
    if(lower1<lower2):
        #if upper1 < upper2 i.e. int1 =(1,3) int2 =(2,4)
        if(upper1<upper2):
            return("{}{},{}{}".format(front1,lower1,upper2,end2))
        #if upper1 > upper2 i.e. int1=(1,4) int2 = (2,3)
        elif(upper1>upper2):
            return(int1.interv)
        #if upper1 = upper2, i.e. int1=(1,4) int2 = (2,4), keep 4) 
        elif(end1 == end2):
            return(int1.interv)
        #if int1 = (1,4] int2 = 4)
        elif(end1 != end2):
            return("{}{},{}]".format(front1,lower1,upper1))
    #Second instance: lower1 > lower 2 , basically the same:
    if(lower2<lower1):
        #if upper2 < upper1 i.e. int2 =(1,3) int1 =(2,4)
        if(upper2<upper1):
            return("{}{},{}{}".format(front2,lower2,upper1,end1))
        #if upper2 > upper1 i.e. int2=(1,4) int1 = (2,3)
        elif(upper2>upper1):
            return(int2.interv)
        #if upper1 = upper2, i.e. int2=(1,4) int1= (2,4), keep 4) 
        elif(end1 == end2):
            return(int1.interv)
        #if int1 = (1,4] int2 = 4)
        elif(end1 != end2):
            return("{}{},{}]".format(front2,lower2,upper2))
    if(lower1==lower2):
        #if upper2 < upper1 i.e. int2 =(1,3) int1 =(2,4)
        if(upper2<upper1):
            if(front1 == front2):
                return(int1.interv)
            else:
                return("[{},{}{}".format(lower1,upper1,end1))
        #if upper2 > upper1 i.e. int2=(1,4) int1 = (2,3)
        elif(upper2>upper1):
            if(front1 == front2):
                return(int2.interv)
            else:
                return("[{},{}{}".format(lower2,upper2,end2))
        #if upper1 = upper2, i.e. int2=(1,4) int1= (2,4), keep 4) 
        elif(end1 == end2):
            return(int1.interv)
        #if int1 = (1,4] int2 = 4)
        elif(end1 != end2):
            return("{}{},{}]".format(front2,lower2,upper2))
    
    
def mergeOverlapping(intervals):
    #intervals is a string that user inputs
    splits = intervals.split(',')
    #element that take in user input and concentrate to intervals
    allelement = []
    #get in 0,1 2,3 ....
    ran = range(int(len(splits)/2))
    splitran = list(map(lambda x: 2*x, ran))
    for i in splitran:
        allelement.append(splits[i].strip()+','+splits[i+1].strip())
    lists = list(map(lambda x: interval(x), allelement))
    si = sorted(lists, key=lambda tup:tup.lower )
    merged = [si[0]]
    inter = []
    for i in range(1,len(si)):
        try:
            inter = mergeIntervals(merged[-1].interv,si[i].interv)
            merged[-1] = interval(inter)
        except Exception:
            merged.append(si[i])
            
    result = list(map(lambda x: x.interv, merged))
    return(result)
    

def insert(intervals,newint):
    intervals.append(newint)
    lists = list(map(lambda x: interval(x), intervals))
    si = sorted(lists, key=lambda tup:tup.lower )
    merged = [si[0]]
    inter = []
    for i in range(1,len(si)):
        try:
            inter = mergeIntervals(merged[-1].interv,si[i].interv)
            merged[-1] = interval(inter)
        except Exception:
            merged.append(si[i])         
    result = list(map(lambda x: x.interv, merged))
    return(result)

if __name__ == "__main__":
    pass
