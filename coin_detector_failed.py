# [ 0 40  0] [179 255 255]

import cv2
import numpy as np

image = cv2.imread("resources/coins.jpg")

image = cv2.resize(image, (500, 396))

im_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

low_hsv = np.array([0, 40, 0])
high_hsv = np.array([179, 255, 255])

mask = cv2.inRange(im_hsv, low_hsv, high_hsv)

# erosion
kernel = np.ones((5, 5), np.uint8)
dilatation = cv2.dilate(mask, kernel, iterations=1)
erosion = cv2.erode(dilatation, kernel, iterations=1)
dilatation = cv2.dilate(erosion, kernel, iterations=1)
erosion = cv2.erode(dilatation, kernel, iterations=1)
# kernel = np.ones((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
dilatation = cv2.dilate(erosion, kernel, iterations=2)
erosion = cv2.erode(dilatation, kernel, iterations=15)
dilatation = cv2.dilate(erosion, kernel, iterations=10)

dilatation_zeros = dilatation * 0
mask_zeros = mask * 0

merged_dilatation = cv2.merge([dilatation_zeros,  dilatation_zeros, dilatation])
merged_mask = cv2.merge([mask_zeros,  mask, mask_zeros])

final_result = merged_dilatation + merged_mask

cv2.imshow("coins", mask)
cv2.imshow("coins_dilatation", merged_dilatation)
cv2.imshow("coins_mask", merged_mask)
cv2.imshow("coins_final", final_result)

cv2.waitKey(0)
