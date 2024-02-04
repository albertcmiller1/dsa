# https://realpython.com/primer-on-python-decorators/

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

one = parent(1) # returns a reference to the local one function 
print(one)
print(one())
print("\n")

two = parent(2)
print(two)
print(two())