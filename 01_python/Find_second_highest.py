def second_high(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]

numbers = [1, 3, 2, 4, 4, 5, 6, 6]
print(second_high(numbers))