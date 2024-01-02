import time

def performance_tracker(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper

@performance_tracker
def add_numbers(a, b):
    result = a + b
    return result

@performance_tracker
def subtract_numbers(a, b):
    result = a - b
    return result

@performance_tracker
def multiply_numbers(a, b):
    result = a * b
    return result

@performance_tracker
def divide_numbers(a, b):
    result = a / b
    return result

# Calling the decorated functions
result_add = add_numbers(5, 7)
result_subtract = subtract_numbers(10, 3)
result_multiply = multiply_numbers(4, 6)
result_divide = divide_numbers(8, 2)

# Printing the results
print(f"The sum is: {result_add}")
print(f"The difference is: {result_subtract}")
print(f"The product is: {result_multiply}")
print(f"The quotient is: {result_divide}")
