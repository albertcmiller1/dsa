'''
An instance method accesses the instance variables of the calling object 
because it takes the reference to the calling object. 
But it can also access the class variable as it is common to all the objects.

>> ask ChatGPT the difference between class method and instance method
'''

class Employee:
    num_employees = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.num_employees += 1

    @classmethod
    def show_count(cls):
        print(cls.num_employees)

    @classmethod
    def new_employee(cls, name, age):
        return cls(name, age)


e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.new_employee("Anil", 21)

e1.show_count()
Employee.show_count()
