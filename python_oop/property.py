'''
aticles: 
    > https://www.programiz.com/python-programming/property
    > https://realpython.com/python-property/ 


property(fget=None, fset=None, fdel=None, doc=None)
> fget --> an instance method that retrieves value of an instance variable.
> fset --> an instance method that assigns value to an instance variable.
> fdel --> an instance method that removes an instance variable
> fdoc --> Documentation string for the property.

the property function returns a propery object, and acts as an interface to the instance variables.
the propery function provides a solution the the OOP critrea that instance variables should have a restricted private access.

'''

class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name
        return

    def set_age(self, age):
        self.__age=age
        return

    # add property objects as class attributes.
    name = property(get_name, set_name, "name")
    age  = property(get_age, set_age, "age")


e1 = Employee("Bhavana", 24)
print("Name:", e1.name, "age:", e1.age)

e1.name = "Archana"
e1.age = 23
print("Name:", e1.name, "age:", e1.age)

print("\n")
e2 = Employee("Albert", 27)
print("Name:", e1.name, "age:", e1.age)
print("Name:", e2.name, "age:", e2.age)