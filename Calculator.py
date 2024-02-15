# A calculator program.
        
from calc_art import logo

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None

operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    try:
        num1 = float(input("What's the first number?: "))
    except ValueError:
        print("Error: Please provide a valid input.")
        return

    for symbol in operations:
        print(symbol)

    Should_Continue = True

    while Should_Continue:
        operation_symbol = input("pick a operation: ")
        if operation_symbol not in operations:
            print("Error: Invalid operation!")
            return
        try:
            next_number = float(input("What's the next number?: "))
        except ValueError:
            print("Error: Please provide a valid input.")
            return

        calculation = operations[operation_symbol]
        answer = calculation(num1, next_number)
        
        if answer is not None:
            print(f"{num1} {operation_symbol} {next_number} = {answer}")
            num1 = answer

            
        if input(f"Type 'y' to continue calculating with the result {answer}, or type 'n' or press any other key to start a new calculation.: ") != 'y':
            Should_Continue = False
            calculator()

calculator()



