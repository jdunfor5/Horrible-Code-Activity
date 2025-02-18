# Adds the numbers collected from the user
def add(num1, num2):
    return num1 + num2

# Subtracts the numbers collected from the user
def subtract(num1, num2):
    return num1 - num2

# Multiplies the numbers collected from the user
def multiply(num1, num2):
    return num1 * num2

# Divides the numbers collected from the user
def divide(num1, num2):
    return num1 / num2

# Checks that user input is a valid number
def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main Loop
while True:
    # Collecting user input
    num1 = get_valid_number("Enter the first number: ")
    num2 = get_valid_number("Enter the second number: ")

    # Ask the user for an operation
    while True:
        operation = input("Enter the operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid input. Please enter a valid operation (+, -, *, /).")

    result = None

    match operation:
        case "+":
            result = add(num1, num2)

        case "-":
            result = subtract(num1, num2)

        case "*":
            result = multiply(num1, num2)

        case "/":
            if num2 != 0:
                result = divide(num1, num2)
            else:
                print("Error: Division by 0 not allowed.")
                continue  # Restart from collecting numbers

    print(f"{num1} {operation} {num2} = {result}")

    # Ask user if they want to continue
    user_input = input("Would you like to continue? (y/n): ").strip().lower()
    if user_input != 'y':  # If not 'y', exit the loop
        print("Exiting calculator. Goodbye!")
        break
