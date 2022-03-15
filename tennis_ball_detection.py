#
import cv2
import numpy as np

window_name = "HSV"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

image = cv2.imread("resources/tennis.jpeg")

im_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

low_hsv = np.array([23, 52, 155])
high_hsv = np.array([58, 255, 255])

mask = cv2.inRange(im_hsv, low_hsv, high_hsv)
mask_bgr = cv2.merge((mask, mask, mask))

contours_found = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = contours_found[1]

cv2.drawContours(mask_bgr, contours, 2, (0, 255, 0), 5)
ball = contours[2]
x, y, w, h = cv2.boundingRect(ball)
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("contours", mask_bgr)
cv2.imshow("original", image)
cv2.imshow(window_name, mask)

cv2.waitKey(0)
