def outer_function():
    def inner_function():
        print('I came from the inner function.')

    # Executing the inner function inside the outer function.
    inner_function()

outer_function()