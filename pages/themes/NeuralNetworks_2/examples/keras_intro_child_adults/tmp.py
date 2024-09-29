# Import necessary libraries
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split

# Create a small dataset with height, weight, and labels (1 = Adult, 0 = Child)
data = np.array([
    [150, 50],  # Child
    [160, 60],  # Child
    [170, 65],  # Child
    [180, 75],  # Adult
    [190, 90],  # Adult
    [175, 80],  # Adult
    [165, 55],  # Child
    [185, 85],  # Adult
    [155, 45],  # Child
    [195, 100],  # Adult
])

# Labels: 0 = Child, 1 = Adult
labels = np.array([0, 0, 0, 1, 1, 1, 0, 1, 0, 1])

# Split into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Build a simple Sequential ANN model
model = Sequential()
model.add(Dense(8, input_shape=(2,), activation='relu'))  # Input layer + hidden layer with 8 neurons
model.add(Dense(4, activation='relu'))  # Second hidden layer with 4 neurons
model.add(Dense(1, activation='sigmoid'))  # Output layer with 1 neuron for binary classification

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=0)


# Evaluate the model on test data
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {accuracy:.2f}")

# Make predictions on the test data
predictions = model.predict(X_test)
predictions = [1 if p > 0.5 else 0 for p in predictions]  # Convert probabilities to binary output (0 or 1)

# Display predictions and true labels
print(f"Predictions: {predictions}")
print(f"True Labels: {y_test.tolist()}")

