'''
Inheritance allows capabilities of existing class to be reused and if required extended to design new class.
Instead of starting from scratch, you can create a class by deriving it from a pre-existing class by listing the parent class in parentheses after the new class name.
'''

class Parent: # define parent class
    def __init__(self):
        self.attr = 100
        print("Calling parent constructor")
    
    def parentMethod(self):
        print('Calling parent method')

    def set_attr(self, attr):
        self.attr = attr
    
    def get_attr(self):
        print("Parent attribute :", self.attr)

class Child(Parent): # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')

c = Child()         # Calling child constructor
c.childMethod()     # Calling child method
c.parentMethod()    # Calling parent method
c.set_attr(200)     # 
c.get_attr()        # Parent attribute : 200