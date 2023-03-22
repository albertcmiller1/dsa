
def myfunc_1(a,b, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)
    for ar in args:
        print(ar)

def myfunc(a,b, **kwargs):
    print(a)
    print(kwargs['c'])

myfunc(a='alpha',b='bravo',c='charlie',d='delta')