def exception_handle(n, m):
    try:
        return n / m
    
    except ZeroDivisionError:
        return "Zero devision error"
        

result = exception_handle(10, 0)
print(result)