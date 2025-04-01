def calculate_average(*args):

    if not args:
        return 0

    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError("All arguments must be int or float.")

    return sum(args) / len(args)


print(calculate_average(10, 20, 30))  # Output: 20.0
