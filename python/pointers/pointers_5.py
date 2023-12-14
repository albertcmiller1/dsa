i = [1, 2, 3]   # create new array with assigned values 
j = i           # assign new variable j to reference of i, same place in memory 
i[0] = 5        # update first index, which will update both. 

print("i: ", i)
print("j: ", j)