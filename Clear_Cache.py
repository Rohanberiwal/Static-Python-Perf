import time
import random
import pandas as pd
from statistics import mean, stdev
import os

def split_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    split_row, split_col = rows // 2, cols // 2

    A11 = [row[:split_col] for row in matrix[:split_row]]
    A12 = [row[split_col:] for row in matrix[:split_row]]
    A21 = [row[:split_col] for row in matrix[split_row:]]
    A22 = [row[split_col:] for row in matrix[split_row:]]

    return A11, A12, A21, A22

def add_matrices(matrix1, matrix2):
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]

def subtract_matrices(matrix1, matrix2):
    return [
        [matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]

def strassen(matrix1, matrix2):
    if len(matrix1) == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]

    A11, A12, A21, A22 = split_matrix(matrix1)
    B11, B12, B21, B22 = split_matrix(matrix2)

    P1 = strassen(A11, subtract_matrices(B12, B22))
    P2 = strassen(add_matrices(A11, A12), B22)
    P3 = strassen(add_matrices(A21, A22), B11)
    P4 = strassen(A22, subtract_matrices(B21, B11))
    P5 = strassen(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen(subtract_matrices(A11, A21), add_matrices(B11, B12))

    C11 = subtract_matrices(add_matrices(P5, P4), subtract_matrices(P2, P6))
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = subtract_matrices(subtract_matrices(P5, P3), subtract_matrices(P1, P7))

    result = [
        C11[i] + C12[i]
        for i in range(len(C11))
    ] + [
        C21[i] + C22[i]
        for i in range(len(C21))
    ]

    return result

def generate_random_matrix(rows, cols, seed=None):
    if seed is not None:
        random.seed(seed)
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def clear_cache():
    # Clear cache to ensure consistent benchmarking
    os.system('sync; echo 3 > /proc/sys/vm/drop_caches')

def pin_cpu():
    # Pin the process to the first CPU core
    os.system(f"taskset -p 0x1 {os.getpid()}")

def benchmark(matrix_size, repetitions=5, warm_up_runs=3, stress_runs=100, seed=None):
    data = {'Matrix Size': [], 'Run Number': [], 'Runtime (seconds)': []}

    # Pin CPU
    pin_cpu()

    # Warm-up phase
    for _ in range(warm_up_runs):
        matrix1 = generate_random_matrix(matrix_size, matrix_size, seed=seed)
        matrix2 = generate_random_matrix(matrix_size, matrix_size, seed=seed)
        strassen(matrix1, matrix2)

    # Actual benchmarking
    for run_number in range(1, repetitions + 1):
        matrix1 = generate_random_matrix(matrix_size, matrix_size, seed=seed)
        matrix2 = generate_random_matrix(matrix_size, matrix_size, seed=seed)

        clear_cache()  # Clear cache before each run

        start_time = time.perf_counter()
        strassen(matrix1, matrix2)
        end_time = time.perf_counter()

        runtime = end_time - start_time

        data['Matrix Size'].append(matrix_size)
        data['Run Number'].append(run_number)
        data['Runtime (seconds)'].append(runtime)

    df = pd.DataFrame(data)
    average_runtimes = df.groupby('Matrix Size')['Runtime (seconds)'].agg([mean, stdev]).reset_index()
    print("\nAverage Runtimes:\n", average_runtimes)

    # Stress testing
    stress_data = []
    for _ in range(stress_runs):
        matrix1 = generate_random_matrix(matrix_size, matrix_size, seed=seed)
        matrix2 = generate_random_matrix(matrix_size, matrix_size, seed=seed)

        clear_cache()  # Clear cache before each stress run

        start_time = time.perf_counter()
        strassen(matrix1, matrix2)
        end_time = time.perf_counter()

        runtime = end_time - start_time
        stress_data.append(runtime)

    print(f"\nStress Testing for Matrix Size {matrix_size}x{matrix_size}:")
    print(f"Mean Runtime: {mean(stress_data)} seconds")
    print(f"Standard Deviation: {stdev(stress_data)} seconds")

    return df

matrix_sizes = [2, 4, 8, 16, 32, 64, 128]
repetitions = 5
stress_runs = 100

all_data = pd.DataFrame()

for matrix_size in matrix_sizes:
    matrix_data = benchmark(matrix_size, repetitions=repetitions, stress_runs=stress_runs)
    all_data = pd.concat([all_data, matrix_data], ignore_index=True)
print("\nCombined Data Table:\n", all_data)
