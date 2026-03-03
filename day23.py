
############### Dictionary In Python ###################
# A dictionary is a data structure in Python that stores data in key-value pairs. Dictionary items (key-value pair) are ordered, changeable, and do not allow duplicates.

# Creating Dictionary
# Method-1:
dict1 = {
    "name": "M Saqib Khan",
    "address": "Peshawar"
}

# Method-2: Using dict() constructor
dict2 = dict(name="M Saqib Khan", age=18)

# Method-3: Using a List of Tuples
dict3 = dict([("name", "M Saqib Khan"), ("age", 18)])
print(dict3) # {'name': 'M Saqib Khan', 'age': 18}

#-----------------------------------------------

# Access Dictionary Values
print(dict3["name"])
print(dict3["age"])

#------------------------------------------------

# Dictionary Methods
dict4 = {
     "name": "M Saqib Khan",
     "address": "Peshawar",
     "age": 18
}
print(dict4.keys()) # dict_keys(['name', 'address', 'age'])
print(dict4.values()) # dict_values(['M Saqib Khan', 'Peshawar', 18])
print(dict4.items()) # All key value pairs
print(dict4.get("name")) # M Saqib Khan: We can also do this by using dict4["name"], but there is difference b/w them if a property not present in dictionary and I use [] like dict4["email"] then it will give error but by using get method it didn't give error(dict4.get("email")) just give None but if we wite something with it like dict4.get("email", "Nothing") so now the output will be 'Nothin'

#------------------------------------------------

# Add and Remove Items In Dictionary
dict5 = {
     "name": "M Saqib Khan",
     "address": "Peshawar",
}
dict5["age"] = 18 # Adding
print(dict5)

del dict5["address"] # Deleting item using 'del'
print(dict5)

user_age = dict5.pop("age") # Deleting item using pop but it also return the deleted value 
print(dict5)

#------------------------------------------------------

# Dictionary Iterations
