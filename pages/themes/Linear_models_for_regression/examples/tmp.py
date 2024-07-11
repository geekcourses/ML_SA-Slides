import numpy as np
import matplotlib.pyplot as plt

# Function to compute the cost (Mean Squared Error)
def compute_cost(X, y, beta):
    m = len(y)
    predictions = X.dot(beta)
    cost = (1/(2*m)) * np.sum(np.square(predictions - y))
    return cost

# Function to perform gradient descent
def gradient_descent(X, y, beta, learning_rate, iterations):
    m = len(y)  # Number of training examples
    cost_history = np.zeros(iterations)  # To store cost at each iteration

    for i in range(iterations):
        predictions = X.dot(beta)  # Compute predictions
        errors = predictions - y  # Compute error
        gradients = X.T.dot(errors)  # Compute gradients
        beta = beta - (learning_rate / m) * gradients  # Update parameters
        cost_history[i] = compute_cost(X, y, beta)  # Store cost for plotting

    return beta, cost_history

# Generate some data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add x0 = 1 to each instance (bias/intercept term). The optimal value will be learned.
X_b = np.c_[np.ones((100, 1)), X]

# Initialize beta
beta_initial = np.random.randn(2, 1)

# Set hyperparameters
learning_rate = 0.1
iterations = 50

# Perform gradient descent
beta, cost_history = gradient_descent(X_b, y, beta_initial, learning_rate, iterations)

# Extract the bias (intercept) and coefficient(s)
bias = beta[0, 0]
coefficients = beta[1:, 0]

print(f"Optimized parameters: bias={bias}, coefficients={coefficients}")


# Plot cost history
plt.plot(range(iterations), cost_history)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost Function')
plt.show()

