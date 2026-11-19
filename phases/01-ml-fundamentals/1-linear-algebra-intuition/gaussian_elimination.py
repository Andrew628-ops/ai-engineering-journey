matrix = [
    [2, 4],
    [6, 8],
    [4, 10]
]


pivot_row  = 1
pivot_col = 1
for pivot_index in range(0, min(len(matrix), len(matrix[0]))):
    for candidate_row in range(pivot_index + 1, len(matrix)):
        if matrix[candidate_row][pivot_index] != 0:
            matrix[pivot_index], matrix[candidate_row] = (
            matrix[candidate_row], matrix[pivot_index]
            )
            break
        for row in range(pivot_index + 1, len(matrix)):
            factor = matrix[row][pivot_col] / matrix[pivot_row][pivot_col]
            for col in range(0, len(matrix[row])):
                matrix[row][col] = matrix[row][col] - factor * matrix[pivot_row][col]