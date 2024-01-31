# A calculator program.

from art import logo 

def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operations = { 
              "+": sum,
              "-": subtract,
              "*": multiply,
              "/": divide 
              } 


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    Should_Continue = True

    while Should_Continue:
        operation_symbol = input("pick a operation: ")
        next_number = float(input("What's the next number?: "))

        calculation = operations[operation_symbol]
        answer = calculation(num1,next_number)
        print(f"{num1} { operation_symbol }  {next_number} = {answer}")
        
        if input(f"Type 'y' to continue calculating with the result {answer}, or type 'n' to start a new calculation.: ") == 'y':
            num1 = answer
        else:
            Should_Continue = False
            calculator()
        
calculator()
        


