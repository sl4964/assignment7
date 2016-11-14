from main_file import interval

def loop():
    interval_list = input('> List of intervals? ')
    new_interval = input('> Interval? ')
    
    while((new_interval == 'quit') == False and ((new_interval == 'QUIT') == False) and (new_interval == 'Quit') == False):

        interval_sample = interval(new_interval, 1)
        if interval_sample.valid_string == 1:
            interval_list = interval_sample.insert(interval_list, new_interval)
            interval_list = ', '.join(interval_list)
            print(interval_list)

        new_interval = input('> Interval? ')
    
    
if __name__ == "__main__":
    try:
        loop()
    except EOFError:
        pass