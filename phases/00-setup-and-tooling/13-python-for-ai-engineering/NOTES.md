# Lesson 13: Python for AI Engineering

Date: 2026-10-24
Quiz: first attempt **1/2**; retake **2/2**.

## Session scope

We worked through Python examples interactively, then switched to larger exercises at my request. Results below were learner-reported. The full reference toolkit and all optional exercises were not completed.

Practice files:

- [lists_practice.py](lists_practice.py)
- [records_practice.py](records_practice.py)
- [math_practice.py](math_practice.py)
- [reviews.json](reviews.json) and [reviews.csv](reviews.csv)

## Assignment and list copies

Assignment binds a name to an object; it does not copy the object.

```python
values = [10, 20, 30]
other = values
other[1] = 50
print(values)  # [10, 50, 30]
```

An indexed assignment replaces an item; it does not insert another item.

For an independent flat list:

```python
values = [10, 20, 30]
other = values.copy()
other[1] = 50
print(values)  # [10, 20, 30]
print(other)   # [10, 50, 30]
```

`.copy()` is shallow: nested objects can still be shared.

## Independent rows in a nested list

```python
grid = [[0, 0]] * 2
grid[0][0] = 1
print(grid)  # [[1, 0], [1, 0]]
```

Both rows refer to one inner list. Create a new list for each row instead:

```python
grid = [[0, 0] for _ in range(2)]
grid[0][0] = 1
print(grid)  # [[1, 0], [0, 0]]
```

## Comprehensions

```python
numbers = [1, 2, 3, 4]
squares = [number ** 2 for number in numbers]
large = [number for number in numbers if number > 2]
result = [number ** 2 for number in numbers if number > 2]
```

Results: `[1, 4, 9, 16]`, `[3, 4]`, and `[9, 16]`.

The expression before `for` transforms each selected item. A trailing `if` filters which items are included.

## Unpacking and f-strings

```python
record_id, label = ("review-01", 1)
```

This assigns the first value to `record_id` and the second to `label`.

In a loop, unpacking happens once per item:

```python
pairs = [("apple", 3), ("banana", 5), ("orange", 2)]

for name, count in pairs:
    print(f"{name}: {count}")
```

Observed output:

```text
apple: 3
banana: 5
orange: 2
```

There are three tuples, so there are three loop passes. Each pass assigns a new pair of values. An f-string inserts values or expression results into `{...}`.

I also printed:

```text
Alice scored 80
Bob scored 90
```

using tuple unpacking and an f-string.

## Default and keyword-only arguments

```python
def scale(value, *, factor=2):
    return value * factor

print(scale(3))            # 6
print(scale(3, factor=4))  # 12
```

The default factor is 2. The `*` makes `factor` keyword-only: `scale(3, 4)` raises `TypeError`.

## Mutable default arguments

Python evaluates a default once when the function is defined:

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana']
```

Use `None` to create a fresh list when the caller supplies no list:

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

Observed outputs from separate calls: `['apple']`, then `['banana']`.

If I explicitly pass an existing list, the function changes that list:

```python
basket = ["pear"]
add_item("banana", bucket=basket)
print(basket)  # ['pear', 'banana']
```

## Closures

A closure is a function that keeps access to values from the function that created it.

```python
def make_multiplier(factor):
    def multiply(value):
        return value * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
times_ten = make_multiplier(10)
```

`double(6)` returns 12, `triple(6)` returns 18, and `times_ten(7)` returns 70. The remembered factor comes from the argument to `make_multiplier`, not the inner function's name.

## Generators and exhaustion

A generator produces items on request and is exhausted after one pass:

```python
items = (n for n in [10, 20])
print(next(items))  # 10
print(next(items))  # 20
print(list(items))  # []
```

These were the observed outputs. Another `next()` after exhaustion would raise `StopIteration`. A list can be iterated repeatedly, but an exhausted generator must be recreated.

## Mini-batches across epochs

```python
def batches(items, batch_size):
    for start in range(0, len(items), batch_size):
        yield items[start:start + batch_size]

data = [10, 20, 30, 40, 50]

for epoch in range(1, 3):
    print(f"Epoch {epoch}")
    for batch in batches(data, batch_size=2):
        print(batch)
