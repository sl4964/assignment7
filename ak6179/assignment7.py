import interval


def main():
    valid_intervals_list = False
    intervals_list = []
    while not valid_intervals_list:
        try:
            input_string = input("List of intervals?")
            if input_string.lower() == "quit":
                return
            intervals_list = interval.get_intervals_list(input_string)
            valid_intervals_list = True
        except Exception as e:
            print(e)
            print("Invalid list of intervals")
    while True:
        try:
            input_string = input("Interval?")
            if input_string.lower() == "quit":
                return
            it = interval.Interval(input_string)
            intervals_list = interval.insert(intervals_list, it)
            print(intervals_list)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
