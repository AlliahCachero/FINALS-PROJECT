
# ICT 09 – Programming 1

# FINAL PROJECT
# Matrix:
# 2. Find the sum of rows and columns of elements using numpy as follows:

import numpy as np

# Define the matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Sum of rows
row_sums = np.sum(matrix, axis=1)

# Sum of columns
column_sums = np.sum(matrix, axis=0)

# Display the results
print("Matrix:")
print(matrix)
print("The sum of rows:", row_sums)
print("The sum of columns:", column_sums)
