# https://www.programiz.com/python-programming/methods/list/copy

# mixed list
prime_numbers = [2, 3, 5]
print(id(prime_numbers))
# copying a list
numbers = prime_numbers.copy()
print(id(numbers))

print('Copied List:', numbers)

# Output: Copied List: [2, 3, 5]

# he copy() method returns a shallow copy of the list.