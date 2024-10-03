import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, Input

# 1. Load MNIST data and prepare a single image
(X_train, _), (_, _) = mnist.load_data()
X_train = X_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0  # Reshape and normalize
single_image = X_train[0:1]  # Extract the first image for testing

# 2. Define a single convolutional layer model
inputs = Input(shape=(28, 28, 1))  # Input layer for grayscale image
conv1 = Conv2D(1, (3, 3), activation='relu', use_bias=False)(inputs)  # Single filter, no bias
model = Model(inputs=inputs, outputs=conv1)

# 3. Create a custom vertical line filter and reshape to (3, 3, 1, 1)
vertical_filter = np.array([[1, 0, -1],
                            [1, 0, -1],
                            [1, 0, -1]], dtype=np.float32).reshape(3, 3, 1, 1)

# 4. Set the custom filter to the first convolutional layer
model.layers[1].set_weights([vertical_filter])

# 5. Pass the image through the model to get the feature map
feature_map = model.predict(single_image)

# 6. Plot the feature map
plt.imshow(feature_map[0, :, :, 0], cmap='viridis')  # Visualize the feature map for the single filter
plt.axis('off')
plt.title("Feature Map for Custom Vertical Line Filter")
plt.show()
