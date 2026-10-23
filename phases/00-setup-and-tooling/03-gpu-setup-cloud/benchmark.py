
import time
import torch

size = 300
a = torch.randn(size, size)
b = torch.randn(size, size)
print(a.shape)
print(b.device)

result = a @ b
start = time.perf_counter()

for i in range(10):
    result = a @ b

elapsed = time.perf_counter() - start
average = elapsed / 10
print(average)