x = 300         # ref count = 1
y = 300         # ref count = 2
z = [300, 300]  # ref count = 4
x = True        # ref count = 3
del y           # ref count = 2

'''
the del keyword 
    > will remove the "name" as a reference to that object 
    > reduces the ref count by 1
'''


def print_hello(): 
    greeting = "Hello" # ref count = 1
    print(greeting)

print_hello()
# when the greeting object goes out of scope, the ref count goes back to 0