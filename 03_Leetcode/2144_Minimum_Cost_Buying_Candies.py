class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0
        i = len(cost) - 1
        cost.sort()

        while i >= 0:
            ans += cost[i]
            if i - 1 >= 0:
                ans += cost[i - 1]
            i -= 3

        return ans