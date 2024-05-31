class Parent1:
    def __init__(self, param1):
        self.param1 = param1

class Parent2:
    def __init__(self, param2):
        self.param2 = param2

class Child(Parent1, Parent2):
    def __init__(self, param1, param2):
        Parent1.__init__(self, param1)  # Call Parent1's constructor
        Parent2.__init__(self, param2)  # Call Parent2's constructor

child_instance = Child('value1', 'value2')
print(child_instance.param1)  # Output: 'value1'
print(child_instance.param2)  # Output: 'value2'