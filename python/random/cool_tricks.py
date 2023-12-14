# interesting return statement 
def is_alnum(c):
    return (
        ord("A") <= ord(c) <= ord("Z") or
        ord("a") <= ord(c) <= ord("z") or 
        ord("0") <= ord(c) <= ord("9")
    )

print(is_alnum("G"))
print(is_alnum("&"))


# condensed if else 
print("fiz") if True else print("buzz") 

# create an array 
nums = [1,2,2,4,6,7,7,7,8]
feq = [i for i in range(len(nums))]
feq = [i*i for i in range(len(nums))]
feq = [[] for i in range(len(nums))]


foo = (1, 2, 3)
new_foo = [*foo]

print((0<=5<=9))

# dictionary .get method 
dic = {
    'foo': 0
}
dic['bazz'] = dic.get('bazz',0) 
'''
dic.get(key, value)
key: required 
value: optional --> A value to return if the specified key does not exist.
'''


# dictionary .items method 
dic = {
    'foo': 0,
    'bar': 1,
    'bazz': 2
}
for k,v in dic.items(): 
    print(k)
    print(v)

# range function ==> range(start, stop, step)


# generators 
# https://www.programiz.com/python-programming/generator
