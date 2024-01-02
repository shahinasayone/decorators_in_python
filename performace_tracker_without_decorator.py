import time

def time_consuming_operation():
    start_time = time.time()

    # Simulate a time-consuming operation
    time.sleep(3)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"The operation took {execution_time:.6f} seconds to execute.")
    print("Operation completed!")

# Calling the function
time_consuming_operation()
