from functools import wraps

def my_decorator_func(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
        print(args)

    return wrapper_func

@my_decorator_func
def main(my_args):
    '''Example docstring for function'''
    print('main func')

    pass

# use functools.wraps to fix the issue seen in ex 5.py
main("arg1")
print(main.__name__)
print(main.__doc__)