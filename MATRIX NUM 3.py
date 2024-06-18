
# ICT 09 – Programming 1

# FINAL PROJECT
# Matrix:
# 3. Find the sum of diagonal elements in a given matrix the manual way or NOT numpy way:

def sum_of_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result = sum_of_diagonal(matrix)
    print("The sum of diagonal elements:", result)
