import numpy as np


# To calculate the sum of list of numbers
def sum_nums(input_list):

    try:
        ans = np.sum(input_list)
    except IOError:
        print("I/O Error. May be out of space.")
    except TypeError:
        print("Type Error. Input of wrong type.")
    except ValueError:
        print("Value Error. Not valid input.")

    return ans


# returns a tuple of the min and max values in a list
def min_max(input_list):

    min_max_val = (min(input_list), max(input_list))

    return min_max_val


# To calculate the maximum difference between two adjacent numbers
def max_diff(input_list):

    diff = np.diff(input_list)
    abs_diff = np.abs(diff)
    max_val = np.max(abs_diff)

    return max_val
