# defining a OOP style student class

class Student:
    def __init__(self, name, ID, age, dep, CGPA):
        self.name = name
        self.ID = ID
        self.age = age
        self.dep = dep
        self.CGPA = CGPA

# creating a list of students

class main:
    
    students = [
        Student("Alice", "S001", 20, "Computer Science", 3.5),
        Student("Bob", "S002", 21, "Mathematics", 3.8)]

     #printing the list of students

    print("List of Students:")
    for student in students:
        print(f"Name: {student.name}, ID: {student.ID}, Age: {student.age}, Department: {student.dep}, CGPA: {student.CGPA}")