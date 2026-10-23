# Lesson 03: GPU Setup & Cloud

Status: completed; first quiz **1/3**, retry **2/3**, with FP16 arithmetic review needed. Notes updated 2026-10-23.

## What I did

- Checked my laptop's graphics hardware: Intel UHD Graphics 600.
- Installed CPU PyTorch inside my local virtual environment after retrying a failed download.
- Created tensors, checked their shape and device, and practised matrix multiplication.
- Wrote a local CPU benchmark with a warm-up and 10 timed multiplications.
- Used a Google Colab T4 GPU runtime, copied tensors to CUDA, and compared CPU and GPU timings.
- Inspected GPU memory and calculated an FP16 weights-only parameter ceiling.

## What I learned

A CPU handles general tasks. A GPU can perform many similar calculations in parallel, which can help model training. CUDA targets NVIDIA GPUs; having an Intel GPU does not provide CUDA support.

Colab runs my code on a remote computer. My laptop returned `False` for CUDA availability, but Colab's NVIDIA T4 returned `True`.

A tensor holds numbers. Its `shape` describes its dimensions, and its `device` tells me where it is stored. For example, a tensor with shape `[2, 3]` has two rows and three columns.

```python
b = a.to("cuda")
```

This stores a GPU copy in `b`; it does not move the original `a` in place. Both operands of the matrix multiplication I practised must be on the same device.

## Local setup and exercise files

```bash
source .venv/bin/activate
uv pip install torch --index-url https://download.pytorch.org/whl/cpu
python -c "import torch; print(torch.__version__)"
```

My reported local version was `2.14.1+cpu`.

- [check_device.py](check_device.py): checked CUDA, doubled tensor elements, and multiplied features by weights.
- [benchmark.py](benchmark.py): measured a 300 × 300 CPU multiplication, averaged over 10 repetitions after a warm-up.
- [Colab notebook](Untitled0.ipynb): contains the remote CPU/GPU comparison and memory calculation.

In the matrix exercise, `[[2, 3]] @ [[10], [20]]` produced `[[80]]`: multiply matching entries and add, giving `2 × 10 + 3 × 20`. Changing the features to `[[1, 4]]` gives `90`.

## Benchmark method

1. Create matching inputs on CPU and GPU before timing.
2. Warm up each device with one multiplication.
3. Start `time.perf_counter()` before the work.
4. Multiply 10 times inside the loop.
5. Calculate total elapsed time after the loop, then divide by 10.

For GPU timing, call `torch.cuda.synchronize()` after the warm-up and again after the timed loop, before reading the end time. Python can otherwise reach the timer before the GPU finishes.

## Saved Colab results

These are the saved notebook's results for 1,000 × 1,000 matrices, not the smaller local benchmark.

| Measurement | Result |
|-------------|--------|
| PyTorch | 2.11.0+cu130 |
| GPU | NVIDIA Tesla T4 |
| Total GPU memory | 15,637,086,208 bytes, about 14.56 GiB |
| CPU average | 0.0196659302 seconds, about 19.666 ms |
| GPU average | 0.0007926241 seconds, about 0.793 ms |
| CPU average / GPU average | About 24.81× |

The input transfers to the GPU happened outside the timer. The comparison measures multiplication with inputs already on their devices, not the total application time. Timings vary between runs. A GPU can lose on a small task when transfer and launch costs outweigh faster computation.

## Memory estimate

FP16 weights take 2 bytes per parameter:

```text
15,637,086,208 bytes / 2 = 7,818,543,104 parameters
                           ≈ 7.82 billion parameters
```

This is a theoretical weights-only ceiling using total memory, not a model size guaranteed to fit. Memory already in use and working data reduce capacity. Training also needs gradients, optimizer state, and intermediate results.

## Mistakes and corrections

- My Intel GPU does not support CUDA, but Colab's remote T4 does.
- Calling `synchronize()` does not move CPU calculations to the GPU; I must use GPU tensors.
- The multiplication must be inside the repetition loop; printing the same timing 10 times does not measure 10 operations.
- The timer starts before multiplication. GPU synchronization after the loop ensures the last operation has finished.
- I initially predicted GPU copies would also move the original tensor. The device output showed otherwise.

## Still to do

- Retain NVIDIA status recall: `nvidia-smi` reports GPU status, memory usage, and processes. I answered this correctly on the retry. `torch.cuda.list_devices()` is not a valid PyTorch function.
- Review FP16 arithmetic: 24 GB (24 billion bytes) divided by 2 bytes per parameter gives 12 billion parameters for weights alone. This excludes working and training memory.
- First quiz: NVIDIA status command incorrect; synchronization correct; FP16 estimate incorrect. Retry: NVIDIA status and synchronization correct; FP16 estimate still incorrect. Both attempts are recorded in LEARNING.md.
- Update dependency documentation: the current root `requirements.txt` lists NumPy but does not yet include the PyTorch installed during this lesson or its CPU package source.

Self-check: can I explain why a CUDA check differs between my laptop and Colab, and why a weights-only limit is not a training limit?
