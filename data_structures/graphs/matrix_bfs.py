'''
Question: find the length of the shortest path from the top left of the grid to the bottom right 
'''


from collections import deque 

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

def bfs(grid): 
    ROWS, COLS = len(grid), len(grid[0])
    visit = set() 
    queue = deque()
    
    visit.add((0,0))
    queue.append((0,0))        

    length = 0
    while queue: 
        for _ in range(len(queue)): 
            r, c = queue.popleft()

            # is bottom right position
            if r == ROWS-1 and c == COLS-1: 
                return length

            neighbors = [
                [0, 1],
                [0,-1],
                [1, 0],
                [-1,0]
            ]

            for dr, dc in neighbors: 
                if (
                    min(r+dr, c+dc)<0 or 
                    r+dr==ROWS or c+dc == COLS or 
                    (r+dr, c+dc) in visit or 
                    grid[r+dr][c+dc]==1
                    ):
                    continue 

                queue.append((r+dr, c+dc))
                visit.add((r+dr, c+dc))
            
            length+=1

print(bfs(grid))


# o(n*m)