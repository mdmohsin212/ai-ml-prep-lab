from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s, s1 = Counter(ransomNote), Counter(magazine)

        return True if (s & s1) == s else False 