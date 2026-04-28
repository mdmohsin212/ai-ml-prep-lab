class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            val = num
            cnt = 0
            for i in nums:
                if i != val and i < val:
                    cnt += 1
            ans.append(cnt)
        
        return ans