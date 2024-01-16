#Static Python Perf - Measuring the Cost of Sound Gradual Types
# Strassen's Matrix Multiplication Benchmarking

This repository contains Python code for benchmarking Strassen's Matrix Multiplication algorithm across different matrix sizes. The code uses Pandas for data organization and Matplotlib for visualization.

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

6. **`benchmark(matrix_size, repetitions=5, warm_up_runs=3, seed=None)`**
   - Measures individual runtimes of Strassen's algorithm for a specified matrix size.
   - Performs warm-up runs for system stabilization.
   - Calculates average runtimes over multiple repetitions.
   - Stores benchmarking data in a Pandas DataFrame.

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
    - Also prints average runtimes for each matrix size.

## Observations

**Observation 1: Algorithm Efficiency**

Upon analyzing the benchmark results, we observe that Strassen's Matrix Multiplication algorithm demonstrates efficient performance for smaller matrix sizes. As the matrix size increases, the algorithm maintains a reasonable runtime, showcasing its scalability.

**Observation 2: Logarithmic Trend in Runtimes**

The runtime vs. matrix size graph indicates a logarithmic trend, particularly visible when using a logarithmic scale on the y-axis. This suggests that the algorithm's complexity scales better than traditional matrix multiplication methods for larger matrices.

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
