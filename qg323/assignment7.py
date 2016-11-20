
import sys
from interval import *


if __name__ == '__main__':
    while True:
        try:
            interval_list_string = input(
                    'List of intervals (comma separated)?'
                    )
        except EOFError:
            # Allow users to enter Ctrl+D (on *nix) to exit
            sys.exit(0)

        try:
            interval_list_string = interval_list_string.strip()
            # For empty string, we yield an empty list.
            if interval_list_string == '':
                interval_list = []
                break

            comma_subs = interval_list_string.split(',')

            # We expect that there are odd number of commas: for n intervals,
            # there are n commas for each interval, and (n-1) commas for
            # separating those intervals.  This is equivalent to having
            # an even number of substrings separated by commas.
            if len(comma_subs) % 2 != 0:
                raise ValueError('invalid list')
            interval_list = [','.join(comma_subs[i:i+2])
                    for i in range(0, len(comma_subs), 2)]
            interval_list = [interval.fromString(i) for i in interval_list]
            break
        except ValueError as e:
            # We output the error message and let the user try again.
            print(str(e))

    while True:
        try:
            input_string = input('Interval?')
            if input_string.lower() == 'quit':
                break
            i = interval.fromString(input_string)
            interval_list = insert(interval_list, i)
            print(', '.join([str(i) for i in interval_list]))
        except ValueError as e:
            print(str(e))
        except EOFError:
            break
