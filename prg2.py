class Student:
    college_name = "ABC College"
    def __init__(self, name):
        self.sname = name
    def f1(self):
        print("Name:", self.sname)
        print("College Name:", Student.college_name)
s1=Student("Alice")
s2=Student("Bob")
s3=Student("Charlie")

