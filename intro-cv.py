import cv2

alpha_slider_max = 100
title_window = 'Linear Blend'


def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = (1.0 - alpha)
    dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
    cv2.imshow(title_window, dst)


src1 = cv2.imread("resources/doge.jpg")
src2 = cv2.imread("resources/opencv.jpg")

src2 = cv2.resize(src2, src1.shape[::-1][1:])


cv2.namedWindow(title_window)
trackbar_name = f'Alpha x {alpha_slider_max}'
cv2.createTrackbar(trackbar_name, title_window, 0, alpha_slider_max, on_trackbar)
on_trackbar(0)

cv2.waitKey(0)
