def permute(nums):
    '''
                [1,2,3]

                1   2   3 

    1 2 3         1 2 3      1 2 3        

    etc..

    '''

    soln = []
    curr = []
    def backtrack():
        if len(curr) == len(nums):
            soln.append(curr[:])
            return
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack()
                curr.pop()
        
    backtrack()
    return soln

print(permute(list(set(["a", "b", "a", "c"]))))
# print(permute([1, 2, 3]))
'''
O(n * !n)
top level makes n calls, then n-1 for each level below 
inside each function, we have to loop over all elements O(n), and check if an element is in curr O(n) could be O(1) if we use set 
'''