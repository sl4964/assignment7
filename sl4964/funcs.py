'''
This is where all the functions and classes are defined.
@author: ShashaLin
'''
from Errors import MergeError, InputError

lowerbounds = ('(', '[')
upperbounds = (')', ']')
        

class interval(object):
    
    'The interval class represents the range of integers between two bounds.'
    
    def __init__(self, readin):
        '''the constructor ensures the argument for class interval is
        of correct format'''
        
        try: 
            li = readin.split(',')
        except:
            InputError('input has to include two numbers, with a comma in between.')
        if ' ' in list(readin):
            raise InputError('space in interval is not allowed.')   
        
        if li[0][0] not in lowerbounds or li[-1][-1] not in upperbounds:
            
            raise InputError ('Your input is not of the right format.\
            \n The input has to be a correct mathematical representation\
            of an interval with either closed or open bounds. \n \
            Example: [5, 7)')
            
        elif li[0][0] == lowerbounds[1] and li[-1][-1] == upperbounds[1] and int(li[0][1:]) > int(li[-1][: -1]):
            raise InputError('The lower bound has to be smaller or equal to the upper bound for inclusive intervals.')
            
        elif li[0][0] == lowerbounds[0] and li[-1][-1] == upperbounds[0] and int(li[0][1:]) >= int(li[-1][: -1]) - 1:
            raise InputError('The lower bound has to be smaller than upper bound - 1f or intervals with exclusive bounds on both sides') 
            
        elif (li[0][0] == lowerbounds[0] and li[-1][-1] == upperbounds[1] and int(li[0][1:]) >= int(li[-1][: -1])) \
        or (li[0][0] == lowerbounds[1] and li[-1][-1] == upperbounds[0] and int(li[0][1:]) >= int(li[-1][: -1])):
            raise InputError('The lower bound has to be smaller than upper bound if one bound is inclusive and the other inclusive.')
         
        else:   
            self.interva = readin
            return None
    
    def __str__(self):
        return "{}".format(self.interva)
            
def mergeIntervals(inta, intb):
    
    int1 = inta.split(',')
    int2 = intb.split(',')
    
    int1a = int(int1[0][1:]) #lower number for int1
    int1b = int(int1[-1][: -1]) #upper number for int1
    int2c = int(int2[0][1:]) #lower number for int2
    int2d = int(int2[-1][: -1]) #upper number for int2
    
    int1b1 = int1[0][0] #lowerbound for int1
    int1b2 = int1[-1][-1] #upperbound for int1
    
    int2b1 = int2[0][0] #lowerbound for int1
    int2b2 = int2[-1][-1] #upperbound for int1
    
    if int1a != int1b:
        if int1b == int2c:
            if int1b2 ==upperbounds[0] and int2b1==lowerbounds[0]:
                raise MergeError()
            else: intNew = int1[0] + ',' + int2[-1]
        
        elif int1b - int2c ==-1:
            if int1[-1][-1] == upperbounds[1] and int2[0][0]== lowerbounds[1]: #and\
            #int(int1[-1][: -1]) - int(int2[0][1:]) < -1:
                intNew = int1[0] + ',' + int2[-1]
                
            elif int1[-1][-1] == upperbounds[1] and int2[0][0]== lowerbounds[1]: #and int(int1[-1][: -1]) - int(int2[0][1:])\
            #== -1 and int1[0][0] != lowerbounds[0] and int1[0][0] != upperbounds[0]:
                intNew = int1[0] + ',' + int2[-1]
                
            else: raise MergeError()
    
        elif int1b - int2c < -1:
            raise MergeError()
    
        else:
            if int2c > int1a:
                if int2d == int1b:
                    if int2b2 == int1b2 == upperbounds[0]:
                        intNew = inta
                    elif int2b2 == upperbounds[0] and int1b2 == upperbounds[1]:
                        intNew = inta
                    elif int2b2 == upperbounds[1] and int1b2 == upperbounds[0]:
                        intNew = int1[0] + ',' + int2[1]
                    else:
                        intNew = inta
                        
                elif int2d < int1b:
                        intNew = inta
                else: 
                    intNew = int1[0] + ',' + int2[1]
                    
            elif int2c < int1a or (int2c == int1a and int1b1 != lowerbounds[1]):
                if int2d < int1a - 1:
                    raise MergeError()
                
                elif int2d == int1a - 1:
                    if int2b2 == upperbounds[1] and int1b1 == lowerbounds[1]:
                        intNew = int2[0] + ',' + int1[1]
                    else:
                        raise MergeError()
                    
                elif int2d == int1a:
                    if int2b2 == upperbounds[0] and int1b1 == lowerbounds[0]:
                        raise MergeError()
                    else:
                        intNew = int2[0] + ',' + int1[1]
                        
                elif int1a < int2d and  int2d < int1b:
                    intNew = int2[0] + ',' + int1[1]
                    
                
                elif int2d == int1b:
                    if int2b2 == upperbounds[0]:
                        intNew = int2[0] + ',' + int1[1]
                    else: 
                        intNew = int2[0] + ',' + int2[1]
                        
                else:
                    intNew = intb
            
            else: 
                if int2d < int1a - 1:
                    raise MergeError()
                
                elif int2d == int1a - 1:
                    if int2b2 == upperbounds[1] and int1b1 == lowerbounds[1]:
                        intNew = int1[0] + ',' + int1[1]
                    else:
                        raise MergeError()
                    
                elif int2d == int1a:
                    if int2b2 == upperbounds[0] and int1b1 == lowerbounds[0]:
                        raise MergeError()
                    else:
                        intNew = int1[0] + ',' + int1[1]
                        
                elif int1a < int2d < int1b:
                    intNew = int1[0] + ',' + int1[1]
                    
                
                elif int2d == int1b:
                    if int2b2 == upperbounds[0]:
                        intNew = int1[0] + ',' + int1[1]
                    else: 
                        intNew = int1[0] + ',' + int2[1]
                else:
                    intNew = intb
    
    else:
        if int2c == int2d:
            if int1b == int2c:
                intNew = inta
            else:
                raise MergeError()
        else: 
            if int1b == int2c:
                intNew = int1[0] + int2[-1]
            elif int2d > int1b > int2c:
                intNew = intb
            elif int2d == int1b:
                intNew = int2[0] + ',' + int1[1]
            else:
                if int2b2 == upperbounds[0]:
                    raise MergeError()
                else:
                    if int1b == int2d + 1:
                        intNew = int2[0] + ',' + int1[1]
                    else:
                        raise MergeError()
                    
    
    return intNew
                 
                
def mergeOverlapping (inter):
    inter = inter.split(', ')
    inter.sort(key = lambda x: int(x.split(',')[0][1:]))
    
    i = 0 #counter or the list of intervals
    originalLength = len(inter)
    while i < originalLength - 1:
        #print(intervals)
        try: 
            
            inter.append(mergeIntervals(inter[i], inter[i+1]))
           
            del(inter[i])
            del(inter[i])
            
            inter.sort(key = lambda x: int(x.split(",")[0][1:]))
            
        except: 
            i = i + 1
    inter = ', '.join(inter)
    return inter
                
def insert(inter1, newint):
    inter1 = inter1 + ', ' + newint
    
    result = mergeOverlapping(inter1)
    
    return result 