import torch

x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
x[0, 0] = float("nan")

print("Shape:", x.shape)
print("dtype:", x.dtype)
print("Device:", x.device)
print("Has NaN:", torch.isnan(x).any().item())

print("All finite:", torch.isfinite(x).all().item())