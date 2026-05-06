def fibonacci(n):
    fibo = [0, 1]
    while len(fibo) < n:
        fibo.append(fibo[-1] + fibo[-2])
    
    return fibo

n = 10
print(fibonacci(n))