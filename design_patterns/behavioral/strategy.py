'''
modify or extend the behvior of a class without directly changing it

Open-Closed Principle
    > open: for extension 
    > closed: for modifications 
'''


class ABC: 
    pass 

def abstractmethod(): 
    pass 

class FilterStrategy(ABC): 
    @abstractmethod
    def removeValue(self, val): 
        pass 


class RemoveNegativeStrategy(FilterStrategy): 
    def removeValue(self, val): 
        return val < 0

class RemoveOddStrategy(FilterStrategy): 
    def removeValue(self, val): 
        return abs(val) % 2

    

class Values: 
    def __init__(self, vals): 
        self.vals = vals 

    def filter(self, strategy): 
        res = []
        for n in self.vals: 
            if not strategy.removeValue(n): 
                res.append(n)
        return res 

values = Values([-7, -4, -1, 0, 3, 6, 9])

print(values.filter(RemoveNegativeStrategy())) # [0, 3, 6, 9]
print(values.filter(RemoveOddStrategy())) # [-4, 0, 6]


