# Lesson 12: Debugging & Profiling

Date: 2026-10-24
Quiz: first attempt **1/3**; retake **3/3**.

## Debugging versus profiling

| Tool or activity | Purpose |
|------------------|---------|
| Debugging | Find why a program behaves incorrectly |
| `breakpoint()` / pdb | Pause execution and inspect values |
| `cProfile` | Measure function execution times |
| `tracemalloc` | Locate tracked Python memory allocations |
| TensorBoard | Visualize recorded metrics over time |

A program can run without crashing and still produce incorrect results. AI bugs can also make evaluation metrics look better than they should.

## Finding a logic bug

The original function incorrectly divided by a fixed number:

```python
def average(values):
    return sum(values) / 2
```

For `[10, 20, 30]`, it returns `30.0`, but the correct average is `60 / 3 = 20.0`. The divisor must be `len(values)`.

## Inspecting values with pdb

In [debug_practice.py](debug_practice.py), I placed a breakpoint before division:

```python
def average(values):
    total = sum(values)
    count = len(values)
    breakpoint()
    return total / count
```

Run the script normally:

```bash
python debug_practice.py
```

At the `(Pdb)` prompt, enter debugger commands rather than running the script again:

| Command | Meaning | Observed result |
|---------|---------|-----------------|
| `p total` | Print the value of total | `60` |
| `p count` | Print the value of count | `3` |
| `c` | Continue execution | Function returned the average |

The arrow in pdb showed the next line to execute. It had not performed the division yet. Remove temporary breakpoints after finishing the investigation.

## Handling an empty list

For an empty list, both sum and length are zero. Dividing by zero raises `ZeroDivisionError`; it does not return zero.

I added an input check before the calculation:

```python
def average(values):
    if not values:
        raise ValueError("Cannot average an empty list")
    return sum(values) / len(values)
```

Observed results:

- `[10, 20, 30]` produced **20.0**.
- `[]` raised **ValueError: Cannot average an empty list**.

A traceback's last line gives the exception type and message. Entries above show where it was raised and how execution reached that point.

## Finding the time bottleneck

My [profile_practice.py](profile_practice.py) used:

```python
import time


def load_data():
    time.sleep(0.3)
    return [10, 20, 30]


def calculate(values):
    return sum(values) / len(values)


values = load_data()
print(calculate(values))
```

I profiled it with:

```bash
python -m cProfile -s cumtime profile_practice.py
```

Observed total runtime was about **0.301 seconds**. `load_data` accounted for about **0.300 seconds**, spent in `time.sleep`.

| Column | Meaning |
|--------|---------|
| `ncalls` | Number of calls |
| `tottime` | Time in the function itself, excluding functions it calls |
| `cumtime` | Time in the function including its calls |

`load_data` had near-zero own time but 0.300 seconds cumulative time because it called `sleep`. Optimizing `calculate` would barely affect this example's total runtime.

Investigate the bottleneck the measurements reveal. Data loading is not automatically the bottleneck in every training run.

## Tracking Python allocations

My [memory_practice.py](memory_practice.py):

```python
import tracemalloc

tracemalloc.start()

data = [bytearray(1_000) for _ in range(1_000)]

snapshot = tracemalloc.take_snapshot()
for entry in snapshot.statistics("lineno")[:3]:
    print(entry)
```

The snapshot identified line 5 with approximately **1041 KiB** of tracked allocations, including overhead. Reported allocation count: **2002**. This count is not the number of dataset examples.

`tracemalloc` tracks Python memory allocations. It does not measure all native-library allocations, total process memory, or GPU memory.

## Inspecting a tensor

In [tensor_debug.py](tensor_debug.py), I created:

```python
import torch

x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

print("Shape:", x.shape)
print("dtype:", x.dtype)
print("Device:", x.device)
print("Has NaN:", torch.isnan(x).any().item())
```

Observed output:

```text
Shape: torch.Size([2, 3])
dtype: torch.float32
Device: cpu
Has NaN: False
```

