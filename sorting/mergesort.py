'''
Keep splitting the array into halves until the subarrays hit a size of one, sort them, and merge the sorted arrays, which will result in an ultimate sorted array.
Can be solved with two branch recursion. 

Stable
O(n log n)

'''


def sort_array(nums: list[int]) -> list[int]:
    def merge(arr, L, M, R):
        left = arr[L:M+1]
        right = arr[M+1:R+1]

        i = L
        li = 0
        ri = 0

        while (li < len(left) and ri < len(right)):
            if (left[li] <= right[ri]):
                arr[i] = left[li]
                li += 1
            else: 
                arr[i] = right[ri]
                ri += 1
            i += 1

        while (li < len(left)):
            arr[i] = left[li]
            li += 1
            i += 1
        
        while (ri < len(right)):
            arr[i] = right[ri]
            ri += 1
            i += 1

        return 


    def merge_sort(arr, L, R):
        if L == R: return arr

        M = (L+R) // 2

        merge_sort(arr, L, M)
        merge_sort(arr, M+1, R)
        merge(arr, L, M, R)

        return arr


    return merge_sort(nums, 0, len(nums)-1)


assert sort_array([4, 3, 2, 1, 5]) == [1, 2, 3, 4, 5]
assert sort_array([4, 3, 2, 1]) == [1, 2, 3, 4]
