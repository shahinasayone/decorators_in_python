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
def time_consuming_operation():
    # Simulate a time-consuming operation
    time.sleep(3)
    print("Operation completed!")

time_consuming_operation()
