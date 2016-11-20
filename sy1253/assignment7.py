#credit zg475 for references
from sy1253.interval import interval, insert

def loop():
    interval_list = raw_input('List of intervals?')
    Intervals = interval_list.split(", ")
    intervalList = [interval(i) for i in Intervals]
    
    try:
        Intervals = interval_list.split(", ")
        intervalList = [interval(i) for i in Intervals]
    except ValueError:
        print('Invalid interval')
    except IndexError:
        print('Invalid interval')
        
    while True:
        interval_input = raw_input('Interval?')
        if interval_input.upper() == 'QUIT':
            exit('game is over')
        try:
            new_interval = interval(interval_input)
            intervalList = insert(intervalList, new_interval)
            string_trans = [str(i) for i in intervalList] 
            string_join = ', '.join(string_trans)
            print (string_join) 
            
        except Exception:
            print('the interval you enter is invalid, please re-enter again:  ')  
    

if __name__ == '__main__':
    print("please enter a list of valid intervals such as [-10,-7], (-4,1], [3,6)")
    print("you can always quit the program by typing QUIT")
    loop()
    
    
