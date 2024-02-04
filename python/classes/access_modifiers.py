'''
A class member is said to be public if it can be accessed from anywhere in the program. 
Private members are allowed to be accessed from within the class only.


'''

class Employee:
   def __init__(self, name, age, salary):
      self.name     = name      # public variable
      self.__age    = age       # private variable
      self._salary  = salary    # protected variable
   
   def displayEmployee(self):
      print("Name: ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee("Bhavana", 24, 10000)


e1.displayEmployee()        # Name:  Bhavana , age:  24 , salary:  10000
print(e1.name)              # Bhavana
print(e1._salary)           # 10000, still modifiable and accessable 
print(e1._Employee__age)    # "name mangling", dont do this,  bad practice
print(e1.__age)             # AttributeError: 'Employee' object has no attribute '__age'