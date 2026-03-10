
##################### OOPs In Python #######################

# Class 
# It's the blueprint or template. Use for creating objects
class Student:
    def __init__(self, name, grade, team):
# self parameter build connection btw class and object
        self.name = name
        self.grade = grade
        self.team = team
    def student_details(self):
        print(f"{self.name} is in class {self.grade} and in team {self.team}")
team = 'A'
student1 = Student('Saqib', 12, team)
student2 = Student('Ali', 10, team)
student1.student_details()            
student2.student_details()
print(student1.__dict__) # {'name': 'Saqib', 'grade': 12}
# # __dict__: Gives all the values in key value pairs.    


#--------------------------------------------------------------------


# 1️⃣ Abstraction: Hiding the un-necassary details from user is called abstraction.
# Like we just show the necessary part of the code to user not show the logic behind the output of code


#------------------------------------------------------------------------------


# 2️⃣ Encapculation: Giving privacy to the code or to secure the data us called encapsulation
class User:
    def __init__(self, name, email, password):
        self.userName = name
        self.userEmail = email
        self.__userPassword = password # Now this password is private because of double underscore(__)
    def details(self):
        print(f'User name is {self.userName}, email is {self.userEmail} and password is {self.__userPassword}')
user1Details = User('Ali', 'ali@gmail.com', 123123)
user2Details = User('Ahmed', 'ahmed@gmail.com', 10201020)
# print(user1Details.__userPassword) # Error ❌
# If we want to use or to access that private property, so we can access that property inside method like:
user2Details.details() # Password is also accessable here.


#----------------------------------------------------------------------------------


# 3️⃣ Inheritance: 