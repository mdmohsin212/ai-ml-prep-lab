class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_values = sorted(piles)
        n = len(piles) - 1
        ans = 0

        for i in range(len(piles) // 3):
            ans += sorted_values[n - (i * 2) - 1]
        
        return ans