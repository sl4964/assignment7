"""
Utilities for the Interval class.
"""


def get_clean_string(s):
    """Removes whitespace from both front and back sides of the string."""
    if not isinstance(s, str):
        raise ValueError("\"%s\" is not a string." % s)
    return s.strip()


def check_brackets(s):
    """Checks whether the brackets on both the sides of interval string are valid.
    (,),[,] are considered as valid brackets.
    """
    if not (s.startswith("(") or s.startswith("[")):
        raise ValueError("Interval string \"%s\" does not start with a valid bracket." % s)
    if not (s.endswith(")") or s.endswith("]")):
        raise ValueError("Interval string \"%s\" does not end with a valid bracket." % s)


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def check_interval_limits(s):
    """Checks whether the strings representing the limits of the interval are valid. Also checks if
    the left_limit <= right_limit after accounting for the open and closed brackets, parentheses.
    """
    if len(s) < 3:
        raise ValueError("There are no limits specified in the interval string \"%s\"." % s)
    bounds = s[1:-1].split(",")
    if len(bounds) != 2:
        raise ValueError("The limits of the interval \"%s\" are not correct." % s)
    if not is_integer(bounds[0]):
        raise ValueError("The starting bound \"%s\" is not a valid integer." % bounds[0])
    if not is_integer(bounds[1]):
        raise ValueError("The ending bound \"%s\" is not a valid integer." % bounds[1])
    opening_limit = int(bounds[0])
    closing_limit = int(bounds[1])
    if s[0] == "(":
        opening_limit += 1
    if s[-1] == ")":
        closing_limit -= 1
    if opening_limit > closing_limit:
        raise ValueError("For the interval \"%s\" the opening limit is greater than the closing limit." % s)


