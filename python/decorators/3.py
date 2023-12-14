def outer_function():
    '''Assign task to student'''

    task = 'Read Python book chapter 3.'
    def inner_function():
        print(task)
        
    return inner_function

homework = outer_function()

homework()