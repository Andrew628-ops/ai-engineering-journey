def dot(a, b):
    total = 0
    for x, y in zip(a, b):
        total = total + x * y
    return total

def project(v, d):
    denominator = dot(d, d)
    if denominator == 0:
        raise ValueError("Direction must be nonzero")
    t = dot(v, d) / denominator
    # return [t, 2*t]
    return [t * d[0], t * d[1]]

print(project([2, 6], [1, 2]))
print(project([2, 6], [1, 0]))
print(project([2, 6], [0, 1]))
print(project([2, 6], [2, 4]))
print(project([2, 6], [0, 0]))