class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique_num = set(nums)
        ans = []

        for i in range(1, len(nums) + 1):
            if i not in unique_num:
                ans.append(i)
        
        return ans