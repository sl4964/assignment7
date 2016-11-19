from interval import interval
from interval import insert

'''
Prompts the user a list of intervals and a single interval. Return a merged interval every time, keep 
merging and returning interval until quit. 
'''
def main():
    interval_list = raw_input('List of intervals?')
    split_intlist=interval_list.split(", ")
    result = [interval(i) for i in split_intlist]
    
    try:
        split_intlist=interval_list.split(", ")
        result = [interval(i) for i in split_intlist]         #list holds for the interval objects
    except ValueError:
        print('Invalid interval')
    except IndexError:
        print('Invalid interval')
        
    
    while True:
        input_str = raw_input('Interval?').lower()
        if input_str == 'quit':
            exit('End')
        try:
            newint = interval(input_str)
            result=insert(result,newint)
            str_re = [str(i) for i in result] 
            join_str = ', '.join(str_re)
            print (join_str) 
            
        except ValueError:
            print('Invalid interval')  
    

if __name__ == '__main__':
    print('Please prompt a list of intervals and other intervals to mere into list, only integers accepted')
    print("Hint: exit by enter 'quit' ")
    main()
    
    
    
    