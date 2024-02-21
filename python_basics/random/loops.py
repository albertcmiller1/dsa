matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

N = len(matrix)
for i in range(N):
    for j in range(N): 
        print(matrix[i][j])

print("\n\n")

for i in range(N):
    for j in range(i, N): 
        print(matrix[i][j])