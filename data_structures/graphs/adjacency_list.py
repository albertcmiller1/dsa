from collections import deque

# GraphNode used for adjaceny list 
class GraphNode: 
    def __init__(self, val): 
        self.val = val 
        self.neighbors = []

# use HashMap 
adjList = { "A": [], "B": [] }


'''
Example problem: 

given directed edges, build an adjacency list 
AKA array of edges 
'''

edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adjList = {} # node, neighbors 
for src, dst in edges: 
    if src not in adjList: 
        adjList[src] = []
    if dst not in adjList: 
        adjList[dst] = []
    adjList[src].append(dst)

print(adjList)

'''
        A
              D
        |     
        \/    ^
              |
        B  -> E
               
        |     ^
        \/    |
              |  
        C  ---|
''' 


# count the number of paths from starting node to ending node (backtracking)
# time is O(N^V) -> nodes the the power of verticies 
def dfs(node, target, adjList, visit): 
    if node in visit: 
        return 0
    if node == target: 
        return 1

    count = 0
    visit.add(node)
    for neighbor in adjList[node]: 
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)

    return count 

print(dfs("A", "E", adjList, set()))



# shortest path from a node to a target
# time complexity of O(V+E)
def bfs(startNode, target, adjList): 
    length = 0
    
    visit = set()
    visit.add(startNode)
    
    queue = deque()
    queue.append(startNode)

    while queue: 
        for _ in range(len(queue)): 
            curr = queue.popleft()
            if curr == target: 
                return length 
            
            for neighbor in adjList[curr]: 
                # only visity if we have not visited yet 
                if neighbor not in visit: 
                    visit.add(neighbor)
                    queue.append(neighbor)
        
        length += 1 
    return length 

print(bfs("A", "E", adjList))



