class Dog: 
    pass 

buddy = Dog()
buddy.name = "buddy"

print(buddy.__dict__) 


'''
'Hello'.name = 'Fred' # AttriuteError
'''

# __slots__ turn the internals of an object to a tuple 
class Point(object): 
    __slots__ = ('x', 'y') # tuples are immutible 

point = Point()
point.x = 5
point.y = 8
# point.name = "fred" # AttributeError: 'Point' object has no attribute 'name'
# print(point.__dict__) # cant do this either 

'''
when to use __slots__
    > creating many instances of a class 
    > know in advance what properties the class should have 

'''