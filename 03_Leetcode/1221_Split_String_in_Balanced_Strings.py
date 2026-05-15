class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        
        for char in s:
            if char == 'L':
                l += 1
            elif char == 'R':
                r += 1
            
            if l == r and (l != 0 and r != 0):
                ans += 1
                l = 0
                r = 0
        
        return ans