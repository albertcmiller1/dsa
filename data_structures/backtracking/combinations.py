from typing import List
def subsets(nums):
    soln   = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            soln.append(subset[:])
            return
        
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        
        # decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return soln

if __name__ == "__main__":
    print(subsets([1, 2, 3]))