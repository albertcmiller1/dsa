'''
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix2 = []
for r in range(len(matrix)):
    col = []
    for c in range(len(matrix[0])):
        col.append(matrix[c][r])
    matrix2.append(col)
'''


matrix = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l']
]

matrix2 = []
for c in range(len(matrix[0])): # 0-3
    col = []
    for r in range(len(matrix)): # 0-2
        col.append(matrix[r][c])
    matrix2.append(col)


print(matrix2)
    
