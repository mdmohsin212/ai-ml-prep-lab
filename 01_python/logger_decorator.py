def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print("-" * 30)
        print(f"--- [LOG]: '{func.__name__}' start of function")
    
        result = func(*args, **kwargs)
        
        print(f"--- [LOG]: '{func.__name__}' end of function")
        print("-" * 30)
        return result
    
    return wrapper


@logger_decorator
def hi_fun():
    print("Hi")


hi_fun()