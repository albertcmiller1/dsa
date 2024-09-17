# class Company: 
#     def __init__(self, address):
#         self.address = address
#         print('Company created')


#     def p(self): 
#         print("im a cool company.")


# class Employee(Company):
#     def __init__(self, name, address):
#         print('Employee created')
#         super().__init__("wall street")
#         self.address = address
#         self.name = name 


# obj = Employee("albert", "nyny")
# print(obj.address)
# obj.p()


def foo(): 
    print("starting foo")
    yield 5
    yield 6
    print("ending foo")


print("pre foo call")
soln = foo()
print("post foo call")
for x in soln: 
    print(x)