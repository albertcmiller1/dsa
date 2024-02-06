from singleton_decorator import singleton

@singleton
class Albert: 
    def __init__(self): 
        print('hello init')

o1 = Albert()
o2 = Albert()
print(o1 is o2)