- **Shape:** two rows and three columns.
- **dtype:** the kind of stored values, here float32.
- **Device:** where the tensor lives, here CPU.
- **NaN check:** whether any value is not a number.

A filename typo, `tensor_debug.p`, initially caused a missing-file error. Using `tensor_debug.py` fixed the command.

## Detecting NaN and infinity

I inserted a NaN before the print statements:

```python
x[0, 0] = float("nan")
```

`Has NaN` then became **True**.

```python
print("All finite:", torch.isfinite(x).all().item())
```

This printed **False**. `isfinite` excludes both NaN and infinity; `.all()` asks whether every element passed the check.

For floating-point tensors, nonzero division by zero generally gives infinity, while `0 / 0` gives NaN. Ordinary Python numeric division by zero raises an exception.

A conditional breakpoint can pause when a scalar loss becomes NaN:

```python
if torch.isnan(loss).item():
    breakpoint()
```

This conditional example was discussed, not executed in a real training loop. Investigate where invalid values first appear rather than immediately changing optimizers or restarting with another seed.

## Data leakage

Data leakage occurs when information that should be held out enters model training or selection. Examples include overlapping train/test records or features that reveal the target.

Unexpectedly high test accuracy warrants checking for leakage. High accuracy alone does not prove a bug, and a large batch size alone does not explain it.

## Loss and overfitting

**Loss measures error: lower is better.**

- Training loss measures performance on examples used for learning.
- Validation loss measures performance on held-out validation examples.

I used these simulated values:

| Epoch | Training loss | Validation loss |
|-------|---------------|-----------------|
| 1 | 0.8 | 0.9 |
| 2 | 0.5 | 0.7 |
| 3 | 0.3 | 0.8 |
| 4 | 0.1 | 1.0 |

After epoch 2, training improves while validation worsens. This pattern suggests **overfitting**, rather than improvement on unseen data. Validation loss is the relevant column for the held-out validation examples.

## Recording and viewing losses in TensorBoard

I installed TensorBoard in the project environment:

```bash
uv pip install tensorboard
```

My [log_losses.py](log_losses.py) recorded the simulated values:

```python
from torch.utils.tensorboard import SummaryWriter

training = [0.8, 0.5, 0.3, 0.1]
validation = [0.9, 0.7, 0.8, 1.0]

with SummaryWriter("runs/loss_demo") as writer:
    for epoch, (train_loss, val_loss) in enumerate(zip(training, validation), start=1):
        writer.add_scalar("loss/train", train_loss, epoch)
        writer.add_scalar("loss/validation", val_loss, epoch)
```

`zip` pairs corresponding values. `enumerate(..., start=1)` supplies epoch numbers. `SummaryWriter` saves event data for TensorBoard.

From the lesson directory:

```bash
python log_losses.py
tensorboard --logdir=runs --host=127.0.0.1 --port=6006
```

I opened `http://localhost:6006` and confirmed both loss plots were visible. **Ctrl+C** stops the TensorBoard server. These plots came from simulated values, not a trained model.

## GPU memory concept

A batch is a group of examples processed in one step. With the same model and example sizes, reducing the batch size generally reduces memory needed for intermediate results. A batch of 8 generally needs less memory than a batch of 64.

Clearing a GPU cache does not free tensors the program still uses. No GPU-memory experiment was performed in this session.

## Quiz and reflection

- First attempt: **1/3**. NaN debugging was correct; data leakage and identifying the measured bottleneck needed review.
- Retake: **3/3**. All three topics were recalled correctly.
- Original attempt preserved; quiz review item cleared.
- I needed extra practice with the debugger prompt, zero division, finite checks, validation loss, and the meaning of increasing versus decreasing loss.
- Results were learner-reported. Official toolkit execution, real training-loop profiling, gradient inspection, line profiling, GPU-memory checks, and the VS Code debugger were not tested.

Next lesson: **Python for AI Engineering**.
