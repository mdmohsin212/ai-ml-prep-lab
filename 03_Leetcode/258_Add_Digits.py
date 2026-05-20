class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            ans = 0
            while num > 0:
                tmp = num % 10
                ans += tmp
                num = num // 10
            
            num = ans

        return num