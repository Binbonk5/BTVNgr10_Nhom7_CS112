import math
import time
from concurrent.futures import ThreadPoolExecutor

# Hàm kiểm tra số nguyên tố tuần tự
def is_prime_sequential(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Hàm kiểm tra số nguyên tố song song
def is_prime_parallel(n, num_threads=4):
    if n < 2:
        return False
    
    def check_range(start, end):
        for i in range(start, end):
            if n % i == 0:
                return False
        return True

    sqrt_n = int(math.sqrt(n)) + 1
    step = (sqrt_n - 2) // num_threads + 1
    ranges = [(2 + i * step, min(2 + (i + 1) * step, sqrt_n)) for i in range(num_threads)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(lambda r: check_range(*r), ranges)
    
    return all(results)

# Hàm đo thời gian và kiểm tra
def test_prime_check(x):
    print(f"Testing X = {x}")
    
    start = time.perf_counter()
    sequential_result = is_prime_sequential(x)
    sequential_time = time.perf_counter() - start
    print(f"Sequential: Result = {sequential_result}, Time = {sequential_time:.5f}s")
    
    start = time.perf_counter()
    parallel_result = is_prime_parallel(x)
    parallel_time = time.perf_counter() - start
    print(f"Parallel: Result = {parallel_result}, Time = {parallel_time:.5f}s")
    
    print("-" * 50)

# Test case
test_cases = [1000000000000091, 10000000000000099, 100000000000000049]
for x in test_cases:
    test_prime_check(x)
