class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
            ans = []
            for num in nums:
                k = 0
                temp = num
                while temp & 1:
                    k += 1
                    temp >>= 1
                
                if k == 0:
                    ans.append(-1)
                    continue
                
                if num == (1 << num.bit_length()) - 1:
                    ans.append(num >> 1)
                
                else:
                    val = num - (1 << k) + (1 << (k - 1))
                    ans.append(val)

            
            return ans