'''
We will pick a pivot if we haven't already hit the base case which is array of size 1 and pick a left pointer, which will point to the left-most element of the current subarray to begin with. 
Then, we will iterate through our array and if we find an element smaller than our pivot element, we will swap the current element with the element at our left pointer and increment the left pointer.

Once this condition terminates, we will bring the left element to the end of the array and bring the pivot element to the left position. 
This makes sense because once we have exhausted all the elements that are smaller than the pivot element, and put them to the left of the pivot, left will now be at the first element that is greater than the pivot. 
And, every element after it will also be greater than the pivot. 
This results in all the elements less than or equal to the pivot to be on the left and the rest on the right.

[6,  2,  4,  1,  3]
L,i              p

> no swap, incremenet i 

[6,  2,  4,  1,  3]
 L   i           p 

> 2 is less than 3
> swap, increment both 

[2,  6,  4,  1,  3]
 L   i           p 

[2,  6,  4,  1,  3]
     L   i       p 

> no swap, increment i 

[2,  6,  4,  1,  3]
     L       i    p 

> 1 is less than 3
> swap, increment both

[2,  1,  4,  6,  3]
     L       i    p 

[2,  1,  4,  6,  3]
         L      i,p 

> i at end. move L to end 

[2,  1,  4,  6,  4]

> overwrite left with pivot 

[2,  1,  3,  6,  4]

'''

def sort(nums):
    def quick_sort(arr: list[int], L: int, E: int):
        if (E-L < 1): return arr

        pivot = arr[E]

        # partition: elements smaller than pivot on the left side.
        for i in range(L, E):
            if arr[i] < pivot: 
                tmp = arr[L]
                arr[L] = arr[i]
                arr[i] = tmp
                L += 1
        
        arr[E] = arr[L]             # replace end value with value at L
        arr[L] = pivot              # replace value at L with pivot         
        quick_sort(arr, 0, L-1)     # sort left side  (excluding middle)
        quick_sort(arr, L+1, E)     # sort right side (excluding middle)

        return arr

    return quick_sort(nums, 0, len(nums)-1)


print(sort([6, 2, 4, 1, 3]))
# print(sort([1, 3, 2, 4, 2, 5, 7, 5, 9, 5, 2]))
assert sort([1, 2, 3, 0]) == [0, 1, 2, 3]
assert sort([1, 2, 3, 0, 5, 9, 4]) == [0, 1, 2, 3, 4, 5, 9]

'''
Time Complexity 
O(n log n)  best case
O(n^2)      worst case 

Stability
Quicksort is not a stable algorithm because it exchanges non-adjacent elements
'''