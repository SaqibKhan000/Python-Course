
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
#        This method is specially for 'for' loop. range(start, stop, step)
# start mean start index.
# stop mean end index, mean where the loop will exit and this index is exclusive.
# step defines the step of the iterations. Step is by default (1).
for i in range(1, 5):
    print(i)  # 1  2  3  4


for j in range(5):
    print(j) # 1  2  3  4 
# When we give just one value to range() method, that value only for stop


for k in range(1, 10, 2):
    print(k) # 1  3  5  7  9 . Because of step 2.