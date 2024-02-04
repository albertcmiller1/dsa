'''
break the arrays into sub-arrays and sort them individually, which results in a sorted array. 

Stable
best case time: O(n)
worst case time O(n^2)

[2, 3, 4, 1]
[2, 3, 1, 4]
[2, 1, 3, 4]
[1, 2, 3, 4]
'''

def insertion_sort(nums: list[int]) -> list[int]:

    for i in range(1, len(nums)):
        j = i - 1

        while (j>=0 and nums[j] > nums[j+1]):
            tmp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = tmp
            j -= 1
        
    return nums


assert insertion_sort([2, 3, 4, 1]) == [1, 2, 3, 4]
assert insertion_sort([2, 3, 4, 1, 8]) == [1, 2, 3, 4, 8]