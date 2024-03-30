'''
A monotonic stack or queue is one whose elements are always sorted. 
It can be sorted either ascending or descending, depending on the algorithm. 
Monotonic stacks and queues maintain their sorted property by removing elements that would violate the property before adding new elements. 
'''
nums  = [14]
stack = [1, 5, 8, 15, 23]
for num in nums:
    while stack and stack[-1] >= num:
        stack.pop()
    # Between the above and below lines, do some logic depending on the problem
    stack.append(num)

# stack = [1, 5, 8, 14]

'''
Monotonic stacks and queues are useful in problems that, for each element, involves finding the "next" element based on some criteria, for example, the next greater element
They're also good when you have a dynamic window of elements and you want to maintain knowledge of the maximum or minimum element as the window changes
'''