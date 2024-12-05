import cv2
import numpy as np

# Load the image and the template
image = cv2.imread('res/sample_board.png')  # The larger image where you want to search
template = cv2.imread('res/snowball.png')  # The object you want to detect

# Convert images to grayscale (Template Matching works on grayscale images)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)

# Get the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Get the top-left corner of the match
top_left = max_loc

# Get the bottom-right corner of the match
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

# Draw a rectangle around the matched region
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# Display the image with the match
cv2.imshow('Template Matching', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

