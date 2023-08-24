# he .__call__() method is executed each time you try to call an instance of the class

class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")


c = Counter()

c()