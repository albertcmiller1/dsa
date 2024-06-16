class Parent1: 
    def __init__(self, val) -> None:
        self.foo = val

class Parent2: 
    def __init__(self, val) -> None:
        self.bazz = val

class Child(Parent1, Parent2): 
    def __init__(self):
        # Parent.__init__(self)
        Parent1.__init__(self, 88)
        Parent2.__init__(self, 99)
        # super().__init__(99)
        self.bar = 0


c = Child()
print(c.bar)
print(c.foo)
print(c.bazz)