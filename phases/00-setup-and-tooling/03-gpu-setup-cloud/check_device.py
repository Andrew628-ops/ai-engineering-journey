import torch
print(torch.__version__)
print(torch.cuda.is_available())
result = torch.tensor([1, 2, 3])
print(result * 2)

# table = torch.tensor([[1, 2, 3], [4, 5, 6]])
# print(table)
# print(table.shape)
# print(table.device)

features = torch.tensor([[2.0, 3.0]])
weights = torch.tensor([[10.0], [20.0]])
print(features @ weights)