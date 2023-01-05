import cv2

image_ori = cv2.imread('number_0.png')

# Convert the BGR image to grayscale:
image_gray = cv2.cvtColor(image_ori, cv2.COLOR_BGR2GRAY)

# Show the images:
cv2.imshow('Original image',image_ori)
cv2.imshow('Gray image', image_gray)

# Destroy windows with images once the user pressed a key
cv2.waitKey(0)
cv2.destroyAllWindows()