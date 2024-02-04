# https://realpython.com/python3-object-oriented-programming/

# parent class
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# child classes 
# Instances of child classes inherit all of the attributes and methods of the parent class
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.speak("woof"))
print(miles.species)
print(type(miles))
print(isinstance(miles, Dog))
print(isinstance(miles, JackRussellTerrier))