```

Observed batches in each epoch: `[10, 20]`, `[30, 40]`, `[50]`.

The final batch has one item because five does not divide evenly by two. Calling `batches` inside the epoch loop creates a fresh generator for each epoch. This teaching version expects a positive integer batch size and a sliceable input.

## Dataclass records

```python
from dataclasses import dataclass

@dataclass
class Record:
    text: str
    label: int
```

The decorator generates methods such as the initializer, representation, and equality comparison. I can create a record with `Record("Great movie", 1)` and access `.text` and `.label`. Annotations alone do not enforce runtime types.

## JSON and CSV files

The workflow is **save → load → convert → inspect**.

```python
import json

with open("reviews.json", "w", encoding="utf-8") as file:
    json.dump([{"text": "Great movie", "label": 1}], file)

with open("reviews.json", "r", encoding="utf-8") as file:
    rows = json.load(file)

records = [Record(text=row["text"], label=row["label"]) for row in rows]
```

I initially used `rows` before loading it. Assigning the result of `json.load` to `rows` fixes that undefined-name problem.

A `with` block closes the file when the block exits, including on an exception. JSON output was confirmed for one review: `Great movie 1`. A second review was proposed but not confirmed.

CSV export:

```python
import csv

with open("reviews.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["text", "label"])
    writer.writeheader()
    writer.writerows(rows)
```

Observed CSV:

```text
text,label
Great movie,1
```

CSV fields are text when read with `csv.DictReader`; convert the label with `int(row["label"])` if an integer is needed. JSON preserves this integer value when loaded. CSV reading and conversion were explained but not tested.

## Mean and dot product

```python
def mean(values):
    return sum(values) / len(values)

def dot(a, b):
    return sum(x * y for x, y in zip(a, b, strict=True))
```

Observed results:

- `mean([2, 4, 6])` → **4.0**
- `dot([1, 2, 3], [4, 5, 6])` → **32**

The dot product is `1*4 + 2*5 + 3*6`. `zip(..., strict=True)` raises an error for unequal lengths instead of silently stopping at the shorter input. This simple mean function needs nonempty input.

Library checks matched: `statistics.fmean` returned 4.0 and `math.sumprod` returned 32. `math.sumprod` requires Python 3.12 or newer.

## NumPy broadcasting

```python
import numpy as np

data = np.array([[1.0, 10.0], [3.0, 30.0]])
column_means = data.mean(axis=0)
centered = data - column_means
```

Observed means: `[2.0, 20.0]`.

Observed centered array:

```text
[[ -1. -10.]
 [  1.  10.]]
```

`axis=0` computes one mean per column. Broadcasting applies the column means to every row without a Python loop in my code. NumPy can process large numeric arrays efficiently using compiled loops over raw numerical values. No performance benchmark was run in this lesson.

## Standardization and leakage

Standard deviation measures spread. Standardization uses:

```text
(value - training_mean) / training_standard_deviation
```

Compute these statistics from the **training split only**, then reuse them for validation and test data. Combining test data with training statistics leaks held-out information. Recomputing separate statistics for each evaluation mini-batch changes the preprocessing rather than applying the fitted training transformation.

Constant features need explicit handling because their standard deviation is zero. The standard-deviation implementation and full standardizer were not built during this session.

## Reproducible splits

We reused the Data Management lesson's idea: shuffle with a local seeded generator such as `random.Random(42)`. Reproducibility also depends on the input data, ordering, and implementation. No new seeded-split implementation was written in this session.

## Quiz and remaining practice

- First attempt: **1/2**. Mutable defaults were correct; training-only standardization needed review.
- Retake: **2/2**. Both concepts recalled correctly; original attempt preserved.
- Revisit shared references, loop unpacking, closures, and exhausted generators through future practical exercises.
- Full toolkit/classifier, standard-deviation implementation, large-file streaming, and speed/memory comparison exercises remain unperformed.
- All Phase 0 lessons are logged; practical gaps and remaining reviews are recorded in `LEARNING.md`.

Next: **Math Foundations**. Use `check-understanding 0` for a Phase 0 review.
