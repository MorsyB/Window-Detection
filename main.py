import urllib.request
import cv2
from djitellopy import Tello
import numpy as np
import time

drone = Tello()
drone.connect()
print(drone.get_battery())
drone.takeoff()

center_offset = 80
takeoff_flag = False

def get_img():
    images = urllib.request.urlopen("http://192.168.1.175:8080/shot.jpg")
    imgNP = np.array(bytearray(images.read()), dtype=np.uint8)
    return cv2.imdecode(imgNP, -1)


def find_path(window_center, image_center):
    if window_center[0] - image_center[0] > center_offset:
        print("GO RIGHT")
        drone.move_right(20)
        time.sleep(2)
    elif window_center[0] - image_center[0] < -center_offset:
        print("GO LEFT")
        drone.move_left(20)
        time.sleep(2)
    elif window_center[1] - image_center[1] > center_offset:
        print("GO DOWN")
        drone.move_down(20)
        time.sleep(2)
    elif window_center[1] - image_center[1] < -center_offset:
        print("GO UP")
        drone.move_up(20)
        time.sleep(2)
    else:
        print("GO FORWARD")


def navigate():
    # cap = cv2.VideoCapture('video4.mp4')
    frames = []
    drone.streamon()
    #drone.takeoff()  # takeoff command
    time.sleep(5)
    drone.move_up(20)
    time.sleep(2)
    while True:
        # Read a frame
        # _, frame = cap.read()

        # Get the frame from the stream
        image = drone.get_frame_read().frame
        while image is None:
            image = drone.get_frame_read().frame
        time.sleep(0.1)

        # the center of the frame
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

            # Give orders to the drone
            find_path(center, centerIMG)

            # Show the image
            cv2.imshow("Frame", image)
            # Exit if the user presses the "q" key
            if cv2.waitKey(1) == ord("q"):
                break
            frames.append(image)
            time.sleep(0.1)


def new_Algo():
    drone.takeoff()
    drone.streamon()
    time.sleep(5)
    while True:
        image = drone.get_frame_read().frame
        cv2.imshow("Frame", image)
        cv2.waitKey(1)
        time.sleep(0.1)

    print("sleep is finished like cr7")
    drone.land()
    drone.streamoff()
    print("lsnding")


if __name__ == '__main__':
    #new_Algo()
    navigate()
