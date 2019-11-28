# def function's name(arg1, arg2...):
# python args of function are not specified for data type


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    pass


# case1: args are read by location
approximate_size(10000)  # defalt
approximate_size(10000, False)

# case2: args are read by name
approximate_size(a_kilobyte_is_1024_bytes=False, size=2000)
approximate_size(size=2000, a_kilobyte_is_1024_bytes=False)

