class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        is_odd = False
        ans = 0
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for count in char_count:
            if char_count[count] % 2 == 0:
                ans += char_count[count]
            else:
                ans += (char_count[count] - 1)
                is_odd = True
        
        return ans + 1 if is_odd is True else ans