def greet(name):
    return f"Hello, {name}!".upper()

# Without using a decorator, directly applying uppercase conversion
result = greet("John")
print(result)
