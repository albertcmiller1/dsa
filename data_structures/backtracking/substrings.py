def find_substrings(s):

    substrings = []
    def backtrack(start, end):
        print(start, end)
        # If the end index has reached the length of the string, backtrack
        if end == len(s):
            return
        
        # If the start index is less than or equal to the end index, add the substring
        if start <= end:
            substrings.append(s[start:end+1])
        
        # Recur by increasing the end index
        backtrack(start, end + 1)
        
        # Recur by increasing the start index (reset end index)
        if end == len(s) - 1:
            backtrack(start + 1, start + 1)

    backtrack(0, 0)
    return substrings

all_substrings = find_substrings("abc")
print(all_substrings)
