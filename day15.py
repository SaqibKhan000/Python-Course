
# STRING INDEXING, SLICING  AND METHODS:

# INDEXING:
name = "MSaqibKhan"
print(name[0])
print(name[-1])



# SLICING:
print(name[0:3]) # MSa
print(name[:]) # all values
print(name[0::2]) # The third one value is for steps, default value is one(1): Answer(MaiKa). And If I leave the end-index value so it will auto set the last index value.
print(name[-1:]) # n
print(name[-5:]) # bKhan: From -5 to -1.
print(name[1:-1]) # SaqibKha
print(name[::-1]) # nahKbiqaSM: For reversing a string



# METHODS:
# 1) len()
print(len(name)) # 10

# 2) upper()
print(name.upper()) # MSAQIBKHAN

# 3) lower()
print(name.lower()) #msaqibkhan

# 4) strip()
sentence = "    Hello! world"
print(sentence.strip()) # Remove the whitespaces. 

# 5) count()
sentence2 = "Hi, hello hi hello"
print(sentence2.count('hello')) # (2): Because count of hello is 2.

# 6) find()
print(name.find('a')) # (2): Because index of 'a' is 2 in name variable.

# 7) title()
print(sentence2.title()) # Hi, Hello Hi Hello: This method converts the first character of each word in upper case.

# 8) split()
name2 = "M Saqib Khan"
print(name.split(" ")) # ['M', 'Saqib', 'Khan']: This method converts the string in List.

# 9) replace()
# str.replace(old, new)
print(name.replace('Saqib', 'Millionaire')) # MMillionaireKhan

# 10) join()
studio = ['Mic', 'Tripod', 'Camera']
print(" ".join(studio)) # Mic Tripod Camera: This method converts the touple or list in string.