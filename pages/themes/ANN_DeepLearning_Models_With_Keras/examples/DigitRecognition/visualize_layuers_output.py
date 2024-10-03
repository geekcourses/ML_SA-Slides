import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input

# 1. Load MNIST data and prepare a single image
(X_train, _), (_, _) = mnist.load_data()
X_train = X_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0  # Reshape and normalize
single_image = X_train[0:1]  # Extract the first image for testing

# 2. Use the Functional API to define the model architecture
inputs = Input(shape=(28, 28, 1))  # Define the input layer
conv1 = Conv2D(32, (3, 3), activation='relu')(inputs)
maxpool1 = MaxPooling2D((2, 2))(conv1)
conv2 = Conv2D(64, (3, 3), activation='relu')(maxpool1)
model = Model(inputs=inputs, outputs=conv2)

# 3. Create a sub-model to get the output of the first convolutional layer
layer_outputs = Model(inputs=model.input, outputs=conv1)  # Focus on the first conv layer's output
feature_maps = layer_outputs.predict(single_image)  # Pass the image through the first conv layer

# 4. Plot the output feature maps
num_filters = feature_maps.shape[-1]  # Number of filters in the layer
plt.figure(figsize=(15, 15))
for i in range(num_filters):
    ax = plt.subplot(6, 6, i + 1)  # Create subplots in a 6x6 grid
    plt.imshow(feature_maps[0, :, :, i], cmap='viridis')  # Show each filter's output
    plt.axis('off')
    plt.title(f"Filter {i + 1}")
plt.suptitle("Feature Maps of First Convolutional Layer", fontsize=16)
plt.show()
