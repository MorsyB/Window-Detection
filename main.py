import urllib.request
import cv2
import time
import numpy as np


def get_img():
    images = urllib.request.urlopen("http://192.168.1.175:8080/shot.jpg")
    imgNP = np.array(bytearray(images.read()), dtype=np.uint8)
    return cv2.imdecode(imgNP, -1)


def find_path(window_center, image_center):
    if window_center[0] - image_center[0] > 50:
        print("GO RIGHT")
    else:
        if window_center[0] - image_center[0] < -50:
            print("GO LEFT")
        else:
            if window_center[1] - image_center[1] > 50:
                print("GO Down")
            else:
                if window_center[1] - image_center[1] < -50:
                    print("GO up")
                else:
                    print("GO FORWARD")


def old_algo():
    cap = cv2.VideoCapture('video4.mp4')
    frames = []
    i = 0
    while True:
        # Read a frame
        _, frame = cap.read()
        # Load the image

        image = get_img()

        height, width = image.shape[:2]
        centerIMG = (int(width / 2), int(height / 2))

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Set the brightness threshold
        threshold = 180

        # Threshold the image
        _, binary_image = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # Find the largest contour
        if contours != ():
            largest_contour = max(contours, key=cv2.contourArea)

            # Draw a bounding box around the largest contour
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            center_x = x + w // 2
            center_y = y + h // 2
            center = (center_x, center_y)

            cv2.circle(image, center, 2, (255, 0, 0), -1)
            cv2.circle(image, centerIMG, 2, (255, 0, 0), -1)
            cv2.line(image, center, centerIMG, (255, 0, 0), 2)

            find_path(center, centerIMG)

            # Show the image
            cv2.imshow("Frame", image)
            time.sleep(0.02)

            # Exit if the user presses the "q" key
            if cv2.waitKey(1) == ord("q"):
                break
            frames.append(image)
            i += 1


if __name__ == '__main__':
    old_algo()
