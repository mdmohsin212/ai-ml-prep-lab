class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []

        for num in nums:
            if num < pivot:
                ans.append(num)

        [ans.append(pivot) for _ in range(nums.count(pivot))]        

        for num in nums:
            if num > pivot:
                ans.append(num)
                
        return ans