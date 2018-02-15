

def max_diff(input_list):
    """Returns the maximum absolute difference between two adjacent numbers

    :param input_list: a list of numbers
    :returns max_val: maximum absolute difference between two adjacent numbers
    :raises ImportError: if required modules are not found
    :raises TypeError: if input_list contains anything other than numbers
    :raises ValueError: if input_list contains less than two values
                        or max_val is NaN
    """

    try:

        import numpy as np
        import logging as lg

        lg.basicConfig(filename='max_diff.log',
                       level=lg.DEBUG,
                       format='%(asctime)s %(message)s',
                       datefmt='%m/%d/%Y %I:%M:%S %p')

        diff = np.diff(input_list)
        abs_diff = np.abs(diff)
        max_val = np.max(abs_diff)
        if(np.isnan(max_val)):
            raise ValueError

        lg.info(' | SUCCESS: input_list %s returned %g'
                    % (input_list, max_val))
        return max_val

    except ImportError as e:
        print('ImportError: %s module not found.' % e.name)
        lg.debug(' | ABORTED: ImportError: %s' % e.name)
        raise ImportError
    except TypeError:
        print('TypeError: input_list must be a list of integers/floats.')
        lg.debug(' | ABORTED: TypeError: input_list is %s (%s)'
                 % (input_list, type(input_list)))
        raise TypeError
    except ValueError:
        print('ValueError: max_val is NaN')
        lg.debug(' | ABORTED: ValueError: max_val is NaN')
        raise ValueError
    except:
        print('An unknown error occurred.')
        lg.warning(' | WARNING: OMG AN UNKNOWN ERROR OCCURRED!')
        raise


def max_diff(input_list):
    """Returns the maximum absolute difference between two adjacent numbers

    :param input_list: a list of numbers
    :returns max_val: maximum absolute difference between two adjacent numbers
    :raises ImportError: if required modules are not found
    :raises TypeError: if input_list contains anything other than numbers
    :raises ValueError: if input_list contains less than two values
                        or max_val is NaN
    """

    try:

        import numpy as np
        import logging as lg

        lg.basicConfig(filename='max_diff.log',
                       level=lg.DEBUG,
                       format='%(asctime)s %(message)s',
                       datefmt='%m/%d/%Y %I:%M:%S %p')

        diff = np.diff(input_list)
        abs_diff = np.abs(diff)
        max_val = np.max(abs_diff)
        if(np.isnan(max_val)):
            raise ValueError

        lg.info(' | SUCCESS: input_list %s returned %g'
                % (input_list, max_val))
        return max_val

    except ImportError as e:
        print('ImportError: %s module not found.' % e.name)
        lg.debug(' | ABORTED: ImportError: %s' % e.name)
        raise ImportError
    except TypeError:
        print('TypeError: input_list must be a list of integers/floats.')
        lg.debug(' | ABORTED: TypeError: input_list is %s (%s)'
                 % (input_list, type(input_list)))
        raise TypeError
    except ValueError:
        print('ValueError: max_val is NaN')
        lg.debug(' | ABORTED: ValueError: max_val is NaN')
        raise ValueError
    except:
        print('An unknown error occurred.')
        lg.warning(' | WARNING: OMG AN UNKNOWN ERROR OCCURRED!')
        raise


# To calculate the sum of list of numbers
def sum_nums(input_list):
    """Returns sum of numbers in an input list

    :param input_list: list of input numbers
    :returns ans: sum of numbers in input list
    :raises ImportError: required module is not found
    :raises TypeError: input is not list of float/ints
    :raises ValueError: input is not valid number

    """

    try:

        import numpy as np
        import logging as lg

        lg.basicConfig(filename='sum_nums.log',
                       level=lg.DEBUG,
                       format='%(asctime)s %(message)s',
                       datefmt='%m/%d/%Y %I:%M:%S %p')

    return min_max_val
