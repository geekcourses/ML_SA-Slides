# Import necessary libraries
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Example dataset creation
X, y = make_classification(n_samples=1000, n_features=8, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert data to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)

# Define the model
class SimpleANN(nn.Module):
    def __init__(self):
        super(SimpleANN, self).__init__()
        self.hidden = nn.Linear(8, 32)  # Hidden layer with 32 neurons
        self.output = nn.Linear(32, 1)  # Output layer with 1 neuron

    def forward(self, x):
        x = torch.relu(self.hidden(x))  # ReLU activation for hidden layer
        x = torch.sigmoid(self.output(x))  # Sigmoid activation for output layer
        return x

# Initialize the model, loss function, and optimizer
model = SimpleANN()
criterion = nn.BCELoss()  # Binary Cross-Entropy loss
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(10):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch+1}/10, Loss: {loss.item():.4f}')