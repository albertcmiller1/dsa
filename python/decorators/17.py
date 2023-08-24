import functools

# The * in the argument list means that the remaining arguments can’t be called as positional arguments.
# another way to do it: https://docs.python.org/3/library/functools.html#functools.partial
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


# @repeat(num_times=4)
@repeat
def greet(name):
    print(f"Hello {name}")


greet("albert")