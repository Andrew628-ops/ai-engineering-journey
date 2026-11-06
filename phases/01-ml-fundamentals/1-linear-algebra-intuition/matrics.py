def dot_product(a, b):
    total = 0
    for x, y in zip(a, b):
        total = total + x * y
    return total

def matrix_vector_multiply(matrix, vector):
    results = []
    for row in matrix:
        if len(row) != len(vector):
            raise ValueError("length must be thesame")
        result = dot_product(row, vector)
        results.append(result)
    return results


matrix = [
    [3, 0],
    [0, 2]
]

vector = [1, 4]
print(matrix_vector_multiply(matrix, vector))


def get_column(B, column_index):
    column = []
    for b in B:
        result = b[column_index]
        column.append(result)
    return column


def matrix_multiply(A, B):
    results = []
    if len(A[0]) != len(B):
        raise ValueError("have incompatible")
    for row in A:
        result_row = []
        for col in range(len(B[0])):
            res = get_column(B, col)
            result_row.append(dot_product(row, res))
        results.append(result_row)
    return results