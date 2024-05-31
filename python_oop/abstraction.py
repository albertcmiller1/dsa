from abc import ABC, abstractclassmethod

class Shape(ABC): 
    @abstractclassmethod # i think this works but is techically wrong. abstractclassmethod should be used on class methods: def foo(cls, param)
    def area(self): pass

    @abstractclassmethod
    def perimeter(self): pass

    '''
    abstract methods: must be implemented in the sub class
    cannot instantiate the abstract class
    '''

class Square(Shape):
    def __init__(self, side): 
        self._side = side

    def area(self): 
        return self._side *  self._side

    def perimeter(self): 
        return self.side * 4


# shape = Shape()       #TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

square = Square(5)      
