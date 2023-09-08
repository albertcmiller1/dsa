i = 5   # create new place in memory for i as an integer with value 5
j = i   # assign j to a reference of i, same place in memeroy 
j = 3   # when we update j, a new place in memeory will be created for j, no longer binding to i

print("i: ", i) # 5
print("j: ", j) # 3