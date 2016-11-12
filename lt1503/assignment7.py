import sys
import interval


# prompt_user is the main function that a user interacts with to create intervals
def prompt_user():
    """get list of intervals to start, then get one more interval at a time.
    'quit' or ctrl+c exits"""
    active_intervals = []
    while True:
        try:
            user_input = input("List of intervals?")

            if user_input.lower() == 'quit':
                return

            # Raises a ValueError and loops back if user_input is not correctly structured
            # as a sequence of intervals
            active_intervals = interval.get_interval_list(user_input)
            break

        except KeyboardInterrupt:
            # Exit if the user enters Ctrl+C
            sys.exit(0)
        except EOFError:
            # Exit if the user enters Ctrl+D
            sys.exit(0)

        except ValueError:
            print("Invalid list of intervals")

    # active_intervals maintains a list of intervals merged from the user input so far
    # Here we iteratively ask for more intervals or exit
    while True:

        try:
            user_input = input("Interval?")

            if user_input.lower() == 'quit':
                return

            # Raises a ValueError and loops back if user_input is not a correctly structured interval
            active_intervals = interval.insert(active_intervals, interval.interval(user_input))
            print(active_intervals)

        except KeyboardInterrupt:
            # Exit if the user enters Ctrl+C
            sys.exit(0)
        except EOFError:
            # Exit if the user enters Ctrl+D
            sys.exit(0)

        except ValueError:
            print("Invalid interval")


if __name__ == '__main__':
    prompt_user()
