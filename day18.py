
#########   NESTED LOOPES IN PYTHON #########

for i in range(3):
    for j in range(1, 4):
        print(j)
    print("Outer loop ended")



#--------------------------------------------



k = 0
while k < 3:
    l = 1
    while l <= 3:
        print(l)
        l += 1
    k += 1
    print("Outer while loop ended")

#-------------------------------------------------



m = 0
while m < 3:
    for n in range(1, 4):
        print(n)
    m += 1
    print("Outer while loop ended")