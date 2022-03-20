import cv2
import click

window_name = "threshold"
th_min = 15

def on_track(_):
    global th_min, th_max
    th_min = cv2.getTrackbarPos("threshold", window_name)

def resize_image(image, ratio):
    rows, cols = image.shape
    return cv2.resize(image, (int(cols * ratio), int(rows * ratio)))

def loop(image):
    previous_th = tuple()

    while True:
        current_th = th_min

        if current_th != previous_th:
            _, im_bin = cv2.threshold(image, th_min, 255, cv2.THRESH_BINARY)
            cv2.imshow(window_name, im_bin)
            previous_th = current_th
            print(previous_th)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break


@click.command()
@click.option("--path", default="resources/fire.png", help="Image path.")
@click.option("--image-ratio", default=1, help="Ratio of the image being displayed.")
def main(path, image_ratio):
    cv2.namedWindow(winname=window_name, flags=cv2.WINDOW_NORMAL)
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image = resize_image(image, image_ratio)    

    cv2.createTrackbar("threshold", window_name, 15, 255, on_track)
    cv2.imshow("original", image)
    loop(image)


if __name__ == "__main__":
    main()