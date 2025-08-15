#linear regression from scratch using pytorch tensors
import torch

X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
Y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Initialize parameters
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

# Define the forward pass
def forward(X):
    return X * w + b

#loss function(mean squared error)
def mse(y_pred, y_true):
    return ((y_pred - y_true) ** 2).mean()
