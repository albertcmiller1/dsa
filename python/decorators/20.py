import functools

'''
Recall that the decorator syntax @my_decorator is just an easier way of saying func = my_decorator(func). 
Therefore, if my_decorator is a class, it needs to take func as an argument in its .__init__() method. 
Furthermore, the class instance needs to be callable so that it can stand in for the decorated function.
'''

'''
The .__call__() method will be called instead of the decorated function. 
It does essentially the same thing as the wrapper() function in our earlier examples. 
Note that you need to use the functools.update_wrapper() function instead of @functools.wraps.
'''

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")

say_whee() 
say_whee() 
say_whee() 
print(say_whee.num_calls)
print(isinstance(say_whee, CountCalls))