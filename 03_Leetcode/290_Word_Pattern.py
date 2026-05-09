class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        hashmap = {}
        
        for char, word in zip(pattern, words):
            if char in hashmap:
                if hashmap[char] != word:
                    return False
            else:
                if word in hashmap.values():
                    return False
                hashmap[char] = word
                
        return True