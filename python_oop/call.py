class Albert: 
    def __init__(self, albert):
        print("hello init function")
        self.albert = albert

    def __call__(self):
        print("hello from call func")
        return self.albert


foo = Albert("chris")
doo = Albert("albert")
foo() 