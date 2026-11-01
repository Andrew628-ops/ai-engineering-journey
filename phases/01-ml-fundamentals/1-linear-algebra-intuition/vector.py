# a = [3, 2]
# b = [1, -1]

# result = [
#     a[0] + b[0],
#     a[1] + b[1]
# ]

# print(result)

a2 = [2, -1]
result2 = [
    3 * a2[0],
    3 * a2[1]
]
print(result2)

# a = [2, 3]
# b = [4, 1]
# result = a[0] * b[0] + a[1] * b[1]

# print(result)

a = [2, 3, 1]
b = [4, 1, 5]

for x, y in zip(a, b):
    print(x, y)


total = 0

for x, y in zip(a, b):
    total = total + x * y

print(total)

def dot(a, b):
    total = 0
    for x, y in zip(a, b):
        total = total + x * y
    return total

print(dot([2, 3, 1], [4, 1, 5]))


def magnitude(v):
    squared_length = dot(v, v)
    return squared_length ** 0.5

print(magnitude([3, 4]))
print(magnitude([6, 8]))

# normalize 
def normalize(v):
    length = magnitude(v)
    result = []
    for coordinate in v:
        result.append(coordinate / length)
    return result

matrix = [
    [2, 0],
    [0, 3],
]
v = [3, 4]

result = []
for row in matrix:
    result.append(dot(row, v))

def matrix_vector(matrix, v):
    result = []
    for row in matrix:
        result.append(dot(row, v))
    return result


def project_vertical(v):
    return [0, v[1]]

print(project_vertical([2, 5]))

def project_horizontal(v):
    return [v[0], 0]

print(project_horizontal([3, 7]))

v = [3, 7]
projection = project_horizontal(v)

residual = [
    v[0] - projection[0],
    v[1] - projection[1]
]
print(residual)

print(dot(projection, residual))

def subtract(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x - y)
    return result

print(subtract([5, 8], [2, 3]))

v = [4, 6]
projection = project_horizontal(v)

residual = subtract(v[0] - projection[0], v[1] - projection[1])

print(projection)
print(residual)