from interval import *

while True:
    interval_string = input('List of Intervals? ')
    interval_string_list = interval_string.split(', ')
    interval_list = []

    for segment in range(len(interval_string_list)): 
        try:
            x = interval(interval_string_list[segment])
            interval_list.append(x)
            
        except:
            raise ValueError('Invalid input. Intervals should be correctly formatted, and separated by commas')        
            break
                
    break

while True:
    response = input('Interval? ')
    if response == 'quit':
        break
        
    try:
        new_int = interval(response)
        interval_list = insert(interval_list, new_int)
        print(interval_list)
        continue
        
    except:
        print('Invalid interval')
        continue
