

foo = 0

def dummy(): 
    foo += 1

dummy() 

'''
UnboundLocalError: cannot access local variable 'foo' where it is not associated with a value
'''
print(foo)