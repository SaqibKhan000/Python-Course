
##################### OOPs In Python #######################

# Class 
# It's the blueprint or template. Use for creating objects
class Student:
    def __init__(self, name, grade):
# self parameter build connection btw class and object
        self.name = name
        self.grade = grade
    def student_details(self):
        print(f"{self.name} is in class {self.grade}")
student1 = Student('Saqib', 12)
student2 = Student('Ali', 10)
student1.student_details()            
student2.student_details()
print(student1.__dict__) # {'name': 'Saqib', 'grade': 12}
# # __dict__: Gives all the values in key value pairs.    











