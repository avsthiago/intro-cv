import cv2
import numpy as np

image = cv2.resize(cv2.imread("resources/coins.jpg"), (500, 396))


def image_to_binary(image):
    im_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([0, 40, 0])
    high_hsv = np.array([179, 255, 255])
    return cv2.inRange(im_hsv, low_hsv, high_hsv)


def morphological_operations(mask):
    kernel = np.ones((5, 5), np.uint8)
    dilatation = cv2.dilate(mask, kernel, iterations=1)
    erosion = cv2.erode(dilatation, kernel, iterations=1)
    dilatation = cv2.dilate(erosion, kernel, iterations=1)
    erosion = cv2.erode(dilatation, kernel, iterations=1)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatation = cv2.dilate(erosion, kernel, iterations=2)
    erosion = cv2.erode(dilatation, kernel, iterations=15)
    return cv2.dilate(erosion, kernel, iterations=10)

if __name__ == "__main__":
    mask = image_to_binary(image)
    image_dil = morphological_operations(mask)

    dilatation_zeros = image_dil * 0
    mask_zeros = mask * 0

    merged_dilatation = cv2.merge([dilatation_zeros, dilatation_zeros, image_dil])
    merged_mask = cv2.merge([mask_zeros, mask, mask_zeros])
    final_result = cv2.add(merged_dilatation, merged_mask)

    cv2.imshow("merged dilatation", merged_dilatation)
    cv2.imshow("mask", merged_mask)
    cv2.imshow("dilatation and mask", final_result)

    cv2.waitKey(0)
