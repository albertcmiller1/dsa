nums = [1, 3, 4, 2]
stack = []
for num in nums:
    while stack and num<stack[-1]:
        print(f"cur number: {num} is smaller than top of stack. popping top of stack: {stack.pop()}")
    print(f"adding {num} to stack.")
    stack.append(num)
    print(f"cur stack: {stack}\n")