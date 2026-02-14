
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