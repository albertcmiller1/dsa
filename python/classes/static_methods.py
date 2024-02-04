'''
static methods dont have mandatory arguments like reference to the object (cls, self)
'''

class Employee:
   num_employees = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.num_employees += 1
   
   @staticmethod
   def showcount():
        print(Employee.num_employees)
        return


e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

Employee.showcount()