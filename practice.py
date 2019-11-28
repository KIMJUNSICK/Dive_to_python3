# def function's name(arg1, arg2...):
# python args of function are not specified for data type
# docstring is not just an annotation. ftn attribute called when runtime


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    """ Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string
    """


# case1: args are read by location
approximate_size(10000)  # defalt
approximate_size(10000, False)

# case2: args are read by name
approximate_size(a_kilobyte_is_1024_bytes=False, size=2000)
approximate_size(size=2000, a_kilobyte_is_1024_bytes=False)

