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

print(subsets(["a", "b", "c"]))
# print(subsets([1, 2, 3]))

'''
2^n subets where n is the length of the input array 
for each element, we can either take it or not take it. 
at each node, we make a copy of curr so we get 
O(n*2^n)


['a'], 
['a', 'b'], 
['a', 'b', 'c']
['a', 'c'], 
['b'], 
['b', 'c'], 
['c']



a
ab 
abc
ac
b
bc
c




'''