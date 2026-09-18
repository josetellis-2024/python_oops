class Employee(object):
    company_name = "Google"
    def __init__(self, name, salary):
        self.__ename = name
        self.__esalary = salary
    def __str__(self):
        return f"Employee Name: {self.__ename}, Salary: {self.__esalary}, Company: {Employee.company_name}"
    def __repr__(self):
        return f"Employee('{self.__ename}', {self.__esalary})"
e1=Employee("David", 50000)



