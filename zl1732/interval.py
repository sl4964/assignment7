class interval:
    """ constructor, the interval has four instance variable which are two brackets and two numbers """
    def __init__(self, bra1='', s=0, e=0, bra2=''):
        self.bra1=bra1
        self.bra2=bra2
        self.start = s
        self.end = e  
        if self.start > self.end: 
            raise ValueError("Invalid interval")     
        
    """ this function will be used in the next function, which helps to convert user's input(interval list) to interval object
        it takes an string format interval and convert it into one interval object.
    """
    def make_interval_helper(self, input_string):
        obj = interval('[',0,0,']')
        obj.bra1 = str(input_string)[0]
        obj.bra2 = str(input_string)[-1]
        if obj.bra1 not in ['[','('] or obj.bra2 not in [']',')']:
            raise ValueError("Invalid interval")
        try:
            input_string = input_string[1:-1].split(',')  #split two number in a interval
        except:
            raise ValueError("Invalid interval")
        try:
            obj.start = int(input_string[0])
            obj.end = int(input_string[1])
        except:
            raise ValueError("Invalid interval")
        if obj.start > obj.end:
            raise ValueError("Invalid interval") 
        return obj
    
    
    """ This function will convert users interval list into a interval objects list """
    def make_intervals(self, input_string):
        intervals = []
        obj = interval('[',0,0,']')
        try:
            input_string = input_string.split(', ') # split the interval list into single interval
        except:
            raise ValueError("Invalid interval")
        
        for strings in input_string:
            obj = self.make_interval_helper(strings)
            intervals.append(obj)
        return intervals


    """ this function check if two intervals are overlaped, like [2,4] and [3,5]"""
    def is_overlap(self, int1, int2):
        if  int1.end==int2.start and int1.bra2==')' and int2.bra1=='(':
            return False
        elif (int1.end <= int2.end and int1.end >= int2.start) or (int2.end <= int1.end & int2.end >= int2.start):
            return True
        else:
            return False 
    
    """ this function check if two intervals are adjacent, like [1,2] and [3,4]"""
    def is_adjcent(self, int1, int2):
        if int1.end == int2.start-1 and int1.bra2==']' and int2.bra1=='[':
            return True
        
    """ this function will merge two intervals, however, it will not be responsible for checking
        if two intervals are overlapped or adjacent.
    """
    def merge_two(self, int1, int2):
        ans = interval('[',0,0,']')
        ans.start = min(int1.start, int2.start)
        ans.end = max(int1.end, int2.end)
        if int1.start > int2.start:
            ans.bra1 = int2.bra1
        else:
            ans.bra1 = int1.bra1
        
        if int1.end > int2.end:
            ans.bra2 = int1.bra2
        else:
            ans.bra2 = int2.bra2
            
        if int1.start == int2.start:
            ans.bra1=max(int1.bra1, int2.bra1)
        return ans
     
    
    """ This function will check if two interval could be merged and merge them if possible"""
    def mergeIntervals(self, int1, int2):  #two interval object
        if self.is_overlap(int1, int2): #check merge-able or not
            ans = interval('[',0,0,']')
            ans = self.merge_two(int1, int2)
        mergedInterval = ans
        return mergedInterval ######################################## need throw error condition
    

    """ This function will merge multiple intervals and return a list containing merged interval objects"""
    def mergeOverlapping(self, intervals):
        intervals.sort(key = lambda x:x.start)
        length=len(intervals)
        merged=[]
        for i in range(length):
            if merged==[]:
                merged.append(intervals[i])
            else:
                size=len(merged)
                if merged[size-1].end==intervals[i].start and merged[size-1].bra2==')' and intervals[i].bra1=='(':
                    merged.append(intervals[i])
                elif merged[size-1].start<=intervals[i].start<=merged[size-1].end or self.is_adjcent(merged[size-1], intervals[i]):
                    merged[size-1]=self.merge_two(merged[size-1], intervals[i])                   
                else:
                    merged.append(intervals[i])
        overlapInterval =  merged
        return overlapInterval
    
    """ This function will insert a new interval into the existing merged interval list """
    def insert(self, intervals, newint):
        intervals.append(newint)
        mergedult = self.mergeOverlapping(intervals)
        return mergedult
    
    """ This function will check if a interval is overlapped or adjacent to each interval in a list of intervals """
    def check_adjcent(self, intervals, newint):
        for interval in intervals:
            if self.is_adjcent(interval, newint) or self.is_overlap(interval, newint):
                return True
        raise ValueError("Invalid interval")
    
    """ This function will print out the intervals in a list of interval objects """
    def list_print(self, intervals):
        for obj in intervals:
            print(str(obj.bra1)+str(obj.start)+','+str(obj.end)+str(obj.bra2))