import sys
from Interval import *


def main():

    try:
        # Receive user input and split on comma.
        components = input('Comma-separated list of intervals: ').split(',')

    except EOFError:
        print("End-of-file error. Exiting...")
        sys.exit(1)

    except (KeyboardInterrupt, SystemExit):
        print('Exiting...')
        sys.exit(1)

    # Assert that our list is of even length. Assuming each interval is
    # properly formatted (values split by a comma) and each interval is
    # separated by a comma, each interval requires 2 commas.
    validate_even_list(components)

    # Now that we have valid input, build our list of Interval objects.
    intervals = create_intervals(components)

    # Switch to read-eval-respond loop.
    interactive_input(intervals)


def validate_even_list(components: List[str]):
    """Validate our user-input list of Intervals has even length.

    This is necessary because after splitting a valid input of Intervals -- assuming
    comma-delimited format -- we should have an even-length list. This is because
    each interval requires two commas: one for their range delimiting, and
    another for individual Interval delimiting. In the case of a single Interval,
    we still have two Interval components.

    :param components: comma-separated user-input list of Interval objects
    :return: raises UserInputException if list is not even, else continues program
    """

    # One-off boolean for determining length evenness.
    even_length = len(components) % 2 == 0

    # If our components list is not of even length,
    # our input is invalid and we raise an exception.
    if not even_length:
        print(UserInputException(components))


def create_intervals(components: List[str], separated=True) -> List[Interval]:
    """Given valid components list, create Intervals from pairwise components.

    :param components: comma-separated user-input list of Interval objects
    :param separated: boolean denoting whether our components are split
                      or self-contained. Allows for re-use of method when
                      testing numerous intervals
    :return intervals: list of Interval objects made from components
    """

    if separated:

        # Zip the even and odd elements of our components list, ensuring
        # each item is a potential Interval object.
        zipped_components = zip(components[::2], components[1::2])

        # Join each pair by a comma. :joined should now contain eligible intervals.
        components = [', '.join(pair) for pair in zipped_components]

    # Initialize container for valid intervals.
    intervals = []

    for candidate in components:
        try:
            # Attempt to create an Interval object using our string representation.
            # If we succeed, append that interval to our container.
            interval = Interval(candidate)
            intervals.append(interval)

        # If we do not succeed: locate the exception, print this information to
        # the user, and continue.
        except ParsingException as p:
            print(str(p), file=sys.stderr)

        except RangeMismatchException as rm:
            print(str(rm), file=sys.stderr)

        except RangeException as r:
            print(str(r), file=sys.stderr)

        except EOFError:
            print("End-of-file error. Exiting...")
            break

        except (KeyboardInterrupt, SystemExit):
            break

    # Return elements from components that were successfully made into
    # Interval objects.
    return intervals


def interactive_input(intervals: List[Interval]):
    """Read-eval-response loop for interactive insertion into :intervals.

    :param intervals: list of Interval objects to be inserted into
    :return: never-ending; if user enters a common 'quit' symbol they will exit
    """

    # While our user has not asked to exit, keep receiving input.
    response = input('Interval: ').lower()

    while response not in ['q', 'quit', 'exit']:

        try:
            # Attempt to coerce this new input as an Interval object.
            # If we succeed, insert into the current list of Intervals
            # and print the new, sorted, merged list of Intervals including
            # the original input. Print the new intervals list, as well.
            interval = Interval(response)
            intervals = insert_into(intervals, interval)
            print(', '.join([str(interval) for interval in intervals]))

        # If we cannot create an Interval object or insert the response
        # into :interval, locate the exception, tell the user what happened,
        # and continue.
        except ParsingException as p:
            print(str(p), file=sys.stderr)

        except RangeMismatchException as rm:
            print(str(rm), file=sys.stderr)

        except RangeException as r:
            print(str(r), file=sys.stderr)

        except EOFError:
            print("End-of-file error. Exiting...")
            break

        except (KeyboardInterrupt, SystemExit):
            print("Exiting...")
            break

        # Once we've reasonably handled exceptions, prompt the user
        # for their next requested interval of insertion.
        response = input('Interval: ')


if __name__ == '__main__':
    main()
