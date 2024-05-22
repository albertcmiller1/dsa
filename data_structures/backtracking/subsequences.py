def all_subsequences(s):
    def subsequences_recursive(s, current, index, result):
        if index == len(s):
            result.append(current)
            return
        # Include the current character
        subsequences_recursive(s, current + s[index], index + 1, result)
        # Exclude the current character
        subsequences_recursive(s, current, index + 1, result)

    result = []
    subsequences_recursive(s, "", 0, result)
    return result

# Example usage
input_string = "abc"
all_subsequences_of_string = all_subsequences(input_string)
print(all_subsequences_of_string)
