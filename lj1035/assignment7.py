import MyPackage.interval as interval
import sys

# This is the main function to prompt the user for inputs, handle the inputs using functions, and display outputs.
def main():
    initial_intervals = []
    while True:
        try:
            user_input = input('List of intervals? ')
        except EOFError:
            sys.exit(0)
        initial_intervals = []
        try:
            for i in user_input.split(', '):
                interval_i = interval.interval(i)
                initial_intervals.append(interval_i)
            break
        except ValueError as e:
            print(e)
        except:
            print('Other unexpected errors.')
    while True:
        try:
            user_input = input('Interval? ')
        except EOFError:
            sys.exit(0)
        if user_input == 'quit':
            break
        try:
            new_interval = interval.interval(user_input)
            insert_intervals = interval.insert(initial_intervals, new_interval)
            intervals_to_strings = ", ".join(repr(x) for x in insert_intervals)
            print(intervals_to_strings)
            continue
        except ValueError as e:
            print(e)
        except:
            print('Other unexpected errors.')


if __name__ == '__main__':
    main()