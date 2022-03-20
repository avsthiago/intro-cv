import cv2

alpha_slider_max = 100
title_window = "Linear Blend"


def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = 1.0 - alpha
    dst = cv2.addWeighted(img1, alpha, img2, beta, 0.0)
    cv2.imshow(title_window, dst)


def read_images(path_img1, path_img2):
    img1 = cv2.imread(path_img1)
    img2 = cv2.imread(path_img2)
    return img1, cv2.resize(img2, img1.shape[::-1][1:])


def create_trackbar():
    trackbar_name = f"Alpha x {alpha_slider_max}"
    cv2.createTrackbar(trackbar_name, title_window, 0, alpha_slider_max, on_trackbar)


if __name__ == "__main__":
    path_img1 = "resources/doge.jpg"
    path_img2 = "resources/opencv.jpg"
    img1, img2 = read_images(path_img1, path_img2)
    cv2.namedWindow(title_window)
    create_trackbar()

    cv2.waitKey(0)
