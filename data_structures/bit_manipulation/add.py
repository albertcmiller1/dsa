# these half adders wont work for negative values. 
def half_adder_iterative(x, y):
    while (y != 0):
        carry = x & y 
        x = x ^ y
        y = carry << 1
    return x
# print(half_adder_iterative(27,5))

def half_adder(a, b):
    if a==0 or b==0: 
        return a | b
    return half_adder(a^b, (a&b)<<1)
# print(half_adder(9, 5))

# this one will work with negative values. 
def getSum(a: int, b: int) -> int:
    def add(a, b):
        if not a or not b:
            return a or b
        return add(a ^ b, (a & b) << 1)

    # either a or b is negative. 
    if a * b < 0:  # assume a < 0, b > 0
        if a > 0:
            return getSum(b, a)
        if add(~a, 1) == b:  # -a == b
            return 0
        if add(~a, 1) < b:  # -a < b
            # -add(-a, -b)
            return add(
                ~add(add(~a, 1), add(~b, 1)), 1)  

    return add(a, b)  # a*b >= 0 or (-a) > b > 0

# print(getSum(5, -3))


def getSum2(a, b):
    b32 = 0xffffffff
    while (b&b32)>0: 
        carry = (a&b)<<1
        a = (a^b)
        b = carry
    return (a&b32) if b>0 else a


x = getSum2(3, 2)
print(x)
