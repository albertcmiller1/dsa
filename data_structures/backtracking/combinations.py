def combine(n, k):
    ''' 
    return all possible combinations of k numbers from range 1 to n
    k = 2
    n = 4
    [1, 2, 3, 4]

    [
        [1,2],
        [1,3],
        [1,4],
        [2,3],
        [2,4],
        [3,4]
    ]
    '''
    soln = []
    curr = []
    def backtrack(i):
        if len(curr) == k: 
            soln.append(curr[:])
            return 
        
        for num in range(i, n+1):
            curr.append(num)
            backtrack(num+1)
            curr.pop()

    backtrack(1)
    return soln 

print(combine(4, 2))
'''
first call loop run n times 
then n-1 
aka n!
we also copy an array of size k 
so O(k*n!) is a close approximation 


'''