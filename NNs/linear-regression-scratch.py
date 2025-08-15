#linear regression from scratch using pytorch tensors
import torch

X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
Y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Initialize parameters
# random initialization of weights and bias
# requires_grad=True allows us to compute gradients for these parameters
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)

# Define the forward pass
def forward(X):
    return X * w + b

#loss function(mean squared error)
def mse(y_pred, y_true):
    return ((y_pred - y_true) ** 2).mean()

# Training loop
learning_rate = 0.01
epoch = 100

for epoch in range(epoch):
    # Forward pass
    y_pred = forward(X)
    
    # Compute loss
    loss = mse(y_pred, Y)
    
    # Backward pass
    # backpropagation to compute gradients
    loss.backward()
    
    # Update parameters
    # using the gradients computed in the backward pass
    with torch.no_grad():
        w -= learning_rate * w.grad
        b -= learning_rate * b.grad
    
    # Zero gradients
    # reset gradients to zero for the next iteration
    w.grad.zero_()
    b.grad.zero_()
    
    # Print loss every 10 epochs
    # this helps to monitor the training process
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{epoch}], Loss: {loss.item():.4f}')

# Final parameters
print("Final parameters:", w.item(), b.item())
# Prediction after training
# using the trained model to make predictions
print(f'Prediction after training: f(5) = {forward(torch.tensor([5.0])).item()}')

#accuracy of the model
# since this is a simple linear regression, we can check the accuracy by comparing the predicted values
# with the actual values
predicted = forward(X)
accuracy = ((predicted - Y) ** 2).mean().item()
print(f'Accuracy: {100 - accuracy}%')

