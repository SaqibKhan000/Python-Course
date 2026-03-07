
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

#------------------------------------------------------------------

# Q5 Find the index of an element in a tuple
my_tuple = (1, 10, 2, 3, 4)
def find_index(tup, elem):
     return tup.index(elem) if elem in tup else -1
print(find_index(my_tuple, 100))

#------------------------------------------------------------------

# Q6 Find the Most Frequent Value in a dictionary
data = {'a': 2, 'b': 2, 'c': 1, 'd': 3, 'e': 2} 
def most_freq(dict):
     freq = {}
     for value in dict.values():
          if  value not in freq:
               freq[value] = 0
          freq[value] += 1
     max_value = max(freq, key = freq.get)
     return max_value
print(most_freq(data)) # 2

#------------------------------------------------------------

# Q7 Merge Dictionaries with Summation 
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 35, 'd': 25} 
def merge_dict(dict1, dict2):
     result = dict1.copy()
     for key, value in dict2.items():
          if key in result:
               result[key] += value
          else: 
               result[key] = value
     return result
print(merge_dict(dict1, dict2)) # {'a': 10, 'b': 35, 'c': 65, 'd': 25}

#-------------------------------------------------------------

# Q8 Flatten a Nested Dictionary 
data = {'a': {'b': {'c': 42}, 'd': 7}, 'e': 10}
def flatten_dict(data, parent_key='', sep='.'):
     items = {}
     for key, value in data.items():
          new_key = f"{parent_key}{sep}{key}" if parent_key else key
          if isinstance(value, dict): 
               items.update(flatten_dict(value, new_key, sep))
          else:
               items[new_key] = value
     return items
print(flatten_dict(data)) # {'a.b.c': 42, 'a.d': 7, 'e': 10}