

# IF STATEMENT IN PYTHON:
age = int(input("Enter your age: "))
if age >= 18:
    print("You can drive")






# IF-ELSE STATEMENT IN PYTHON:
temp = 28
if temp <= 18:
    print("It's a cool day.")
else:
    print("It's a hot day.")    






# IF ELIF ELSE STATEMENT IN PYTHON:   
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")







# NESTED IF-ELSE STATEMENT:
number = int(input("Enter any number: "))
if number > 0:
    if(number % 2 == 0):
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    if(number == 0):
        print("Number is Zero")
    else:
        print("Number is negative")







# CONDITIONAL EXPRESSIONS OR TERNARY OPERATOR:
value = 11
result = 'Even Number' if(value % 2 == 0) else 'Odd Number'
print(result)