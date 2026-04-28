# Naive solution -> O(N^2)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            cnt = 0
            for i in nums:
                if i != num and i < num:
                    cnt += 1
            ans.append(cnt)
        
        return ans