'''
[2, 1, 2, 0, 0, 2]

loop over each element, and count each element 
{
    0: 2
    1: 1
    2: 3, 
}
or could use an array 
 
 0  1  2
[2, 1, 3]


O(n) time 
not stable 
'''



def bucket_sort(arr: list[int]) -> list[int]:

    counts = [0 for _ in range(max(arr)+1)]
    for n in arr: 
        counts[n] += 1

    i = 0
    for j in range(len(counts)):
        for _ in range(counts[j]):
            arr[i] = j
            i += 1

    return arr

assert bucket_sort([2, 1, 2, 0, 0, 2]) == [0, 0, 1, 2, 2, 2]
assert bucket_sort([2, 1, 2, 1, 1, 3, 4]) == [1, 1, 1, 2, 2, 3, 4]