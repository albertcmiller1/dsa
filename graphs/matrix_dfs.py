'''
count the unique paths from the top left to the bottom right. 
a single path may only move along 0's and cant visit the same cell more than once. 
'''

graph = [
    [0,0,0,0],
    [1,1,0,0],
    [0,0,0,1],
    [0,1,0,0]
]


def dfs(grid, r, c, visit): 
    ROWS, COLS = len(grid), len(grid[0])

    if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1):
        return 0

    if r == ROWS - 1 and c == COLS - 1: 
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r+1, c, visit)
    count += dfs(grid, r-1, c, visit)
    count += dfs(grid, r, c+1, visit)
    count += dfs(grid, r, c-1, visit)

    visit.remove((r, c))
    return count 

assert dfs(graph, 0, 0, set()) == 2

# O(4^(N*M)) time 
# O(N*M) memory 