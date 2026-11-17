matrix = [
    [2, 4],
    [6, 8],
    [4, 10]
]


for pivot_index in range(0, min(len(matrix), len(matrix[0]))):
    for row in range(pivot_index + 1, len(matrix)):
        factor = matrix[row][pivot_index] / matrix[pivot_index][pivot_index]
        for col in range(0, len(matrix[row])):
            matrix[row][col] = matrix[row][col] - factor * matrix[pivot_index][col]