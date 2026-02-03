


################ TYPE-CASTING ###############
# ->  Conversion of one type to another is called type casting.


# From number to string conversion
num1 = 10
print(str(num1))          # '10'
print(type(str(num1)))   # <class 'str'>



# From string to number conversion
num2 = "20"
print(int(num2))          # 20
print(type(int(num2)))   # <class 'int'>


# From number to float conversion
num3 = 30
print(float(num3))          # 30.0
print(type(float(num3)))   # <class 'float'>


# From integer to complex conversion
num3 = 40
print(complex(num3))          # (40+0j)
print(type(complex(num3)))   # <class 'complex'>


# From float to interger
num4 = 13.5
print(int(num4))
print(type(int(num4)))   # <class 'int'>


# From integer to boolean
num5 = 0
print(bool(num5))          # False
print(type(bool(num5)))   # <class 'bool'>

num6 = 1
print(bool(num6))          # True
print(type(bool(num6)))   # <class 'bool'>  


# From string to boolean
str1 = ""       
print(bool(str1))          # False
print(type(bool(str1)))   # <class 'bool'>

str2 = "Hello"       
print(bool(str2))          # True   
print(type(bool(str2)))   # <class 'bool'>




# Implicit Type Casting OR Coercion
# ->  In implicit type casting, Python automatically converts one data type to another without any user involvement.
num7 = 5        # int
num8 = 2.5      # float
result = num7 + num8   # int + float = float
print(result)            # 7.5
print(type(result))     # <class 'float'>






# Explicit Type Casting OR Type Conversion
# ->  In explicit type casting, the user manually converts one data type to another using built-in functions.
num9 = "100"    # string
num10 = int(num9)   # string to int
print(num10)          # 100
print(type(num10))   # <class 'int'>