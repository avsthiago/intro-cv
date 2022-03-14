import cv2
import numpy as np

alpha_slider_max = 100
title_window = 'HSV'


def on_trackbar(_):
    global low_h, high_h, low_v, high_v, low_s, high_s, title_window
    low_h = cv2.getTrackbarPos("low h", title_window)
    high_h = cv2.getTrackbarPos("high h", title_window)
    low_s = cv2.getTrackbarPos("low s", title_window)
    high_s = cv2.getTrackbarPos("high s", title_window)
    low_v = cv2.getTrackbarPos("low v", title_window)
    high_v = cv2.getTrackbarPos("high v", title_window)


image = cv2.imread("resources/doge.jpg")
cv2.namedWindow(title_window, cv2.WINDOW_NORMAL)

# global
low_h = 0
high_h = 180
low_s = 0
high_s = 50
low_v = 0
high_v = 50

# H
cv2.createTrackbar("low h", title_window, 0, 360, on_trackbar)
cv2.createTrackbar("high h", title_window, 360, 360, on_trackbar)

# S
cv2.createTrackbar("low s", title_window, 0, 255, on_trackbar)
cv2.createTrackbar("high s", title_window, 255, 255, on_trackbar)

# V
cv2.createTrackbar("low v", title_window, 0, 255, on_trackbar)
cv2.createTrackbar("high v", title_window, 255, 255, on_trackbar)

cv2.imshow("original", image)

while 1:
    im_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_hsv = np.array([low_h, low_s, low_v], np.uint8)
    upper_hsv = np.array([high_h, high_s, high_v], np.uint8)

    mask = cv2.inRange(im_hsv, lower_hsv, upper_hsv)

    cv2.imshow(title_window, mask)

    cv2.waitKey(1)

