class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        reversed_words = [w[::-1] for w in words]

        result = " ".join(reversed_words)

        return result