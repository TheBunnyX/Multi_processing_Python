import multiprocessing
import time
import random
import math

# Function to perform a complex calculation (e.g., calculate (x^2 + sqrt(x)) / sin(x))
def calculate(x):
    # Example of a complex calculation, avoiding division by zero in sin(x)
    if x == 0:  # To avoid division by zero in sin(x)
        return 0
    return (x ** 2 + math.sqrt(x)) / math.sin(x)

# Main function to perform the computation using multiprocessing
def parallel_computation(array):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(calculate, array)
    return result

# Function to perform the computation sequentially
def sequential_computation(array):
    return [calculate(x) for x in array]

if __name__ == "__main__":
    # Set seed for random number generation
    random.seed(42)

    # Create two arrays of size 10,000,000 with random values between 1 and 100
    array1 = [random.randint(1, 100) for _ in range(10000000)]  # Array with random values between 1 and 100
    array2 = [random.randint(1, 100) for _ in range(10000000)]  # Array with random values between 1 and 100

    # Start measuring time for parallel computation
    start_time = time.perf_counter()  # Use perf_counter() for high precision timing
    # Perform parallel computation
    result1_parallel = parallel_computation(array1)
    result2_parallel = parallel_computation(array2)
    parallel_time = time.perf_counter() - start_time  # Calculate elapsed time

    # Start measuring time for sequential computation
    start_time = time.perf_counter()  # Start new timing
    # Perform sequential computation
    result1_sequential = sequential_computation(array1)
    result2_sequential = sequential_computation(array2)
    sequential_time = time.perf_counter() - start_time  # Calculate elapsed time

    # Display the results using f-string formatting to avoid scientific notation
    print(f"Time taken for parallel computation: {parallel_time:.6f}")  # Display time with 6 decimal places
    print(f"Time taken for sequential computation: {sequential_time:.6f}")  # Display time with 6 decimal places
