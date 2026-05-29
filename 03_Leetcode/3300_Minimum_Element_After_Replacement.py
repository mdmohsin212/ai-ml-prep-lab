class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = []
        for n in nums:
            tmp = 0
            while(n != 0):
                x = (n % 10)
                tmp += x
                n = n // 10
            ans.append(tmp)
        
        return min(ans)