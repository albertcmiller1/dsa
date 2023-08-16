'''
[2, 1, 2, 0, 0, 2]

loop over each element, and count each element 
{
    0: 2
    1: 1
    2: 3, 
}
or could use an array 
 
 0  1  2
[2, 1, 3]


'''


arr = [2, 1, 2, 0, 0, 2]
counts = [0, 0, 0]

for n in arr:
    counts[n] += 1

print(counts)