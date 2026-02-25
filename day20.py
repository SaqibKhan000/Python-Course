
########## LIST IN PYTHON ##########

list1 = [1, 2, 'a', 'b', True]
print(list1)

#------------------------------


list2 = [[1, 2], [3, 4]]
print(list2)



#-------------------------

list3 = [1, 2, 3, 4, 5]
print(list3[-1]) # 5


#-------------------------



# List Slicing
list4 = ['Apple', 'Banana', 'Cherry', 'Dragon-fruit', 'Mango']
print(list4[2:4]) # ['Cherry', 'Dragon fruit']
print(list4[0::2]) # By Step-2 -> ['Apple', 'Cherry', 'Mango']
print(list4[::-1]) # Reverse list -> ['Mango', 'Dragon-fruit', 'Cherry', 'Banana', 'Apple']
print(list4[-2:]) # ['Dragon-fruit', 'Mango']



#----------------------------------



# List Modying
list5 = ['Apple', 'Banana', 'Cherry', 'Dragon-fruit', 'Mango']
list5[0] = 'Watermelon'  # replacing element
list5.append('Guava') # adding element at the end of the list
list5.remove('Banana') # deleting element 
print(list5)



#------------------------------------




# List Methods
# 1) append()
list6 = ['Apple', 'Banana', 'Cherry']
list6.append(2917) # ['Apple', 'Banana', 'Cherry', 2917]
print(list6)


# 2) extend()