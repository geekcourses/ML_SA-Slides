# This will create a 4x6 image that represents the number 0, with red pixels for the lines of the number and white pixels for the background
import cv2
import numpy as np

# Create a blank image with white pixels
image = np.full((6, 4, 3), 255, dtype=np.uint8)

# Set the pixel values for the lines of the number 0 to red (255, 0, 0)
image[0, 0] = [255,0,0]
# image[0, 1] = [0,0,255]
# image[0, 2] = [0,0,255]
# image[0, 3] = [0,0,255]

# image[5, 0] = [255, 0, 0]
# image[5, 1] = [255, 0, 0]
# image[5, 2] = [255, 0, 0]
# image[5, 3] = [255, 0, 0]

# image[1:5, 0] = [255, 0, 0]
# image[1:5, 3] = [255, 0, 0]

# Save the image
cv2.imwrite('number_0.png', image)

print(image)
