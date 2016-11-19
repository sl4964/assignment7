import sys

class InvalidIntervalException(Exception):
    pass

class InvalidUserInputException(Exception):
    pass

class interval:
    def __init__(self, interval_input):
        interval.validate_input(interval_input)
        self.__set_left_interval(interval_input.split(",")[0])
        self.__set_right_interval(interval_input.split(",")[-1])
        self.__validate_interval()
        self.string_represenation = interval_input

    def validate_input(user_string):
        if type(user_string) is not str:
            raise InvalidUserInputException("interval_input must be a string")

    def __set_left_interval(self, user_input):
        if user_input[0] == "[":
            interval_type = "inclusive"
        elif user_input[0] == "(":
            interval_type = "exclusive"
        else:
            raise InvalidUserInputException("Invalid interval input")
        self.left = int(user_input[1:len(user_input)]) + (1 if interval_type == "exclusive" else 0)

    def __set_right_interval(self, user_input):
        if user_input[-1] == "]":
            interval_type = "inclusive"
        elif user_input[-1] == ")":
            interval_type = "exclusive"
        else:
            raise InvalidUserInputException("Invalid interval input")
        self.right = int(user_input[0:-1]) - (1 if interval_type == "exclusive" else 0)

    def __validate_interval(self):
        if self.left > self.right:
            raise InvalidIntervalException("Lower bound has to be greater or equal to upper bound")

    def __repr__(self):
        return self.string_represenation

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.left == other.left and self.right == other.right
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

def mergeIntervals(int1, int2):
    if int1.left < int2.left:
        left_int, right_int = int1, int2
    else:
        left_int, right_int = int2, int1

    if left_int.right < right_int.left - 1:
        return None
    else:
        left_inclusion_sign = left_int.string_represenation[0]
        lower_bound = left_inclusion_sign + str(left_int.left - (1 if left_inclusion_sign == "(" else 0))
        interval_with_max_upper_bound = int1 if int1.right > int2.right else int2
        right_inclusion_sign = interval_with_max_upper_bound.string_represenation[-1]
        upper_bound = str(interval_with_max_upper_bound.right + (1 if right_inclusion_sign == ")" else 0)) + right_inclusion_sign
        return interval(lower_bound + "," + upper_bound)

def mergeOverlapping(interval_list):
    if len(interval_list) in range(0, 1):
        return interval_list
    else:
        interval_list = sorted(interval_list, key = lambda interval: interval.left)
        merged_intervals = []
        merged_intervals.append(interval_list[0])
        for i in range(1, len(interval_list)):
            result = mergeIntervals(merged_intervals[-1], interval_list[i])
            if result == None:
                merged_intervals.append(interval_list[i])
            else:
                merged_intervals[-1] = result
        return merged_intervals

def transform_string_list_to_intervals(input_list):
    interval_list = []
    for i in range(0, len(input_list)):
        interval_list.append(interval(input_list[i]))
    return interval_list

def insert(interval_list, new_interval):
    interval_list.append(new_interval)
    return mergeOverlapping(interval_list)

def main():
    try:
        user_input = input("Please enter a list of intervals separated by ', ': ")
        if "quit" in user_input:
            sys.exit(0)
        print(user_input)
        user_input_list = user_input.split(', ')
        interval_list = transform_string_list_to_intervals(user_input_list)

        while True:
            try:
                user_input_int = input("Interval? ")
                if "quit" in user_input_int:
                    sys.exit(0)
                new_interval = interval(user_input_int)
                interval_list = insert(interval_list, new_interval)
                string_list = map(lambda interval: interval.string_represenation, interval_list)
                print("Current intervals: " + ", ".join(string_list))

            except InvalidIntervalException:
                print("Invalid interval, please try again")
                continue

    except InvalidIntervalException:
        print("Invalid interval(s). Please separate intervals by a comma followed by a space, as in '[1,2], [3,4]'")

if __name__ == '__main__':
        main()
