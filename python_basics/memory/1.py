word_1 = "programming"
word_2 = "programming"
print(id(word_1)) # same address
print(id(word_2)) # same address 
print(word_1 is word_2)
'''
these are the same, because the sting 'programming' is an immutilbe primitive type, 
and thus makes the same object twice
this object would have a reference count of 2
'''

foo_1 = "foo"
foo_2 = "bar"
print(id(foo_1)) # diff address 
print(id(foo_2)) # diff address 
print(foo_1 is foo_2)