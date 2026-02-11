

## Task 1:
# Find leap year:
year = int(input("Enter year: e.g. 2026: "))
if (year % 4 == 0 and year % 100 != 0) or \
      year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")






## Task 2:
# User Login process:
email = 'saqib@gmail.com'
password = '123123'
inpEmail = input("Enter email: ")
inpPass = input("Enter pass: ")
if inpEmail == email:
    if(inpPass == password):
        print("Welcome back")
    else:
        print("Invalid Password")
else: 
    print("Invalid email")