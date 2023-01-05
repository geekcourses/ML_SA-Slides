# This will create a 4x6 image that represents the number 0, with red pixels for the lines of the number and white pixels for the background
import cv2
import numpy as np

# Create a blank image 4x6 with white (255,255,255) pixels
image = np.full((6, 4, 3), 255, dtype=np.uint8)

### Set the pixel values for the lines of the number 0 to red BGR:( 0, 0, 255)

## Set Top line pixels to red ()
image[0, 0] = [0,0,255]
image[0, 1] = [0,0,255]
image[0, 2] = [0,0,255]
image[0, 3] = [0,0,255]

## Bottom line
image[5, 0] = [0,0,255]
image[5, 1] = [0,0,255]
image[5, 2] = [0,0,255]
image[5, 3] = [0,0,255]

## Left column
image[1:5, 0] = [0,0,255]

## Right Column
image[1:5, 3] = [0,0,255]

# Save the image
cv2.imwrite('number_0.png', image)

print(image)
