class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        n = abs(num)
        if n == 0:
            return "0"

        while(n != 0):
            tmp = (n % 7)
            ans += str(tmp)
            n = n // 7

        return ("-" + "".join(reversed(ans)) if num < 0 else "".join(reversed(ans)))