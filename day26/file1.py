import file2

from file2 import list # I can also change the name of list by using 'as' keyword
# And this code is for importing the specific part of the file like:
#  from <file_name> import <part>

file2.myName('M Saqib Khan')
print(list)


# Module (file): A single file is called module


# Package (folder): Collection of modules (python files and __init__ file)


# Library: Collection of Packages and Moules is called Library.
# For example: 'math' is a built-in library of Python
# So I can use it like: import math


# Python PIP: PIP stands for "Pip Installs Packages". It is the package manager for Python that allows you to install, update, and manage Python libraries (packages) from the Python Package index (PyPl).
# For installing packages, we use: 
#     pip install <library_name>
# For Example: 
#     pip install pandas 