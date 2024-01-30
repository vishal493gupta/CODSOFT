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

operation_symbol = input("pick a operation from the line above: ")
num2 = int(input("What's the second number?: "))

calculation = operations[operation_symbol]
print(f"{num1} { operation_symbol }  {num2} = {calculation(num1,num2)}")


