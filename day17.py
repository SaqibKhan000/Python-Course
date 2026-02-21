
######## LOOPS IN PYTHON ########

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("While loop ended")
##################################
count2 = 4
while count2 >= 0:
    print(count2)
    count2 -= 1
else:
    print("While loop ended")




# For Loop
lang = "Python"
for character in lang:
    print(character)
else:
    print("For loop ended")

# range():
#        This function is specially for 'for' loop. range(start, stop, step)
# start mean start index.
# stop mean end index, mean where the loop will exit and this index is exclusive.
# step defines the step of the iterations. Step is by default (1).
for i in range(1, 5):
    print(i)  # 1  2  3  4


for j in range(5):
    print(j) # 1  2  3  4 
# When we give just one value to range() function, that value only for stop


for k in range(1, 10, 2):
    print(k) # 1  3  5  7  9 . Because of step 2.
else:
    print("For loop ended")





# Loop Control Statements:

# Pass Statement:
number = 1
while number <= 5:
    if(number == 3):
       pass
    print(number)
    number += 1
# Pass Statmement doesn't any work, but it is used to prevent ourselves from syntax error. For example as you see in the above example I write a condition and inside I write the pass statement so if I don't write this I will take a syntax error. So if you want to leave a particular area for a future code but directly leaving the area will cause syntax error that's pass statement is use for this problem.


# Break Statement:
for num1 in range(1, 5):
    if(num1 == 4):
        print("Loop ended")
        break
    print(num1)




# Continue Statement:
num2 = 1
while num2 < 10:
    if(num2 == 5):
        num2 += 1
        continue
    print(num2)
    num2 += 1








# For practice purpose:
while True:
    user_input = input("Enter exit to stop the loop:")
    if(user_input == "exit"):
        print("Congrates! loop was exited.")
        break
    else:
        print(F"{user_input} is not a proper command")
   