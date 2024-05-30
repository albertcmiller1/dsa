def missingNumber(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        print(f'''
        idx: {i}
        num: {num}
        mis: {missing}
        xor: {missing ^ i ^ num}
        ''')
        missing = missing ^ i ^ num
    return missing


print(missingNumber([1,3,0]))