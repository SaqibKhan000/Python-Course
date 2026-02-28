
############# Tuple In Python ##############

# Tuple is a collection of items in Python that is ordered, unchangeable (immutable) and allow dulicate values.


# Create Tuple In Python:

# 1) Using Parentheses()
tuple1 = ("red", "green", "blue")


# 2) Without Parentheses
tuple2 = 1, 2, 3, 4, 5


# 3) Using the tuple() Constructor
list = [1, 2, 3, 4, 5]
print(tuple(list)) # (1, 2, 3, 4, 5)


# 4) Single-Item Tuple
tuple3 = ("Only",) # If we not use comma after Only it will be considered as a string.



#------------------------------------------------



# Accessing Tuple Elements - Indexing
tuple4 = ("red", "green", "blue")
print(tuple4[-1]) # blue                    


# Tuple Slicing
tuple5 = ("red", "green", "blue", "orange", "puple")
print(tuple5[1:2]) # ('green',)
print(tuple5[0::2]) # ('red', 'blue', 'puple')
print(tuple5[::-1]) # ('puple', 'orange', 'blue', 'green', 'red')


# Tuple Operations
# 1) Concatenation:
tuple6 = ('puple', 'orange', 'blue')
tuple7 = ('green', 'red')
print(tuple6 + tuple7)

# 2) Repetition:
tuple8 = ("Saqib",) * 3
print(tuple8) # ('Saqib', 'Saqib', 'Saqib')

# 3) Checking for an Item
tuple9 = (1, 2, 3, 4, 5)
print(5 in tuple9) # True
print(4 not in tuple9) # False


# Iteration Over Tuple:
tuple10 = ('puple', 'orange', 'blue')
for item in tuple10:
    print(item)

# By while loop
index = 0
while index < len(tuple10):
    print(tuple10[index])
    index += 1