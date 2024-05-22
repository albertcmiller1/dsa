def all_substrings_recursive(s):
    def helper(start, current, result):
        if start == len(s):
            return
        if current != "":
            result.append(current)
        for i in range(start, len(s)):
            helper(i + 1, current + s[i], result)

    result = []
    helper(0, "", result)
    return result

# Example usage
input_string = "abc"
all_substrings_of_string = all_substrings_recursive(input_string)
print(all_substrings_of_string)
