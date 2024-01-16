import timeit
import perf 
import random
import matplotlib.pyplot as plt
import pandas as pd
###Split a matrix into four equal-sized submatrices.
def split_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    split_row, split_col = rows // 2, cols // 2

    # Split the matrix into four submatrices
    A11 = [row[:split_col] for row in matrix[:split_row]]
    A12 = [row[split_col:] for row in matrix[:split_row]]
    A21 = [row[:split_col] for row in matrix[split_row:]]
    A22 = [row[split_col:] for row in matrix[split_row:]]

    return A11, A12, A21, A22

### Add two matrices element-wise.
def add_matrices(matrix1, matrix2):
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]

###Subtract one matrix from another element-wise.
def subtract_matrices(matrix1, matrix2):

    return [
        [matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]

###Strassen's Matrix Multiplication algorithm.
def strassen(matrix1, matrix2):
 
    # Base case: if matrices are 1x1, perform standard multiplication
    if len(matrix1) == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]

    # Split matrices into submatrices
    A11, A12, A21, A22 = split_matrix(matrix1)
    B11, B12, B21, B22 = split_matrix(matrix2)

    # Calculate intermediate matrices
    P1 = strassen(A11, subtract_matrices(B12, B22))
    P2 = strassen(add_matrices(A11, A12), B22)
    P3 = strassen(add_matrices(A21, A22), B11)
    P4 = strassen(A22, subtract_matrices(B21, B11))
    P5 = strassen(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen(subtract_matrices(A11, A21), add_matrices(B11, B12))

    # Calculate result submatrices
    C11 = subtract_matrices(add_matrices(P5, P4), subtract_matrices(P2, P6))
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = subtract_matrices(subtract_matrices(P5, P3), subtract_matrices(P1, P7))

    # Combine result submatrices into the final result matrix
    result = [
        C11[i] + C12[i]
        for i in range(len(C11))
    ] + [
        C21[i] + C22[i]
        for i in range(len(C21))
    ]

    return result

def generate_random_matrix(rows, cols , seed = None):
    if seed is not None : 
        random.seed(Seed)
    else: 
        return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def benchmark(matrix_size, repetitions=5, warm_up_runs=3, seed=None):
    data = {'Matrix Size': [], 'Run Number': [], 'Individual Runtime': []}

    # Warm-up runs to stabilize the system and trigger optimizations
    for _ in range(warm_up_runs):
        matrix1 = generate_random_matrix(matrix_size, matrix_size, seed=seed)
        matrix2 = generate_random_matrix(matrix_size, matrix_size, seed=seed)
        strassen(matrix1, matrix2)  # Warm-up run

    # Actual benchmarking repetitions
    for run_number in range(1, repetitions + 1):
        matrix1 = generate_random_matrix(matrix_size, matrix_size, seed=seed)
        matrix2 = generate_random_matrix(matrix_size, matrix_size, seed=seed)

        # Repeat the measurement and calculate runtime
        start_time = timeit.default_timer()
        strassen(matrix1, matrix2)
        end_time = timeit.default_timer()

        runtime = end_time - start_time

        # Store data in the dictionary
        data['Matrix Size'].append(matrix_size)
        data['Run Number'].append(run_number)
        data['Individual Runtime'].append(runtime)

        print(f"Matrix size: {matrix_size}x{matrix_size}")
        print(f"Run {run_number} - Runtime: {runtime} seconds")
        print("The result is", strassen(matrix1, matrix2)[0][:min(matrix_size, 5)], "...")
        print()

    df = pd.DataFrame(data)
    average_runtimes = df.groupby('Matrix Size')['Individual Runtime'].mean().reset_index()
    print("\nAverage Runtimes:\n", average_runtimes)
    print()

    return df

# Collect benchmark data
matrix_sizes = [2, 4, 8, 16, 32, 64, 128]
repetitions = 5

all_data = pd.DataFrame()

for matrix_size in matrix_sizes:
    matrix_data = benchmark(matrix_size, repetitions=repetitions)
    all_data = pd.concat([all_data, matrix_data], ignore_index=True)

# Display the combined data table
print("\nCombined Data Table:\n", all_data)
