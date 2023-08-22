# basic example of a decorator 

def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        print("something before")
        func()
        print("something after")
        # Do something after the function.
    return wrapper_func



@my_decorator_func
def main():
    print('hello from main')


main()
print(main.__name__)
print(main.__doc__)
