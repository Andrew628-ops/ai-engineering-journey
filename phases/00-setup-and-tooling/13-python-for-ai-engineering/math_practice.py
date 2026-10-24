import math
import statistics

import numpy as np

print("Library mean:", statistics.fmean([2, 4, 6]))
print("Library dot:", math.sumprod([1, 2, 3], [4, 5, 6]))

data = np.array([[1.0, 10.0], [3.0, 30.0]])
column_means = data.mean(axis=0)
centered = data - column_means

print("Column means:", column_means)
print("Centered:", centered)

def mean(values):
    return sum(values) / len(values)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b, strict=True))


print(mean([2, 4, 6]))
print(dot([1, 2, 3], [4, 5, 6]))