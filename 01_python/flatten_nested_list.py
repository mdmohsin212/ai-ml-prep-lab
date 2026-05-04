def flatten(nums):
    result = []
    for i in nums:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


nested_list = [1, [2, 3, [[4], 5]], 6]
print(flatten(nested_list))