import cv2
import numpy as np

window_name = "coins"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

image_original = cv2.imread("resources/coins.jpg", -1)
image_original = cv2.resize(image_original, (500, 396))
image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)


def get_trackbar_value(trackbar_name):
    value = cv2.getTrackbarPos(trackbar_name, window_name)
    return value if value > 0 else 1


def on_trackbar(_):
    global dp, min_dist, param1, param2, min_radius, max_radius
    dp = get_trackbar_value("dp")
    min_dist = get_trackbar_value("min_dist")
    param1 = get_trackbar_value("param1")
    param2 = get_trackbar_value("param2")
    min_radius = get_trackbar_value("min_radius")
    max_radius = get_trackbar_value("max_radius")


cv2.createTrackbar("dp", window_name, 1, 5, on_trackbar)
cv2.createTrackbar("min_dist", window_name, 15, 50, on_trackbar)
cv2.createTrackbar("param1", window_name, 50, 150, on_trackbar)
cv2.createTrackbar("param2", window_name, 20, 100, on_trackbar)
cv2.createTrackbar("min_radius", window_name, 10, 100, on_trackbar)
cv2.createTrackbar("max_radius", window_name, 50, 100, on_trackbar)

dp = 1
min_dist = 15
param1 = 50
param2 = 20
min_radius = 10
max_radius = 50


def detect_circles(image):
    return cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dp=dp, minDist=min_dist,
                            param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)


def draw_circles(image, circles):
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
    return image


def put_text(image, text):
    return cv2.putText(image, text, (250, 350), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=3, color=(255, 0, 0))


previous_parameters = tuple()

while True:
    current_parameters = (dp, min_dist, param1, param2, min_radius, max_radius)

    if previous_parameters != current_parameters:
        print(current_parameters)

        circles = detect_circles(image_gray)
        current_image = image_original.copy()
        image = draw_circles(current_image, circles)
        text = f"Detections: {len(circles[0])}"
        put_text(current_image, text)
        cv2.imshow(window_name, image)
        previous_parameters = current_parameters

    cv2.waitKey(1)
