# Linear Algebra Intuition — My Notes

Updated: 2026-11-02
Status: **In progress; final lesson quiz not taken.**

These notes cover our interactive practice so far. Code and outputs were discussed or learner-reported; this notes update does not verify the local scripts.

## Vectors and coordinates

A vector is an ordered list of numbers. For a 2D movement vector:

- `v[0]` is horizontal movement: positive means right, negative means left.
- `v[1]` is vertical movement: positive means up, negative means down.

For example, `[2, -1]` means 2 steps right and 1 step down. Coordinates can also describe features, such as house area and number of rooms; their order gives them meaning.

Add matching coordinates:

```python
a = [3, 2]
b = [1, -1]
result = [a[0] + b[0], a[1] + b[1]]
# [4, 1]
```

Scaling multiplies every coordinate by the same number:

```python
v = [2, -1]
result = [3 * v[0], 3 * v[1]]
# [6, -3]
```

Python list multiplication is different: `3 * [2, -1]` repeats the list instead of scaling its coordinates.

## Dot product: multiply matching coordinates, then add

The dot product returns **one number**, not a list.

```python
def dot(a, b):
    total = 0
    for x, y in zip(a, b):
        total = total + x * y
    return total
```

For `[2, 3, 1]` and `[4, 1, 5]`:

| Pass | Pair | Product | Running total |
|------|------|---------|---------------|
| 1 | 2, 4 | 8 | 8 |
| 2 | 3, 1 | 3 | 11 |
| 3 | 1, 5 | 5 | 16 |

`a` and `b` are whole lists. Inside the loop, `x` and `y` are the current numbers, so multiply `x * y`, not `a * b`.

For nonzero vectors:

- Positive dot product: angle less than 90°.
- Zero dot product: perpendicular directions.
- Negative dot product: angle greater than 90°.

Examples: `dot([1, 0], [0, 1]) = 0`, and `dot([1, 0], [-1, 0]) = -1`.

The dot product depends on length as well as direction. It can calculate a model score by multiplying input features by their weights and adding the contributions.

## Magnitude: vector length

For `[3, 4]`:

```text
Squared length = 3² + 4² = 25
Length = √25 = 5
```

Squaring and taking a square root are different: `5 ** 2 = 25`, while `25 ** 0.5 = 5`.

```python
def magnitude(v):
    squared_length = dot(v, v)
    return squared_length ** 0.5
```

| Vector | Squared length | Length |
|--------|----------------|--------|
| `[3, 4]` | 25 | 5 |
| `[6, 8]` | 100 | 10 |
| `[0, 3]` | 9 | 3 |

Remember the final square-root step. The exponent is `0.5`, not `v` or `squared_length`.

## Cosine similarity: compare direction

```python
def cosine_similarity(a, b):
    return dot(a, b) / (magnitude(a) * magnitude(b))
```

For `[2, 0]` and `[3, 0]`, the result is `6 / (2 * 3) = 1`.

- `1`: same direction.
- `0`: perpendicular.
- `-1`: opposite directions.

Both vectors must have nonzero length. Dividing by their lengths removes the length effect from the dot product.

## Normalization: keep direction, make length 1

Divide each coordinate by the original length. `[3, 4]` becomes `[0.6, 0.8]`; `[0, 2]` becomes `[0.0, 1.0]`.

```python
def normalize(v):
    length = magnitude(v)
    if length == 0:
        raise ValueError("Cannot normalize a zero vector")

    result = []
    for coordinate in v:
        result.append(coordinate / length)
    return result
```

The zero vector has no direction. Without the check, normalizing it attempts division by zero.

## Matrices transform vectors

A matrix is a rectangular table of numbers. Each row takes a dot product with the input and produces **one output number**.

```python
def matrix_vector(matrix, v):
    result = []
    for row in matrix:
        result.append(dot(row, v))
    return result
```

Example:

```python
matrix = [[2, 0], [0, 3]]
v = [3, 4]
# First output: 2*3 + 0*4 = 6
# Second output: 0*3 + 3*4 = 12
# Result: [6, 12]
```

After the first pass, `row` is `[2, 0]` and `result` is `[6]`. The next row is `[0, 3]`; it is not the accumulated result.

For a matrix with `m` rows and `n` columns:

- Input length: `n` (number of columns).
- Output length: `m` (number of rows).

A 2-row, 4-column matrix takes 4 input numbers and produces 2 output numbers.

The matrix `[[0, -1], [1, 0]]` rotates vectors 90° counterclockwise:

- `[3, 1]` becomes `[-1, 3]`.
- `[1, 0]` becomes `[0, 1]` (right becomes up).

## Linear independence, basis, and rank

Scaling and adding copies of `[1, 0]` always leaves the second coordinate at zero. This can reach `[4, 0]`, but cannot reach `[0, 1]`.

- `[1, 0]` and `[4, 0]` are dependent: one is a scaled copy of the other.
- `[1, 0]` and `[0, 1]` are independent: neither is a scaled copy of the other.

Independence concerns scaling and adding vectors. Rotating a vector is a different operation.

A **basis** is an independent set that can build every vector in the chosen space. The standard 2D basis is `[1, 0]`, `[0, 1]`:

```text
[5, -2] = 5 × [1, 0] + (-2) × [0, 1]
```

**Rank** is the number of independent column directions (also equal to the number of independent rows).

- `[[1, 2], [0, 0]]` has rank 1: its second column is twice the first.
- `[[1, 0], [0, 1]]` has rank 2: its columns give two independent directions.

We practised these concepts with simple examples; no rank algorithm has been built yet.

## Axis projections and residuals

Projection onto an axis keeps movement along that axis and removes movement perpendicular to it.

```python
def project_horizontal(v):
    return [v[0], 0]

def project_vertical(v):
    return [0, v[1]]
```

For `[3, 7]`, horizontal projection is `[3, 0]` and vertical projection is `[0, 7]`.

The **residual** is the removed part:

```text
original − projection = residual
[3, 7] − [3, 0] = [0, 7]
```

Reusable subtraction:

```python
def subtract(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x - y)
    return result
```

`subtract([5, 8], [2, 3])` gives `[3, 5]`. Subtraction needs `x - y`, not `dot(x - y)`.

To select a coordinate, use an index: `projection[1]` is one number; `projection` is the whole list.

For an orthogonal projection, the projection and residual are perpendicular. We checked the horizontal example with `dot([3, 0], [0, 7]) = 0`.

## Points to practise

- Distinguish a scalar such as `11` from a list such as `[11]`.
- Trace the current loop variables separately from the accumulated result.
- Distinguish squared length from length; use `** 0.5` for the square root.
- Match matrix columns to input length and rows to output length.
- Practise horizontal versus vertical projections and selecting coordinates with indexes.
- Reuse functions by calling them with arguments, for example `dot(row, v)`.
- Training preprocessing statistics must come from the training split only. This needed correction during the warm-up; the training mean was then correctly selected for test values.

The teaching functions above assume matching vector lengths and compatible matrix dimensions. Ordinary `zip` stops at the shorter input; dimension validation has not yet been implemented in this lesson.

## Exact stopping point

We were reusing `subtract` instead of writing coordinate subtraction again:

```python
v = [4, 6]
projection = project_horizontal(v)
residual = subtract(_____, _____)

print(projection)
print(residual)
```

Next exercise: fill in the arguments in original-minus-projection order and report both outputs. The coordinate-by-coordinate version was already supplied correctly; the function-call version is still pending.

Still to cover: projection onto a general nonzero vector, Gram-Schmidt, further from-scratch practice, library equivalents, lesson artifact, and final quiz. The lesson is not complete.
