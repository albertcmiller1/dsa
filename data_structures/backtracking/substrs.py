def partition(s):

    def dfs(s, path):
        if not s:
            result.append(path)
            return

        for i in range(1, len(s) + 1):
            dfs(s[i:], path + [s[:i]])


    result = []
    dfs(s, [])
    return result


print(partition("abc"))


'''

['a', 'b', 'c'], 
['a', 'bc'], 
['ab', 'c'], 
['abc']









a
a
ab 
abc
b
c
bc
c



'''