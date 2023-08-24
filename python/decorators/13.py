# https://realpython.com/primer-on-python-decorators/#decorating-functions-with-arguments


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")

greet("world")



print("\n"*2)

# returns a reference to the wrapper function, which can take args 
def do_twice_2(func):
    def wrapper_do_twice_2(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice_2


def greet_2(name):
    print(f"Hello {name}")



foo = do_twice_2(greet_2)
foo("World")