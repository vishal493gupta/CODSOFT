# A python project that will create a random password.

import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[',']',']','\\','|','`','~',',','<','.','>','?','/']

numbers = ['1','2','3','4','5','6','7','8','9','0']

print("Welcome to the PyPassword Generator")

let = int(input("How many letters would you like in your password?: "))
sym = int(input("How many symbols would you like?: "))
num = int(input("How many numbers would you like?: "))

    
password = ""
    
for i in range(let):
    password += random.choice(letters)   
    
for j in range(sym):
    password += random.choice(symbols)
   
for k in range(num):
    password += random.choice(numbers)    
        
print("Here is your password: ", password)