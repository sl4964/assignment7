class InvalidInterval(Exception):
    def __repr__(self):
        return "Invalid Interval!\n"

class MergeError(Exception):
    def __repr__(self):
        return "Intervals Cannot Be Merged!\n"