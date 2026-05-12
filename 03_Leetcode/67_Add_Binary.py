class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2) + int(b, 2)
        return bin(a)[2:]