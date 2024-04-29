import bisect
arr = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5]

def left_bs(arr, target):
    L, R = 0, len(arr)
    while L<R: 
        M=(L+R)//2
        if arr[M]>=target: 
            R=M
        else: 
            L=M+1
    return L

assert left_bs(arr, 1) == 2
assert left_bs(arr, 4) == 8
assert left_bs(arr, 10) == len(arr)
assert left_bs(arr, -10) == 0


assert bisect.bisect_left(arr, 1) == 2
assert bisect.bisect_left(arr, 4) == 8
assert bisect.bisect_left(arr, 10) == len(arr)
assert bisect.bisect_left(arr, -10) == 0