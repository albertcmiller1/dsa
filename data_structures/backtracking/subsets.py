def subsets(nums):
    soln = []
    curr = []
    def backtrack(i):
        if i>len(nums):
            return 
        
        soln.append(curr[:])
        for j in range(i, len(nums)):
            curr.append(nums[j])
            backtrack(j+1)
            curr.pop()
    
    backtrack(0)
    return soln 

print(subsets([1, 2, 3]))