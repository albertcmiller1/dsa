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

ROWS, COLS = len(graph), len(graph[0])

def is_last_position(r, c): 
    return r == ROWS - 1 and c == COLS - 1

def is_ob(r, c):
    return min(r, c) < 0 or r >= ROWS or c >= COLS

def visited(r, c, visit): 
    return (r, c) in visit

def invalid(r, c): 
    return graph[r][c] == 1

def dfs(r, c, visit): 
    if (is_ob(r,c) or visited(r, c, visit) or invalid(r, c)):
        return 0

    if is_last_position(r, c): 
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(r+1, c, visit)
    count += dfs(r-1, c, visit)
    count += dfs(r, c+1, visit)
    count += dfs(r, c-1, visit)

    visit.remove((r, c))
    return count 

assert dfs(0, 0, set()) == 2

# O(4^(N*M)) time 
# O(N*M) memory 