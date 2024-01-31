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

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

Should_Continue = True

while Should_Continue:
    operation_symbol = input("pick a operation: ")
    next_number = int(input("What's the next number?: "))

    calculation = operations[operation_symbol]
    answer = calculation(num1,next_number)
    print(f"{num1} { operation_symbol }  {next_number} = {answer}")
    
    if input(f"Type 'y' to continue calculating with the result {answer}, or type 'n' to exit.: ") == 'y':
        num1 = answer
    else:
        Should_Continue = False
        

