asteroids = [5,10,-5]
stack = []
for a in asteroids:
    while stack and stack[-1]>0 and a<0:
        # top of stack is positive and asteroid is negative 
        if (stack[-1] + a) < 0: 
            # net sum in negative 
            stack.pop()
        elif (stack[-1] + a) > 0: 
            # net sum is positive 
            break    
        else: 
            # equal 
            print("equal")
            stack.pop()
            break
    else: 
        stack.append(a)        
print(stack)