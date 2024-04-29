arr = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5]

def right_bs(arr, target):
    L, R = 0, len(arr)
    while L<R: 
        M=(L+R)//2
        if arr[M]>target: 
            R=M
        else: 
            L=M+1
    return L

assert right_bs(arr, 0) == 2
assert right_bs(arr, 4) == 11
assert right_bs(arr, 5) == len(arr)
assert right_bs(arr, 6) == len(arr)
assert right_bs(arr, -5) == 0
