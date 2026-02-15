
# TYPES OF ARGUMENTS IN FUNCTION:
# There Are Four(4) Types Of Arguments In Function:

# 1) Required Arguments (single / multiple arguments):
def users(user1, user2):
    print('Hello! ', user1, user2)
users("Ali ", "Usman")



# 2) Default Argument:
def defaultArg(user3 = 'Naseem'):
    print(user3)
defaultArg()



# 3) Keyword Argument OR Named Argument:
# This type arguments does not follow the parameter sequence.
def addNums(num1, num2):
    print(num1 / num2)
addNums(num2=12, num1=6) # These are Keyword arguments or Named arguments



# 4) Arbitrary Arguments OR Variable Length Arugments
# It has two parts:

# i) Arbitrary Positional Arguments (*args): Es mai jtnai b argumets hongai wo as a tuple store hongai.
def add_Numbers(*args):
    return sum(args)
print(add_Numbers(1, 2, 3, 4)) # Here I can add multiple number these numbers will be collect in *args and will b store as a tuple.
# Is mai sequence ko follow krna zrorii hai


# ii) Arbitrary Keyword Arguments (**kwargs): Es mai jtnai b argumets hongai wo as a dictionary store hongai.
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name = "M Saqib Khan", city = "Peshawar") # In **kwargs we pass the keyword arguments and that arguments store in **kwargs as a dictionary and we can pass a lot of arguments.
# Is mai sequence follow nhi hota for arguments