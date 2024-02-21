from collections import defaultdict
'''
less common

you will be given a 2D matrix of size nxn
if adj_matrix[i][j] == 1, that means there is an outgoing edge from i to j

           [2]
            ^
        /   |   \
       <         >
    [0]  -> [1]   [3]  
'''

adj_matrix = [
    [0,1,0,0],
    [0,0,1,0],
    [1,0,0,1],
    [0,0,0,0]
]

'''
adj_matrix[0][1] == 1   ->   node 0 has an edge to node 1
adj_matrix[1][2] == 1   ->   node 1 has an edge to node 2
adj_matrix[2][0] == 1   ->   node 2 has an edge to node 0
adj_matrix[2][3] == 1   ->   node 2 has an edge to node 3

time complexity will be O(n^2)

example problem: https://leetcode.com/problems/number-of-provinces/description/
'''

# build the graph
n = len(adj_matrix)
graph = defaultdict(list)
for i in range(n): 
    for j in range(n):
        if adj_matrix[i][j]:
            graph[i].append(j)

print(graph)