arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def regular_bs(arr, target):
    L, R = 0, len(arr)-1
    while L<=R: 
        M=(R+L)//2
        if arr[M]==target: 
            return M
        elif arr[M]>target: 
            R=M-1
        else: 
            L=M+1
    return -1

assert regular_bs(arr, 0) == 0
assert regular_bs(arr, 3) == 3
assert regular_bs(arr, 7) == 7
assert regular_bs(arr, 9) == 9
assert regular_bs(arr, 15) == -1