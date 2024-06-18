
# ICT 09 – Programming 1

# FINAL PROJECT
# Matrix:
# 1. Transpose the given input of 3x4 matrix:

def transpose_matrix(matrix):
    transposed = []
    for col in range(len(matrix[0])):
        transposed_row = []
        for row in range(len(matrix)):
            transposed_row.append(matrix[row][col])
        transposed.append(transposed_row)
    return transposed

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transposed_matrix = transpose_matrix(matrix)
    for row in transposed_matrix:
        print(row)
