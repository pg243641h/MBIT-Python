def classify_number():
    while True:
        user_input = input("Enter an integer (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Exiting...")
            return None

        try:
            number = int(user_input)
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"



result = classify_number()
if result is not None:
    print(f"The number is: {result}")