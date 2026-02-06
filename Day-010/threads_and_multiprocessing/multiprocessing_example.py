## Multiprocessing is useful for CPU-bound tasks, as it allows you to take advantage of multiple CPU cores

import multiprocessing
import math
import sys
import time


sys.set_int_max_str_digits(1000000)


def compute_factorial(number):
    print(f"Computing factorial of {number}...")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result


if __name__ == "__main__":
    numbers = [100, 200, 300, 400]

    start_time = time.time()

    with multiprocessing.Pool() as pool:  # Create a pool of worker processes by default it will use the number of CPU cores available eg for 4 cores CPU it will create 4 worker processes
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
