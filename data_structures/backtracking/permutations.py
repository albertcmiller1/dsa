from typing import List
def permute(nums: List[int]) -> List[List[int]]:
    res = []

    if len(nums) == 1:
        return [nums[:]]

    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)

        res.extend(perms)
        nums.append(n)

    return res

if __name__ == "__main__":
    print(permute([1, 2, 3]))