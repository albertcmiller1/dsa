def bruteforce(n): 
    if n <= 1: 
        return n
    return bruteforce(n-1) + bruteforce(n-2)
'''
O(2^n) because every call to bruteforce creates 2 more calls to bruteforce
'''

print(bruteforce(5)) # 1 1 2 3 5 
'''
                    5
            4               3
        3       2       2       1
      2   1   1   0   1  0    0
    1  0  
'''

# aka top down dynamic programming
def memoization(n, cache): 
    if n<=1: 
        return n
    if n in cache: 
        return cache[n]
    
    cache[n] = memoization(n-1, cache) + memoization(n-2, cache)
    return cache[n]

print(memoization(5, {}))


# bottom up dynamic programming
def dp(n):
    if n<2: 
        return n

    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp 
        i += 1

    return dp[1]

print(dp(5))

