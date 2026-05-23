class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            tmp = []
            
            for subset in ans:
                new_subset = subset + [num]
                tmp.append(new_subset)
                
            ans += tmp

        return ans