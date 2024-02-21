'''
https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression

max(a, b, c, ...[, key=func]) -> value
min(a, b, c, ...[, key=func]) -> value


key compares items based on a set of rules based on the type of the objects (for example a string is always greater than an integer)
To modify the object before comparison, or to compare based on a particular attribute/index, use the key argument.
'''

target = 3.7
nums = [4, 2, 5, 1, 3]
soln = min(nums, key=lambda x: abs(target-x))
print(soln) # 4




lis = [(1,100), (3,101), (4,102), (-1, 103)]
print(max(lis, key = lambda x: x[1])) # (-1, 103)