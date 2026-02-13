
# Project-01:  SIMPLE CALCULATOR:

def add(num1, num2): 
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def divs(num1, num2):
    return num1 / num2

def avg(num1, num2):
    return (num1 + num2) / 2


print('Select an operator:\n ' \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n"
      )
select = int(input("Select an operation from 1 to 5: ")) 

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

if select == 1:
   print(f'{number1} + {number2} = {add(number1, number2)}')
elif select == 2:
     print(f'{number1} - {number2} = {sub(number1, number2)}')
elif select == 3:
     print(f'{number1} x {number2} = {mult(number1, number2)}')
elif select == 4:
     print(f'{number1} / {number2} = {divs(number1, number2)}')
elif select == 5:
     print(f'{number1} + {number2} / 2 = {avg(number1, number2)}')