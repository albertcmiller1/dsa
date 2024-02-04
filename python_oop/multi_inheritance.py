'''
Multiple inheritance in Python allows you to construct a class based on more than one parent classes. 
The Child class thus inherits the attributes and method from all parents. 
The child can override methods inherited from any parent.

method resolution order
> the mro() method returns the hierarchical order that Python uses to resolve the method to be called
> The resolution order is from bottom of inheritance order to top.

'''

class Division:
    def __init__(self, a, b):
        self.n=a
        self.d=b
    
    def divide(self):
        return self.n/self.d

class Modulus:
    def __init__(self, a, b):
        self.n=a
        self.d=b

    def mod_divide(self):
        return self.n%self.d
      
class Div_mod(Division, Modulus):
    def __init__(self, a,b):
        self.n=a
        self.d=b

    def div_and_mod(self):
        # divval = Division.divide(self)
        # modval = Modulus.mod_divide(self)
        divval = self.divide()
        modval = self.mod_divide()
        return (divval, modval)
  
x = Div_mod(10,3)

print("division:",     x.divide())
print("mod_division:", x.mod_divide())
print("divmod:",       x.div_and_mod())

print(type(x))                  # <class '__main__.Div_mod'>
print(isinstance(x, Division))  # True
print(isinstance(x, Modulus))   # True
print(isinstance(x, Div_mod))   # True

