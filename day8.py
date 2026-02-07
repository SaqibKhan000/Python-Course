# We Have Total Seven (7) Operators In Python:


# 1) ARITHMATIC OPERATOR:
num1 = 10
num2 = 5
print(num1 + num2) # Addition Operator
print(num1 - num2) # Subtraction Operator
print(num1 * num2) # Multiplication Operator
print(num1 / num2) # Division Operator
print(num1 // num2) # Floor Division Operator
print(num1 % num2) # Modulus Operator
print(num1 ** num2) # Exponentiation Operator




# 2) ASSIGNMENT OPERATOR:
num3 = 8 # Assignment Operator (=)
num3 += 1 # Assignment Operator (+=) 
num3 -= 1 # Assignment Operator (-=) 
num3 *= 1 # Assignment Operator (*=) 
num3 /= 1 # Assignment Operator (/=) 
num3 %= 1 # Assignment Operator (%=) 
num3 //= 1 # Assignment Operator (//=) 





# 3) COMPARISON OR RELATIONAL OPERATOR:
num4 = 8
num5 = 5
print(num4 == num5) # equal to 
print(num4 != num5) # not equal to
print(num4 > num5) # greater than
print(num4 < num5) # less than
print(num4 >= num5) # greater than or equal to
print(num4 <= num5) # less than or equal to







# 4) LOGICAL OPERATOR:
num6 = 15
num7 = 10
print((num6 > num7) and (num7 < num6)) # and operator
print((num6 > num7) or (num7 > num6))  # or operator
print(not(num6 > num7)) # not operator








# 5) IDENTITY OPERATOR (is, is not):
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(list1 is list2) # Here 'is' operator checking the memory location of list1 and list2 which is same then it will return true
print(list1 is list3) # Values are same but memory locations are diff so here it will return false
print(list1 is not list3) # 'is not' operator is the inverse of 'is' operator so here it will return true








# 6) MEMBERSHIP OPERATOR (in, not in):
list4 = ['a', 'b', 'c', 'd', 'e']
print('b' in list4) # here 'n' operator checks the element inside the list4 if it's then it will return true
print('x' in list4) # False
print('x' not in list4) # True  -> 'not in' operator is the inverse of 'in' operator










# 7) BITWISE OPERATOR (AND-(&), OR-(|), XOR-(^), NOT-(~):
num8 = 5 # 5 in binary numbers -> 0101
num9 = 3 # 3 in binary numbers -> 0011
print(num8 & num9) # 1

# REASON: In betwise '&' operator compares the binary numbers of a value like:
# 0101  & 0011
# 0 & 0 = 0   OR   False & False = False
# 1 & 0 = 0   OR   True & False = False
# 0 & 1 = 0   OR   False & True = False
# 1 & 1 = 1   OR   True & True = True
# So the result will be 1 

print(num8 | num9) # 7
# 0 | 0 = 0
# 1 | 0 = 1
# 0 | 1 = 1
# 1 | 1 = 1
# So it's 111. And in decimal 111 = 7

