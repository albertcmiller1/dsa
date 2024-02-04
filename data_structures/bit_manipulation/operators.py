def and_opr(): 
    ans = 1 & 1 

    print(ans)

def or_opr(): 
    ans = 1 | 0 
    print(ans)

def xor_opr(): 
    ans = 1 ^ 0 
    print(ans)

def negation_opr():
    ans = ~-10
    print(ans)
    ans = ~10
    print(ans)

def bit_shift():
    ans = 100 >> 1
    print(ans)

def countBits(n):
    # 23 = 10111
    #  1 = 00001
    # 10111 & 00001 => 00001 

    # 11 = 01011
    #  1 = 00001
    # 01011 & 00001 => 00001 

    # 5 = 00101
    #  1 = 00001
    # 00101 & 00001 => 00001 

    # 2 = 00010
    # 1 = 00001
    # 00010 & 00001 => 00000 

    # 1 = 00001
    # 1 = 00001
    # 00001 & 00001 => 00001 


    count = 0
    while n > 0: 
        if n & 1 == 1: # check if the last digit is 1
            count += 1
        n = n >> 1  # shift to the right 
    return count 
    
    

if __name__ == "__main__":
    # print((255).bit_length()) 
    # print(bin(255))
    # print(int('11111111', 2)) 

    # and_opr()
    # or_opr()
    # xor_opr()
    # negation_opr()
    # bit_shift()
    print(countBits(23))
    