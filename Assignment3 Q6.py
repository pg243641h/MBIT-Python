def divide_numbers(numerator, denominator):

    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Invalid input types. Please provide numeric values.")
        return None
    else:
        return result


print(divide_numbers(10, 2))