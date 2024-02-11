# Global variable
x = 10

def print_global_variable():
    # Accessing the global variable
    print("Value of x inside the function:", x)

def modify_global_variable():
    # Attempting to modify the global variable without using 'global' keyword
    # This will result in an UnboundLocalError
    x += 1
    print("Value of x inside the function after incrementing:", x)

def modify_global_variable_correctly():
    global x  # Declare 'x' as a global variable
    x += 1
    print("Value of x inside the function after incrementing:", x)

# Calling functions
print_global_variable()
modify_global_variable_correctly()

'''

In Python, you can access global variables from within a function without any issues. 
However, if you want to modify a global variable within a function, 
you need to use the global keyword to explicitly declare that you intend to modify the global variable, 
rather than creating a local variable with the same name. 
This is a safety mechanism in Python to prevent accidental modification of global variables within functions.
'''