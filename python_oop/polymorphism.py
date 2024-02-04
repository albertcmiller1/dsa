'''
The term "polymorphism" refers to a function or method taking different form in different contexts
If a method in a parent class is overridden with different business logic in its different child classes, the base/parent class method is a polymorphic method.
'''

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract method"
        # print("abstract method from ABC") # Note what happens if we uncomment this. 
        pass

class circle(shape):
    def draw(self):
        super().draw()
        print("Draw a circle")
        return

class rectangle(shape):
    def draw(self):
        super().draw()
        print("Draw a rectangle")
        return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()