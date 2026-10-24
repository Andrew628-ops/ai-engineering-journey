# Lesson 09: Data Management

Date: 2026-10-24
Interface: Google Colab
Quiz: **3/3**

## Why separate data into groups?

A model can memorize examples it learns from. Evaluating only on those examples can give a misleading impression of how well it handles new data.

| Split | Purpose |
|-------|---------|
| Training | Examples the model learns from |
| Validation | Examples used to compare choices and tune the model |
| Test | Held-out examples reserved for final evaluation |

Generalization means performing well on unseen examples. Keeping evaluation data separate helps assess it. Repeatedly tuning against the test set undermines its role as a final evaluation.

## Calculating split sizes

The order **70/15/15** means training / validation / test.

| Total examples | Training (70%) | Validation (15%) | Test (15%) |
|----------------|----------------|------------------|------------|
| 20 | 14 | 3 | 3 |
| 100 | 70 | 15 | 15 |
| 200 | 140 | 30 | 30 |
| 300 | 210 | 45 | 45 |

Calculate a count by multiplying the total by the fraction. For example, `300 × 0.70 = 210`. Percentages are not the same as counts unless the total is 100. Some dataset sizes require rounding.

## Manual split with a fixed seed

I created 20 uniquely numbered examples:

```python
examples = list(range(20))
```

Then shuffled a copy:

```python
import random

shuffled = examples.copy()
random.Random(42).shuffle(shuffled)
```

Each run starts from the same original list and uses the same seed. This repeated the order without changing `examples`.

```python
train = shuffled[:14]
validation = shuffled[14:17]
test = shuffled[17:20]
```

Observed groups:

```text
Training:   [19, 5, 14, 4, 9, 13, 15, 18, 6, 12, 17, 10, 1, 11]
Validation: [2, 16, 7]
Test:       [8, 0, 3]
```

A slice uses an ending position, not a count. `[14:17]` includes positions 14, 15, and 16; it excludes position 17. To take three items from position 14, the ending position is `14 + 3 = 17`. `[17:]` also selects the final three items here.

For these unique example IDs, checking pairwise intersections should produce empty sets:

```python
print(set(train) & set(validation))
print(set(train) & set(test))
print(set(validation) & set(test))
```

Expected output:

```text
set()
set()
set()
```

For real datasets, also consider duplicate records and related examples that could leak information across splits. A random split is not appropriate for every task, such as some time-series problems.

## Using Hugging Face datasets

In Colab:

```python
%pip install datasets
```

```python
from datasets import Dataset

dataset = Dataset.from_dict({"id": examples})
print(dataset)
print(dataset[:3])
```

Observed: one column, `id`, with 20 rows. The first three IDs were `[0, 1, 2]`.

## Library split: 70/15/15

First hold out 30%:

```python
split = dataset.train_test_split(test_size=0.30, seed=42)
```

This produces 14 training rows and 6 held-out rows. The temporary `"test"` group will be divided further.

```python
held_out = split["test"].train_test_split(test_size=0.5, seed=42)

train_ds = split["train"]
validation_ds = held_out["train"]
test_ds = held_out["test"]

print(len(train_ds), len(validation_ds), len(test_ds))
```

Output: `14 3 3`.

The second `test_size=0.5` takes half of the **6 held-out rows**, not half of the original 20.

Observed IDs:

```text
Training:   [6, 19, 3, 0, 16, 5, 11, 18, 2, 4, 17, 1, 13, 8]
Validation: [12, 9, 15]
Test:       [7, 14, 10]
```

The library and Python's `random` need not produce identical shuffles with the same seed: they can use different implementations.

## Checking reproducibility

The same seed, input data, row order, and splitting implementation help reproduce a split. Keeping the split fixed makes model comparisons fairer.

I saved the training IDs:

```python
previous_train_ids = list(train_ds["id"])
```

After rerunning both splitting cells:

```python
print(previous_train_ids == list(train_ds["id"]))
```

The output was **True**. This explicitly checked training-ID reproducibility; equivalent checks can be applied to validation and test IDs.

`Column([6, 19, 3, 0, 16, ...])` is a shortened display, not missing data. `list(train_ds["id"])` displays all IDs for this small dataset.

## CSV and Parquet

```python
dataset.to_csv("examples.csv")
dataset.to_parquet("examples.parquet")
```

| Format | Characteristics |
|--------|-----------------|
| CSV | Plain-text rows; easy to inspect and exchange with spreadsheets |
| Parquet | Binary, column-oriented storage; supports compression and efficient column reads |

I measured the files:

```python
from pathlib import Path

print("CSV bytes:", Path("examples.csv").stat().st_size)
print("Parquet bytes:", Path("examples.parquet").stat().st_size)
```

Observed sizes:

```text
CSV bytes: 53
Parquet bytes: 949
```

Parquet was larger for this tiny dataset because its metadata outweighed storage savings. It is not always smaller or faster; benefits depend on the data and workload.

## Loading Parquet back

```python
from datasets import load_dataset

restored = load_dataset(
    "parquet",
    data_files="examples.parquet",
    split="train",
)

print(len(restored))
print(list(restored["id"]) == list(dataset["id"]))
```

Output: **20**, then **True**. The row count and ID order survived the round trip.

Here, `split="train"` selects the loader's default split name. It does not perform a training/evaluation split.

## Caching and streaming

A **cache** is a local copy of previously fetched or processed data. It can avoid repeated downloads or processing.

**Streaming** processes examples on demand without first downloading and preparing the entire dataset. It still uses memory for current examples, buffers, and any transformations.

I practised with a local CSV:

```python
streamed = load_dataset(
    "csv",
    data_files="examples.csv",
    split="train",
    streaming=True,
)

for example in streamed.take(5):
    print(example)
```

Observed IDs: **0, 1, 2, 3, 4**, each printed in a dictionary such as `{'id': 0}`.

This demonstrated an iterable dataset over a local file. It did not test remote streaming or remote download caching.

## Large files and version control

| Approach | Purpose |
|----------|---------|
| `.gitignore` | Excludes untracked files from normal Git tracking; does not back them up |
| Git LFS | Keeps pointers in Git and stores large file contents separately |
| DVC | Tracks data/model versions using metadata, with contents stored separately |

Pushing code does not upload an ignored, untracked dataset. Ignore rules do not untrack a file already committed to Git.

For reproducible experiments, record the dataset source and revision, preprocessing steps, split method and seed, and relevant software versions. DVC can help version the exact data; a configured remote is needed to share its contents across machines.

## Reflection and completion

- I needed practice turning percentages into counts and using slice end positions.
- I created a reproducible 70/15/15 split, exported data, checked a Parquet round trip, and streamed five local examples.
- Quiz: **3/3**, covering Parquet, streaming, and DVC.
- Results were shared from Colab; the notebook was not inspected locally.
- Remote Hub dataset/model downloads, remote streaming, and actual LFS/DVC setup were not performed.

Download the Colab notebook and any generated files I want to preserve, then save them in this lesson folder. Runtime files should not be assumed to persist after the Colab runtime is discarded.

Next lesson: **Terminal & Shell**.
