# Any class in Python is a subclass of object class, so we dont actually need to put "object" there 

'''
getattr(obj, name[, default])   --> to access the attribute of object.
hasattr(obj,name)               --> to check if an attribute exists or not.
setattr(obj,name,value)         --> to set an attribute. If attribute does not exist, then it would be created.
delattr(obj, name)              --> to delete an attribute.
'''


class Employee(object):
    'im the Employee doc'
    # A class attribute is a variable whose value is shared among all the instances of a in this class
    num_employees = 0

    def __init__(self, name="Bhavana", age=24):
        # name and age are instance variables, as their values may be different for each object
        Employee.num_employees += 1
        self.name = name
        self.age = age

    # this is called an instance method
    def displayEmployee(self):
        print ("Name : ", self.name, ", age: ", self.age)




print("Employee.__doc__:",      Employee.__doc__)       # im the Employee doc
print("Employee.__name__:",     Employee.__name__)      # Employee
print("Employee.__module__:",   Employee.__module__)    # __main__
print("Employee.__bases__:",    Employee.__bases__)     # (<class 'object'>,)
print("Employee.__dict__:",     Employee.__dict__ )     # see below ...
'''
{
    '__module__':       '__main__', 
    '__doc__':          'im the Employee doc', 
    '__init__':         <function Employee.__init__ at 0x1043ec7c0>, 
    'displayEmployee':  <function Employee.displayEmployee at 0x10446d300>, 
    '__dict__':         <attribute '__dict__' of 'Employee' objects>, 
    '__weakref__':      <attribute '__weakref__' of 'Employee' objects>
}
'''