
############## Set In Python ################
# A set is a collection of unique items in Python. Sets don't allow duplicate items and don't maintain any particular order so it can't be indexed

#---------------------------------------

# Characteristics Of Sets
# Unordered
# Unique Elements
# Mutable: Can remove and add elemets
# Immutable Elements: Cannot replace elements. So just elements are immutable

#-----------------------------------------

# Create Set In Python
# 1) Using Curly Braces {}
set1 = {1, 2, 3, 4, 5}

# 2) Using set() Constructor
set2 = set([1, 2, 3, 4, 5])

# Note: An empty set cannot be created using {} as it creates an empty dictionary. For creating empty set use just set() constructor.
set3 = set() # Now it is an empty set

#------------------------------------------

# Set Operations
# 1) Adding Elements
set4 = {'apple', 'banana'}
set4.add('cherry')
print(set4) # {'cherry', 'banana', 'apple'}: Because set does not follow order

# 2) Removing Elements
# We can remove elements using two methods
# a) remove()
# b) discard()
set5 = {'apple', 'banana', 'cherry'}
# set5.remove('mango') # Will give an error because mango does not exit
set5.discard('mango') # Does not raise an error

#----------------------------------------

# Set Methods
# 1) Union: Combines elements from two or more than two sets, removing duplicates
set6 = {1, 2, 3}
set7 = {2, 3, 4}
set8 = {4, 5}
print(set6.union(set7, set8)) # {1, 2, 3, 4, 5}
# OR 
print(set6 | set7 | set8)

# 2) Intersection: It gives us those elements which are include in two or more than two sets.
set9 = {1, 2, 300, 400}
set10 = {1, 2, 3, 4}
print(set9.intersection(set10)) # {1, 2}
# OR
print(set9 & set10)

# 3) Difference: Elements present in the first set but not in the second
set11 = {1, 2, 3, 4}
set12 = {3, 4, 5, 6}
print(set11.difference(set12)) # {1, 2}
# OR 
print(set11 - set12)

# 4) Symmetric Difference: Elements in either set, but not in both
set13 = {1, 2, 3}
set14 = {3, 4, 5}
print(set13.symmetric_difference(set14)) # {1, 2, 4, 5}
# OR 
print(set13 ^ set14)

#---------------------------------------------

# Set Iteration
# You can use a for loop to go through each element in a set
set15 = {1, 2, 3, 4, 5}
for number in set15:
    print("Square of ", number, " is ", number ** 2)

# We cannot use while loop directly on set because set not support indexing so the solution is that first convert it into list then use while loop
set16 = {1, 2, 3, 4, 5}
list = list(set16)
index = 0
while index < len(list):
    print(list[index])
    index += 1

#---------------------------------------------

# Set Comprehensions
# It's similar to list comprehensions but for sets
# SYNTAX:
# set = {expression  for item in iterable   if condition} -> Here condition is optional
set18 = {1, 2, 3, 4, 5}
set17 = {num**2 for num in set18}
print(set17) # {1, 4, 9, 16, 25}