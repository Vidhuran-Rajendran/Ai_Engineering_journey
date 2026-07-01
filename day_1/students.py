class Student:
    def __init__(self,name,age,marks,grade):
        self.name = name
        self.age = age
        self.marks = marks
        self.grade = grade
    
    def display(self):
        print(f"name of the student: {self.name}")
        print(f"age: {self.age}")
        print(f"marks: {self.marks}")
        print(f"grade: {self.grade}")

s1 = Student("jhon",34,23847,"f")
print(s1.display())
s2 = Student("jane",23,23847,"a")
print(s2.display())