import sys
import interval

#PromptUser is the main function that a user interacts with to create intervals
def PromptUser():
    """get list of intervals to start, then get one more interval at a time.
    'quit' or ctrl+c exits"""
    while True:

        try:
            User_input = input("List of intervals?")

            if User_input == 'quit':
                return

            active_intervals = interval.get_interval_list(User_input)
            break

        except KeyboardInterrupt:
            sys.exit()

        except:
            print("Invalid list of intervals")

    while True:

        try:
            User_input = input("Interval?")

            if User_input == 'quit':
                return

            active_intervals = interval.insert(active_intervals, interval.interval(User_input))
            print(active_intervals)

        except KeyboardInterrupt:
            sys.exit()

        except:
            print("Invalid interval")


if __name__ == '__main__':
    PromptUser()
