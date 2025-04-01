class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError(f"{number} is negative!")
    print(f"{number} is positive.")

try:
    test_number = -10
    check_positive(test_number)
except NegativeNumberError as e:
    print("Caught an exception:", e)