n = int(input())

def fibonacci(n):
    seq = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return seq
    
    for i in range(2, n):
        ans = seq[i - 1] + seq[i - 2]
        seq.append(ans)
        
    yield seq


fibo = fibonacci(n)

for i in fibonacci:
    print(i)