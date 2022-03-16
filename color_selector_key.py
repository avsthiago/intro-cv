import cv2
import numpy as np

window_name = "HSV"


def on_trackbar(_):
    global low_h, high_h, low_s, high_s, low_v, high_v
    low_h = cv2.getTrackbarPos("low_h", window_name)
    high_h = cv2.getTrackbarPos("high_h", window_name)
    low_s = cv2.getTrackbarPos("low_s", window_name)
    high_s = cv2.getTrackbarPos("high_s", window_name)
    low_v = cv2.getTrackbarPos("low_v", window_name)
    high_v = cv2.getTrackbarPos("high_v", window_name)


image = cv2.imread("resources/frame_red.png")
dim = (600, 600)
image = cv2.resize(image, dim)

low_h = 0
high_h = 179
low_s = 0
high_s = 255
low_v = 0
high_v = 255

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

cv2.createTrackbar("low_h", window_name, 0, 179, on_trackbar)
cv2.createTrackbar("high_h", window_name, 179, 179, on_trackbar)

cv2.createTrackbar("low_s", window_name, 0, 255, on_trackbar)
cv2.createTrackbar("high_s", window_name, 255, 255, on_trackbar)

cv2.createTrackbar("low_v", window_name, 0, 255, on_trackbar)
cv2.createTrackbar("high_v", window_name, 255, 255, on_trackbar)

cv2.imshow("im_original", image)

while 1:
    im_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    low_hsv = np.array([low_h, low_s, low_v])
    high_hsv = np.array([high_h, high_s, high_v])

    print(low_hsv, high_hsv)

    mask = cv2.inRange(im_hsv, low_hsv, high_hsv)

    cv2.imshow(window_name, mask)

    cv2.waitKey(1)
