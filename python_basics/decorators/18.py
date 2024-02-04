import functools

'''
KEEPING STATE 
In the beginning of this guide, we talked about pure functions returning a value based on given arguments. 
Stateful decorators are quite the opposite, where the return value will depend on the current state, as well as the given arguments.
'''

def count_calls(func):
    print("this only happens once???")
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    print("this also only happens once???")
    return wrapper_count_calls

# The decorator syntax @my_decorator is just an easier way of saying func = my_decorator(func).
@count_calls
def say_whee():
    print("Whee!")

def shit(): 
    print('shit')
    shit.num_calls = 0
    shit.num_calls += 1
    print(shit.num_calls)

# shit()
# shit()
# shit()

say_whee()
say_whee()
say_whee()