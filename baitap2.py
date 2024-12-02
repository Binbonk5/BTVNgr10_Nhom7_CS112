import random
import time
from concurrent.futures import ThreadPoolExecutor

# Hàm nhân ma trận tuần tự
def matrix_multiply_sequential(A, B):
    rows_a, cols_a = len(A), len(A[0])
    rows_b, cols_b = len(B), len(B[0])
    C = [[0] * cols_b for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Hàm nhân ma trận song song
def matrix_multiply_parallel(A, B, num_threads=4):
    rows_a, cols_a = len(A), len(A[0])
    rows_b, cols_b = len(B), len(B[0])
    C = [[0] * cols_b for _ in range(rows_a)]

    def compute_row(row):
        for j in range(cols_b):
            for k in range(cols_a):
                C[row][j] += A[row][k] * B[k][j]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(compute_row, range(rows_a))
    
    return C

# Hàm sinh ma trận ngẫu nhiên
def generate_matrix(rows, cols, min_val=0, max_val=10):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Hàm đo thời gian và kiểm tra
def test_matrix_multiply():
    rows, cols = 400, 400
    A = generate_matrix(rows, cols)
    B = generate_matrix(cols, rows)
    
    print("Testing matrix multiplication with size 400x400")
    
    start = time.perf_counter()
    _ = matrix_multiply_sequential(A, B)
    sequential_time = time.perf_counter() - start
    print(f"Sequential Time: {sequential_time:.5f}s")
    
    start = time.perf_counter()
    _ = matrix_multiply_parallel(A, B)
    parallel_time = time.perf_counter() - start
    print(f"Parallel Time: {parallel_time:.5f}s")
    
    print("-" * 50)

# Test case
test_matrix_multiply()
