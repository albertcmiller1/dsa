def fibonacci(n):
    arr = [0] * (n + 1)
    # base case - the second Fibonacci number is 1
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    return arr[n]

'''
Bottom-Up
start at the base case and work our way up 
aka Tabulation 

'''