
# STRING FORMATING AND STRING OPERATORS:


print('''It's me M Saqib Khan''') # If you want to use single quote inside single quote or double quote inside double quote you can use three times quotes for this case.


# 1) Old Style Formating (% Operator):
my_name = "M Saqib Khan"
my_age = 18
print("My name is %s and I'm %d" % (my_name, my_age))
# %s and %d are placeholders, %s represents string while %d represents digit(numeric value).



# 2) str.format() method
name1 = "Ali"
age1 = 20
print("My name is {} and I'm {}". format(name1, age1))

# We can also reference variables by index or keywords
print("My name is {0} and I'm {1}".format(name1, age1))
print("My name is {name1} and I'm {age1}".format(name1 = 'Saqib', age1 = 19))



# 3) f-string (Very usable and simple string formating technique):
name2 = "Ahmad"
age2 = 22
print(f"My name is {name2} and I'm {age2}")







#   STRING OPERATORS:
a = 'one'
b = 'two'

print(a + b) # Strings will concate

print(a * 4) # * 4 will create 4 coppies

print(r"Hello /n World") # r/R (Raw String): It will print the exact string. It will suppresses the escape characters.


# [] slice 
# [:] rande slice
# % string formating
# in: membership operator
# not in:  membership operator