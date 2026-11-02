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