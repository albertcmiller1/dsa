class Test:
    def __init__(self):
        print("initalizing test class")


    @staticmethod
    def parse_info():
        print("parsing some info")
        other_stuff()


    def other_stuff(self):
        print("helper function")
        self.parse_info()



Test.parse_info()
print("\n")

t = Test()
t.other_stuff()


