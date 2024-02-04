class Schemas: 
    def __init__(self, albert):
        print("hello init function")
        self.albert = albert

    def __call__(self):
        print("hello from call func")
        return self.albert


foo = Schemas("chris")
doo = Schemas("chris")
foo() 
# print(foo.albert)