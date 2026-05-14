class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0

        while (i < len(haystack) and j < len(needle)):
            if haystack[i] == needle[j]:
                j += 1
            else:
                i = i - j
                j = 0
            i += 1
            
        if j == len(needle):
            return i - j
        
        return -1