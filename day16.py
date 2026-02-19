
######## ASSIGNMENT: 4 ########

#1. Limit the decimal places to 2 digits using .format method and print result, for the variable pi = 3.14159265359 
pi = 3.14159265359 
print("Value of PI is {:.2f} ".format(pi))



#2. Extract characters from index 2 to 8 with a step of 2: Given my_string = "Python Course", slice characters from index 2 to 8, skipping every other char.
my_string = "Python Course"
print(my_string[2:8:2])



#3.  Slice to get only the middle character(q): For name = "Saqib", use slicing to extract the middle character(q).
name = 'Saqib'
def mid_char(word):
 middle = int(len(word)/2)
 if(len(word) % 2 == 0):
  return word[middle - 1 : middle + 1]
 else:
  return word[middle]
print(mid_char(name))



#4. Remove the first 3 and last 3 characters: Given my_string = "Regression Analysis", remove the first 3 and last 3 characters.
my_string = "Regression Analysis"
print(my_string[3:-3])



#5. How to Reverse a String Using Python String Methods? 
word = "Python"
print(word[::-1])




#6. Write a Python function to check if a string is a palindrome using string methods.
word = "madam"
word2 = "madan"
def is_palindrom(lafaz):
 if(lafaz == lafaz[::-1]):
  print(f"{lafaz} is a Palindrome")
 else:
  print(f"{lafaz} is not a Palindrome")
is_palindrom(word) # Palindrome ✅
is_palindrom(word2) # Palindrome ❌



