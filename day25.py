
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
class User1:
    def __init__(self, name, email, password):
        self.userName = name
        self.userEmail = email
        self.__userPassword = password # Now this password is private because of double underscore(__)
    def details(self):
        print(f'User name is {self.userName}, email is {self.userEmail} and password is {self.__userPassword}')
user1Details = User1('Ali', 'ali@gmail.com', 123123)
user2Details = User1('Ahmed', 'ahmed@gmail.com', 10201020)
# print(user1Details.__userPassword) # Error ❌
# If we want to use or to access that private property, so we can access that property inside method like:
user2Details.details() # Password is also accessable here.


#----------------------------------------------------------------------------------


# 3️⃣ Inheritance: Allows one class (child class) to reuse the properties and methods of another class (parent class).
class User2(User1): # User2 child class inherit the properties and methods from User1 parent class.
    def __init__(self, userName, userEmail, userPassword, address): # old parameters from parent class like (userName, userEmail) and  new parameters in child class like (address)
        super().__init__(userName, userEmail, userPassword) # super() call parent's class init
        self.address = address # new attribute in child class
    def user2Details(self): # self param is mandatory
        super().details() # to inherit the method from parent
        print(f'Hello {self.userName}')
        
user2Object = User2('Naseem', 'naseem@gmail.com', '123', 'Pindi')
user2Object.user2Details()


#--------------------------------------------------------------


# 4️⃣ Polymorphism: A method with same name use in different classes but work with different behavior in each class.