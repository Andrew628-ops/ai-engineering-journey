# Lesson 05: Jupyter Notebooks

Date: 2026-10-23
Interface: Google Colab
Final quiz: **3/3**

## What a notebook does

A notebook combines executable code cells, Markdown text cells, and outputs in an `.ipynb` file. It is useful for exploring data, trying ideas, and documenting experiments.

The **kernel** is the Python process that runs the cells. All code cells share its variables and imports.

## Cell execution and hidden state

I tested two cells:

```python
price = 10
```

```python
print(price * 2)
```

The second cell printed `20`.

- Editing the first cell to `price = 30` without running it left the output at `20`.
- Running the edited first cell, then the second, produced `60`.
- Restarting the kernel clears variables and imports. Running only the second cell after a restart would raise `NameError`.
- After restarting, running both cells in order produces `60`.

The visible code can differ from the values stored in memory. This is hidden state. Before sharing a notebook, restart the kernel and run all cells from top to bottom.

I used Colab's restart-and-run-all action and reported that every cell completed successfully.

## Code cells and Markdown cells

Code cells execute Python. Markdown cells explain the purpose and results of an experiment.

Example Markdown:

```markdown
# My First Notebook

## Experiment: remembered variables
Editing a code cell does not update a variable until I run the cell.
```

**Shift+Enter** runs the current cell and moves to the next.

## Automatic output

A notebook automatically displays the value of the last expression in a code cell:

```python
price
price * 2
```

With `price = 30`, only `60` is automatically displayed. To display both values:

```python
print(price)
print(price * 2)
```

Output:

```text
30
60
```

## Timing code

Magic commands are notebook commands beginning with `%` or `%%`.

| Command | Behavior | Useful for |
|---------|----------|------------|
| `%%time` | Runs the cell once and reports timing | A long operation, such as model training |
| `%timeit` | Repeats a statement and reports timing statistics | Small, quick operations |

I ran:

```python
%%time
total = sum(range(1_000_000))
print(total)
```

Observed output:

```text
499999500000
CPU times: user 24.8 ms, sys: 0 ns, total: 24.8 ms
Wall time: 24.7 ms
```

CPU time measures processor time used; wall time measures elapsed time. Small differences can come from measurement precision.

I also ran:

```python
%timeit sum(range(1_000))
```

Observed output:

```text
23.1 µs ± 6.41 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

Each loop is one execution of the statement. The result summarizes repeated measurements, rather than guaranteeing that every execution takes exactly that long.

## Python list versus NumPy benchmark

Setup cell:

```python
import random
import numpy as np
```

Separate timing cells:

```python
%timeit [random.random() for _ in range(100_000)]
```

```python
%timeit np.random.random(100_000)
```

My results:

| Method | Mean time | Standard deviation |
|--------|-----------|--------------------|
| Python list | 7.51 ms | 257 µs |
| NumPy array | 971 µs (0.971 ms) | 245 µs |

NumPy took about **7.7 times less time** in this test (`7.51 / 0.971`). It generates values in compiled code instead of executing a Python loop for every value. The outputs also differ: one is a Python list and the other a NumPy array. These measurements apply to this experiment and runtime.

After a kernel restart, the import cell must run before these timing cells.

## Displaying a table

```python
import pandas as pd

results = pd.DataFrame({
    "method": ["Python list", "NumPy array"],
    "time_ms": [7.51, 0.971],
})
results
```

A DataFrame is a table with named columns. Leaving it as the final expression displays a formatted table in Colab.

## Plotting the results

```python
import matplotlib.pyplot as plt

results.plot.bar(x="method", y="time_ms", legend=False)
plt.ylabel("Time (milliseconds)")
plt.title("Generating 100,000 random numbers")
plt.show()
```

The NumPy array has the shorter bar. Here, a shorter bar means less execution time and therefore faster performance.

## Saving and loading CSV data

```python
results.to_csv("timing_results.csv", index=False)
```

`index=False` leaves the DataFrame's row index out of the saved file.

```python
loaded_results = pd.read_csv("timing_results.csv")
loaded_results
```

I compared the original and loaded tables. Both contained the same methods and timings. `7.510` and `7.51` are the same numeric value; the extra zero is display formatting.

## Notebooks and scripts

Use notebooks for exploration, quick experiments, tables, charts, and explanations. Move stable code into `.py` files when it becomes a reusable utility, training pipeline, or production task.

## What I corrected

- Restarting the kernel clears variables; it does not execute the visible code automatically.
- Only the last expression is automatically displayed; use `print()` to show multiple values.
- Use `%%time` to run a long task once and `%timeit` for repeated small benchmarks.
- In a chart of execution time, the shorter bar represents the faster method.

## Completion

I completed the exercises in Google Colab and scored **3/3** on the lesson quiz. The notebook was not inspected locally, and the optional GPU exercise was not performed in this session.

To keep the notebook with these notes, download it from Colab as an `.ipynb` file and save it in this folder. Download `timing_results.csv` too if I want to preserve that runtime file.

Next lesson: **Python Environments**.
