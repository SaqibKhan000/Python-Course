
###################### Assignment-6 ########################

# Q1 Find the Intersection (common elements) of Two Lists? 
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8]
# Using for loop
def intersection_loop(lst1, lst2):
    common_list = []
    for item in lst1:
        if item in lst2 and item not in common_list:
            common_list.append(item)
    return common_list
print(intersection_loop(list1, list2))

# Using list comprehensions
def intersection_loop(lst1, lst2):
      return [item for item in lst1 if item in lst2]
print(intersection_loop(list1, list2))

#------------------------------------------------------------


# Q2 Find the Most Frequent Element in a List? 
numbers = [1,2,2,3,3,3,4,7,7,7,7]
def freq_values(lst):
     most_freq = None
     max_count = 0
     for num in lst:
          count = lst.count(num)
          if count > max_count:
               max_count = count
               most_freq = num
     return most_freq
print(freq_values(numbers))

#----------------------------------------------------------------

# Q3 Find Cumulative Sum of a List
numbers = [1, 2, 3, 4]
def sum(lst):
     val = 0
     list = []
     for item in lst:
               val += item
               list.append(val)
     return list
print(sum(numbers))

#----------------------------------------------------------------

# Q4 Remove Duplicates from a List 
fruits = ["apple", "banana", "mango", "apple", "banana"]
def remove_dup(lst):
     unique = []
     for item in lst:
          if item not in unique:
               unique.append(item)
     return unique
print(remove_dup(fruits))

# Using set constructor             
print(list(set(fruits)))