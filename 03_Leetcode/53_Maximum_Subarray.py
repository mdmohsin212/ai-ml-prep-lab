class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = global_max = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i], nums[i] + max_current)
            global_max = max(global_max, max_current)
        
        return global_max