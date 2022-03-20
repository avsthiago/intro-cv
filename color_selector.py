import click
import cv2
import numpy as np

window_name = "HSV"
low_h = 0
high_h = 179
low_s = 0
high_s = 255
low_v = 0
high_v = 255


def on_trackbar(_):
    global low_h, high_h, low_s, high_s, low_v, high_v
    low_h = cv2.getTrackbarPos("low_h", window_name)
    high_h = cv2.getTrackbarPos("high_h", window_name)
    low_s = cv2.getTrackbarPos("low_s", window_name)
    high_s = cv2.getTrackbarPos("high_s", window_name)
    low_v = cv2.getTrackbarPos("low_v", window_name)
    high_v = cv2.getTrackbarPos("high_v", window_name)


def resize_image(image, ratio):
    rows, cols, _ = image.shape
    return cv2.resize(image, (int(cols * ratio), int(rows * ratio)))


def create_trackbars():
    cv2.createTrackbar("low_h", window_name, 0, 179, on_trackbar)
    cv2.createTrackbar("high_h", window_name, 179, 179, on_trackbar)

    cv2.createTrackbar("low_s", window_name, 0, 255, on_trackbar)
    cv2.createTrackbar("high_s", window_name, 255, 255, on_trackbar)

    cv2.createTrackbar("low_v", window_name, 0, 255, on_trackbar)
    cv2.createTrackbar("high_v", window_name, 255, 255, on_trackbar)


def loop(image):
    while 1:
        im_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        low_hsv = np.array([low_h, low_s, low_v])
        high_hsv = np.array([high_h, high_s, high_v])
        print(low_hsv, high_hsv)
        mask = cv2.inRange(im_hsv, low_hsv, high_hsv)
        cv2.imshow(window_name, mask)
        cv2.waitKey(1)


@click.command()
@click.option("--path", default="resources/tennis.jpeg", help="Image path.")
@click.option("--image-ratio", default=0.8, help="Ratio of the image being displayed.")
def main(path, image_ratio):
    cv2.namedWindow(winname=window_name, flags=cv2.WINDOW_NORMAL)
    image = cv2.imread(path)
    image = resize_image(image, image_ratio)
    create_trackbars()

    cv2.imshow("original", image)
    loop(image)


if __name__ == "__main__":
    main()
