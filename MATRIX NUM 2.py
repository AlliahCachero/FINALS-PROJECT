
# ICT 09 – Programming 1

# FINAL PROJECT
# Matrix:
# 2. Find the sum of rows and columns of elements using numpy as follows:

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row_sums = np.sum(matrix, axis=1)

column_sums = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)
print("The sum of rows:", row_sums)
print("The sum of columns:", column_sums)
