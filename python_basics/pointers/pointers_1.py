num1 = 11
num2 = num1

'''
is num2 pointing to its own 11 in memory? 
or is num2 pointing to the same slot in memory as num1? 
aka ... if we update num1, will num2 still be 11 or not? 
'''

print("before num2 value is updated: ")
print(f"num1: {num1} at point {id(num1)}")  # 4346356864
print(f"num2: {num2} at point {id(num2)}")  # 4346356864
print("\n")

num1 = 22

print("after num2 value is updated: ")
print(f"num1: {num1} at point {id(num1)}")  # 4346357216
print(f"num2: {num2} at point {id(num2)}")  # 4346356864 

'''
as you can see, a new point in memory is created for num1 when we try to update. 
this is because the int type is immutable. this is not the case for dictionarys !!
'''