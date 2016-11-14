#User defined exception(s) are employed for indicating error conditions
class InvalidException(Exception):
    def __str__(self):
        #the interval is not valid
        return 'Invalid interval'

class MergeException(Exception):
    def __str__(self):
        #the intervals could not be merged
        return "these two intervals cannot be merged"


