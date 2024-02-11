

global x # even if tihs is global, we get unbounded error 
x = 100
def recusion(y): 
    if y==0: 
        return 
    x+=1
    print(x)
    # recusion(y-1)

recusion(2)