class Solution:
    def romanToInt(self, s: str) -> int:
        data = {
            "I" : 1, "V" : 5,"X" : 10, "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        ans = 0
        n = len(s)
        
        for i in range(n):
            value = data[s[i]]
            if i < n - 1 and value < data[s[i + 1]]:
                ans -= value
            else:
                ans += value
                
        return ans