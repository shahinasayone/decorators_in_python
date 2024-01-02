def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        print('ffff', func)
        print('99999999999999', func(*args, **kwargs))
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("John"))
