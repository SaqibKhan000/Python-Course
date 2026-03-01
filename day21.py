
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
tuple5 = ("red", "green", "blue", "orange", "purple")
print(tuple5[1:2]) # ('green',)
print(tuple5[0::2]) # ('red', 'blue', 'puple')
print(tuple5[::-1]) # ('puple', 'orange', 'blue', 'green', 'red')


# Tuple Operations
# 1) Concatenation:
tuple6 = ('purple', 'orange', 'blue')
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
tuple10 = ('purple', 'orange', 'blue')
for item in tuple10:
    print(item)

# By while loop
index = 0
while index < len(tuple10):
    print(tuple10[index])
    index += 1



#----------------------------------------




# Tuple Methods:
# Tuple has very less methods because it's immutable

# 1) count()
tuple11 = ('purple', 'orange', 'blue')
print(tuple11.count('purple')) # 1


# 2) index
tuple12 = ('purple', 'orange', 'blue')
print(tuple12.index('blue')) # 2






#----------------------------------------------






# Tuple Functions

# 1) len()
tuple13 = ('purple', 'orange', 'blue')
print(len(tuple13)) # 3


# 2) sum()
tuple14 = (1, 2, 3, 4)
print(sum(tuple14)) # 4


# 3) min()
print(min(tuple14)) # 1
 

# 4) max()
print(max(tuple14)) # 4


# 5) sorted()
print(sorted(tuple14)) # It will give us list not tuple
# Solution is:
list = sorted(tuple14)
print(tuple(list)) # (1, 2, 3, 4)






#-----------------------------------------------





# Packing And Unpacking Tuples:

# PACKING: It is the process of putting multiple values into a sinple tuple.
# UNPACKING: It is extracting the values from a tuple into separate variables.

a = "Saqib"
b = 18
c = "Content Creator"
tuple15 = a, b, c
print(tuple15) # Packing Tuple: ('Saqib', 18, 'Content Creator')


name, age, profession = tuple15 # Unpacking Tuple
print("Name is ", name)
print("Age is ", age)
print("Profession is ", profession)





#--------------------------------------------------





# Tuple is Immutable but we can modify it indirectly:
tuple16 = (10, 20, 30)
tuple16[0] = "ten" 
print(tuple16) # Will Cause Error❌

# Solution Is:
list2 = list(tuple16)
list2[0] = "ten"
tuple17 = tuple(list2)
print(tuple17)







