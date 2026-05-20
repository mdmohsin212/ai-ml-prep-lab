class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        ans = []
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                ans.append(nums2[i])

        return ans