x = 10
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        print(x)    # 6 
    inner()
outer()
print(x)    # 10 
