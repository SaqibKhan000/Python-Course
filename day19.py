
########### ASSIGNMENT: 5 ############

# 1) Use while loop to print the output in the same line
# i = 0
# while(i < 5):
#     print(i, end=" ")
#     i += 1




#2) a: Triangle Pattern 
# for j in range(1, 11):
#     print("*" * j)


# b: Inverted Triangle Pattern 
# i = 10
# while i >= 1:
#     print("*" * i)
#     i -= 1






# 3) Find factorial of any number
# def factorial(number):
#          result = 1
#          while number > 0:
#                  result *= number
#                  number -= 1
#          return result
# print(factorial(5))





# 4) Count the number of vowels in a string
# vowels = "aeiou"
# def vowelsCount(word):
#     count = 0
#     for character in word:
#         if character.lower() in vowels:
#             count += 1
#     return count

# print(vowelsCount("M Saqib Khan"))






# 5) Longest word in a string
# sentence = 'I am M Saqib Khan'
# longest_word = ""
# words_list = sentence.split()
# for word in words_list:
#     if len(word) > len(longest_word):
#         longest_word = word
# print(longest_word)






# 6) do-while loop in python 
# while True:
#     num = int(input("Enter a number which is greater than ten(10): "))
#     if num > 10:
#         print("You entered correct number ", {num})
#         break
#     else:
#         print(f"{num} is not greater than ten(10). Try again")