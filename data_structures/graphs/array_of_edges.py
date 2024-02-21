edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adjList = {} # node, neighbors 
for src, dst in edges: 
    if src not in adjList: 
        adjList[src] = []
    if dst not in adjList: 
        adjList[dst] = []
    adjList[src].append(dst)

print(adjList)

from collections import defaultdict
edges_1 = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adjList_1 = defaultdict(list) # node, neighbors 
for src, dst in edges_1: 
    adjList_1[src].append(dst)

print(adjList_1)