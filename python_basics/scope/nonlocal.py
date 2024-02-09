'''
The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
https://www.w3schools.com/python/ref_keyword_nonlocal.asp
Use the keyword nonlocal to declare that the variable is not local.
'''

def myfunc1():
  x = "John" # in function scope of myfunc1
  def myfunc2():
    nonlocal x     # bring out the other x, and use it here
    x = "hello"
  myfunc2()
  return x

# same example as above but without nonlocal
def myfunc1_():
  x = "John"
  def myfunc2_():
    x = "hello"
  myfunc2_()
  return x

print(myfunc1())     # hello
print(myfunc1_())    # John 