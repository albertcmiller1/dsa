'''
target = 0
[-1, 2, 1, -4]
[-4, -1, 1, 2]
[-50, -5, 0, 50]
    A    B     C 

'''

#         0    1  2  3 
nums =  [-50, -5, 0, 50]
target = 0
diff = float("inf")

for Ai, A in enumerate(nums): 
    Bi, Ci = Ai+1, len(nums)-1
    while Bi<Ci: 
        curr_sum = A + nums[Bi] + nums[Ci]
        print(Ai, Bi, Ci, curr_sum)
        if abs(target-curr_sum) < abs(diff): 
            diff = target-curr_sum
            print(f"diff update to {diff}")
        elif curr_sum < target: 
            Bi+=1
        else: 
            Ci-=1



print(target-diff)
