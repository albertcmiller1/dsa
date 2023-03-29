
def myfunc_1(a,b, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
    for ar in args:
        print(ar)

def myfunc(a,b, **kwargs):
    print(a)
    # print(kwargs['c'])
    for item in kwargs.items():
        print(item[0])
    # print(item for item in kwargs.items())

def myotherfunc(a, b, *args):
    print(f"a: {a}")
    print(f"b: {b}")
    print(args)

# myfunc(a='alpha',b='bravo',c='charlie',d='delta')
myotherfunc('charlie','delta', "alpha", "bravo")