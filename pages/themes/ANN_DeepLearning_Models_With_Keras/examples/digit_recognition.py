import tensorflow as tf
from tensorflow.keras import layers, models, Input
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess the data: reshape and normalize
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# Convert labels to categorical format
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the model using explicit Input layer
input_layer = Input(shape=(28, 28, 1))  # Input layer specifying the shape of the input

# First Conv2D layer: extracts features using 32 filters of size (3x3), ReLU activation
x = layers.Conv2D(32, (3, 3), activation='relu')(input_layer)

# MaxPooling2D layer: reduces the spatial dimensions (downsamples) by a factor of 2
x = layers.MaxPooling2D((2, 2))(x)

# Second Conv2D layer: deeper feature extraction using 64 filters of size (3x3), ReLU activation
x = layers.Conv2D(64, (3, 3), activation='relu')(x)

# Second MaxPooling2D layer: reduces spatial dimensions further
x = layers.MaxPooling2D((2, 2))(x)

# Third Conv2D layer: even deeper feature extraction using 64 filters
x = layers.Conv2D(64, (3, 3), activation='relu')(x)

# Flatten layer: converts 3D feature maps to 1D feature vectors for the dense layer
x = layers.Flatten()(x)

# Dense (fully connected) layer: learns high-level representations with 64 neurons
x = layers.Dense(64, activation='relu')(x)

# Output layer: 10 neurons for 10 digit classes, softmax activation for probability distribution
output_layer = layers.Dense(10, activation='softmax')(x)

# Create the model
model = models.Model(inputs=input_layer, outputs=output_layer)

# Compile the model using Adam optimizer and categorical cross-entropy loss
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model: use 20% of training data as validation, train for 5 epochs
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2)

# Evaluate the model on test data to measure accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc:.4f}')
