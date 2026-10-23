# GOAL 
Learning numpy and want to preparing my project for github

## Lesson notes

My [Phase 00 notes](phases/00-setup-and-tooling/NOTES.md) link to what I did and learned in each lesson, including mistakes, results, and remaining work.

## SETUP

### Create environment 
```bash
uv venv
```
### Activate it
```bash
source .venv/bin/activate
```
### Install  requirements.txt
```bash
uv pip install -r requirements.txt
```
### Run the hello_ai.py and check_numpy.py using
python3 hello_ai.py or python hello_ai.py 
python3 check_numpy.py or python check_numpy.py
## What i learned
i learnt that multiplying a python list repeat the list the number of times it is been multiply while multiplying a numpy multiply each number in the list

## Git practice 
git add stages the changes

### Why use branch
Branches let me experiment separately from `main`. I can merge the changes when they are ready; conflicts can still happen during a merge.

## CPU vs GPU experiment

I used Google Colab to compare matrix multiplication on a CPU and an NVIDIA Tesla T4 GPU. My laptop has Intel UHD Graphics 600, so the CUDA experiment ran on Colab's remote computer.

The experiment used two 1,000 × 1,000 tensors, one warm-up multiplication per device, and 10 timed multiplications. I divided each total time by 10 to find the average. For the GPU, I called `torch.cuda.synchronize()` before starting the timer and after the loop so the measurement included completed GPU work.

| Measurement | Result |
|-------------|--------|
| Colab PyTorch version | 2.11.0+cu130 |
| GPU | NVIDIA Tesla T4 |
| Total GPU memory | About 14.56 GiB |
| CPU average per multiplication | 19.666 ms |
| GPU average per multiplication | 0.793 ms |
| CPU time divided by GPU time | About 24.81× |

These values come from the saved notebook's outputs. The input tensors were already on each device before timing, so this comparison excludes CPU-to-GPU transfers. Results vary between runs; a GPU is not always faster for small tasks.

### Model memory estimate

The GPU reported 15,637,086,208 bytes of total memory. FP16 weights use 2 bytes per parameter:

```text
15,637,086,208 / 2 = 7,818,543,104 parameters
```

That is a theoretical weights-only ceiling of about 7.82 billion parameters. It does not account for memory already in use or working memory. Training also needs gradients, optimizer state, and intermediate results, so the model I can train must be smaller than this ceiling.

### Experiment files

- [Colab notebook](phases/00-setup-and-tooling/03-gpu-setup-cloud/Untitled0.ipynb)
- [Local CPU benchmark](phases/00-setup-and-tooling/03-gpu-setup-cloud/benchmark.py)
- [Local device check](phases/00-setup-and-tooling/03-gpu-setup-cloud/check_device.py)
