import cv2
import numpy as np

cap = cv2.VideoCapture('resources/color_detection.mov')


def get_biggest_countour(mask):
    contours_found = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours_found[0]
    if contours is not None:
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
        if contour_sizes:
            return max(contour_sizes, key=lambda x: x[0])[1]
    return None


def detect_object(image):
    im_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([87, 102, 166])
    high_hsv = np.array([179, 255, 255])
    mask = cv2.inRange(im_hsv, low_hsv, high_hsv)
    biggest_contour = get_biggest_countour(mask)
    if biggest_contour is not None:
        x, y, w, h = cv2.boundingRect(biggest_contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    return image


# Read until video is completed
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Display the resulting frame
        frame = detect_object(frame)
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
