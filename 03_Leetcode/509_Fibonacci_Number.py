class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a = [0, 1]
        while len(a) < n:
            a.append(a[-1] + a[-2])
        
        return (a[-1] + a[-2])