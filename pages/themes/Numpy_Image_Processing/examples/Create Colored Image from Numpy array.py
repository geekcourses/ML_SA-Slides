import cv2
import numpy as np

# Create a NumPy array with 3 channels (RGB) and a width and height of 5
array = np.zeros((5, 5, 3), dtype=np.uint8)

# Set the pixel values to create the number 2
# array[1, 1:4, :] = [0, 0, 0]
# array[2, 2, :] = [0, 0, 0]
# array[3, 1:4, :] = [0, 0, 0]
# array[4, 1, :] = [0, 0, 0]


# Fill the array with a green color
array[:, :, 1] = 255

# Set the central pixel to red
array[2, 2, 0] = 255

# Convert the NumPy array to a OpenCV image
img = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)

# Save the image
cv2.imwrite('image.png', img)

print(array)