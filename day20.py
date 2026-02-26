
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


# 2) remove()
list7 = ['Apple', 'Banana', 'Cherry', 'Banana']
list7.remove('Banana') # deleting element from first occurance
print(list7)


# 3) extend()
list8 = [1, 2, 3]
list9 = [4, 5, 6]
list8.extend(list9)
print(list8) # [1, 2, 3, 4, 5, 6]


# 4) insert()
list10 = ['a', 'b', 'c']
list10.insert(2, 'd')
print(list10) # ['a', 'b', 'd', 'c']


# 5) clear()
list11 = ['a', 'b', 'c']
list11.clear()
print(list11) # []


# 6) index()
list12 = ['a', 'b', 'c', 'b']
index = list12.index('b')
print(index) # 1

# And index() with range
index2 = list12.index('b', 2) # (3): Here range define that from 2 index gimme the index of b but not before 2 index
print(index2)


# 7) count()
list13 = ['a', 'b', 'c', 'c', 'c']
print(list13.count('c')) # 3


# 8) reverse()
list14 = ['a', 'b', 'c']
list14.reverse()
print(list14) # ['c', 'b', 'a']


# 9) sort()
list15 = [30, 10, 50, 20, 40]
list15.sort()
print(list15) # [10, 20, 30, 40, 50] : Default sorting is Ascending but we can convert it into Descending.

list15.sort(reverse=True)
print(list15) # [50, 40, 30, 20, 10]

# Sorting with key
list16 = ['Banana', 'Cherry','Apple']
list16.sort(key = len)
print(list16) # ['Apple', 'Banana', 'Cherry']


# 10) pop()
list17 = [30, 10, 50, 20, 40]
result = list17.pop(2) # return the deleted element (50)
list17.pop() #  [30, 10, 20] By default it removes the last element from the list
print(list17) # [30, 10, 20]


# 11) copy()
list18 = [30, 10, 50, 20, 40]
list19 = list18.copy() # it's a shallow copy
list19.sort()
print(list18) # [30, 10, 50, 20, 40]
print(list19) # [10, 20, 30, 40, 50]