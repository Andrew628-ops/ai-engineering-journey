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