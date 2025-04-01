while True:
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"You entered: {number}")
