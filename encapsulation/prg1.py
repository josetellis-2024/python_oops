class Person:
    def __init__(self, name, age):
        self.__pname =name
        self.__page =age
    def f1(self):
        print("Name:",self.__pname)
        print("Age:",self.__page)
    @classmethod
    def f2(cls):
       
       print("class method")
p1=Person("John",25)
Person.f2()




