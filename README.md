# Strassen's Matrix Multiplication Benchmarking

This repository contains Python code for benchmarking Strassen's Matrix Multiplication algorithm across different matrix sizes. The code leverages advanced features such as warm-up phases, multi-independent runs, stress testing, CPU pinning, cache clearing, and high-resolution timing. It uses Pandas for data organization and Matplotlib for visualization.

## Strassen's Matrix Multiplication Algorithm

### Overview

Strassen's Matrix Multiplication algorithm is an efficient algorithm for multiplying two matrices using a divide-and-conquer approach. Introduced by Volker Strassen in 1969, it reduces the number of multiplications required compared to the standard method.

### Key Concepts

- **Divide and Conquer:** Divides each matrix into four submatrices, recursively multiplies these submatrices, and combines the results.
- **Matrix Splitting:** Splits matrices A and B into four submatrices: A11, A12, A21, A22, and B11, B12, B21, B22.
- **Intermediate Matrix Calculations:** Computes seven recursive multiplications (P1 to P7) using the submatrices.
- **Combining Results:** Combines the intermediate results to obtain the final product matrices.

### Advantages

- **Reduced Multiplications:** Reduces the number of multiplications from 8 to 7 compared to the standard algorithm.
- **Complexity:** Exhibits lower asymptotic complexity, making it useful for large matrix sizes.

### Limitations

- **Addition Overhead:** Introduces additional additions, which may impact performance for smaller matrices.
- **Practical Considerations:** For small matrices, the standard algorithm might outperform Strassen's due to constant factors.

## Usage in Benchmarking

The provided code benchmarks Strassen's Matrix Multiplication algorithm across various matrix sizes, analyzing its scalability and efficiency. The benchmarking process includes:

- **Warm-Up Phase:** Ensures system stability before actual benchmarking.
- **Multi-Independent Runs:** Executes multiple independent runs for each matrix size to ensure result reliability.
- **Stress Testing:** Evaluates performance under heavy load conditions.
- **CPU Pinning:** Pins the process to a specific CPU core for consistent performance measurements.
- **Cache Clearing:** Clears system caches before each run to reduce variability.
- **High-Resolution Timing:** Measures runtime with high precision.

## Code Structure

### Matrix Manipulation Functions

1. **`split_matrix(matrix)`**
   - Splits a matrix into four equal-sized submatrices (A11, A12, A21, A22).

2. **`add_matrices(matrix1, matrix2)`**
   - Adds two matrices element-wise.

3. **`subtract_matrices(matrix1, matrix2)`**
   - Subtracts one matrix from another element-wise.

### Strassen's Matrix Multiplication Algorithm

4. **`strassen(matrix1, matrix2)`**
   - Implements Strassen's Matrix Multiplication algorithm using recursion.

### Random Matrix Generation

5. **`generate_random_matrix(rows, cols, seed=None)`**
   - Generates a random matrix with given dimensions, optionally accepting a seed for reproducibility.

### Benchmarking

6. **`benchmark(matrix_size, repetitions=5, warm_up_runs=3, stress_runs=100, seed=None)`**
   - Measures individual runtimes of Strassen's algorithm for a specified matrix size.
   - Performs a warm-up phase, calculates average runtimes, and stores data.
   - Conducts stress testing with multiple runs to assess performance under load.
   - Incorporates CPU pinning and cache clearing to ensure consistent results.

### Main Benchmarking Loop

7. **`matrix_sizes = [2, 4, 8, 16, 32, 64, 128]`**
   - List of matrix sizes to be benchmarked.

8. **`repetitions = 5`**
   - Number of repetitions for each matrix size.

9. **`all_data = pd.DataFrame()`**
   - Initializes an empty DataFrame to store benchmarking results.

10. **Loop through each matrix size:**
    - Calls `benchmark` function for each matrix size.
    - Concatenates individual data frames into `all_data`.

### Display Results

11. **`print("\nCombined Data Table:\n", all_data)`**
    - Displays the combined data table containing matrix size, run number, and individual runtime for each run.
    - Prints average runtimes and performance metrics.

## Observations

**Observation 1: Algorithm Efficiency**

The benchmark results show that Strassen's Matrix Multiplication algorithm performs efficiently for smaller matrix sizes. As matrix size increases, the algorithm maintains a reasonable runtime, demonstrating its scalability.

**Observation 2: Logarithmic Trend in Runtimes**

The runtime vs. matrix size graph displays a logarithmic trend, particularly visible with a logarithmic scale on the y-axis. This indicates that Strassen's algorithm scales better than traditional matrix multiplication methods for larger matrices.

## References

1. Strassen, V. (1969). Gaussian elimination is not optimal. Numerische Mathematik, 13(4), 354-356.
2. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms (3rd ed.). The MIT Press.

## Benchmarking Results

Result 1 : Repetation cycle = 10 , Maximum size of Matrix = 128*128 , Output Graph attached below : 
![10repetartion@timeit_Graph](https://github.com/Rohanberiwal/Static-Python-Perf/assets/119040957/be2cc091-c877-4efd-b6f0-5fb37fe33c7b)


Result 2 : Repetation Cycle = 1  , Maximun size of Matrix = 128*128 , Ouptut Grpah attached below 

![Strassen_Bencmark_Output _@time](https://github.com/Rohanberiwal/Static-Python-Perf/assets/119040957/1b0f4428-c690-4827-a01a-8eb4e86b44af)

Result 3 :  Repetation Cycle = 10 , Maximum Size of Matrix  = 256*256 

No output 
Reason : High Computation power needed for 256*256 matrix multiplication .


Result 4 :  Repetation Cycle = 1 , Maximum Size of Matrix  = 256*256 

No output 
Reason : High Computation power needed for 256*256 matrix multiplication .

## Usage

To run the benchmark, modify the `matrix_sizes` list and adjust the benchmarking parameters as needed. Execute the script and observe the printed results and the generated combined data table.

## License

This code is provided under the [MIT License](LICENSE).
