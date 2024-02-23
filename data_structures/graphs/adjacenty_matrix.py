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


'''
[Time]
time complexity of DFS on a graph is usually O(n+e), where n is the number of nodes and 3 is the number of edges 
in the worst case scenario where every node is connected with every other node, e = n^2

> each node is visited only once 
> we iterate over a node's edges only when we are visiting that node 
> because we can only visit a node once, a node's edges are only iterated over once 
> therefore, all edges are iterated over only once, which costs O(e)

[Space]
when we build adj_list, we are storing all the edges in arrays. 
we will also need some space for the recursion call stack, O(n) in the worst case. 
space complexity is O(n+e)

'''

# recursive method to visit all neighbors 
def dfs(node):
    seen = set()
    for neighbor in graph[node]:
        # the next 2 lines are needed to prevent cycles
        if neighbor not in seen:
            seen.add(neighbor)
            dfs(neighbor)

# iterative method to visit all neighbors 
def dfs(start):
    seen = set()
    stack = [start]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)