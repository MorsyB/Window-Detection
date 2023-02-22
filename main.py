import urllib.request
import cv2
from djitellopy import Tello
import numpy as np
import time
import threading

drone = Tello()
drone.connect()
print(drone.get_battery())
drone.takeoff()

center_offset = 80

show_box = True
landed = False
image = None
lock = False
counter = 0


def get_img():
    images = urllib.request.urlopen("http://192.168.1.189:8080/shot.jpg")
    imgNP = np.array(bytearray(images.read()), dtype=np.uint8)
    return cv2.imdecode(imgNP, -1)


def open_stream():
    global show_box
    global image
    gray_images = []
    frames = []
    while True:
        # Get the frame from the stream
        image = drone.get_frame_read().frame

        while image is None:
            image = drone.get_frame_read().frame

        # the center of the frame
        height, width = image.shape[:2]
        centerIMG = (int(width / 2), int(height / 2))

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Set the brightness threshold
        threshold = 180

        # Threshold the image
        _, binary_image = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        gray_images.append(binary_image)

        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # Find the largest contour
        if contours != ():
            largest_contour = max(contours, key=cv2.contourArea)

            # Draw a bounding box around the largest contour
            x, y, w, h = cv2.boundingRect(largest_contour)
            center_x = x + w // 2
            center_y = y + h // 2
            center = (center_x, center_y)
            if show_box:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(image, center, 2, (255, 0, 0), -1)
                cv2.circle(image, centerIMG, 2, (255, 0, 0), -1)
                cv2.line(image, center, centerIMG, (255, 0, 0), 2)

            # Give orders to the drone
            # Show the image
            cv2.imshow("Frame", image)
            frames.append(image)
            # Exit if the user presses the "q" key
            if cv2.waitKey(1) == ord("q"):
                break
            if landed:
                break
            time.sleep(0.1)
    print("saving images...")
    frame_num = 0
    for frame in frames:
        cv2.imwrite(f'Frames/frame{frame_num}.jpg', frame)
        frame_num += 1
    frame_num = 0
    for frame in gray_images:
        cv2.imwrite(f'GrayImages/frame{frame_num}.jpg', frame)
        frame_num += 1


def find_path(window_center, image_center):
    global show_box
    global landed
    if window_center[0] - image_center[0] > center_offset:
        print("GO RIGHT")
        drone.move_right(30)
    elif window_center[0] - image_center[0] < -center_offset:
        print("GO LEFT")
        drone.move_left(30)
    elif window_center[1] - image_center[1] > center_offset:
        print("GO DOWN")
        drone.move_down(30)
    elif window_center[1] - image_center[1] < -210:
        print("GO UP")
        drone.move_up(30)
    else:
        for i in range(7):
            drone.move_forward(80)
            print("GO FORWARD")
            show_box = False
            time.sleep(2)
        drone.land()
        landed = True
        print("Drone Landed!")
    time.sleep(3)


def navigate():
    # cap = cv2.VideoCapture('video4.mp4')
    global show_box
    drone.streamon()
    my_thread = threading.Thread(target=open_stream)
    my_thread.start()
    time.sleep(3)
    drone.move_up(30)
    while True:
        # Get the frame from the stream

        while image is None:
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
            center_x = x + w // 2
            center_y = y + h // 2
            center = (center_x, center_y)

            find_path(center, centerIMG)
            time.sleep(0.5)
        if not show_box:
            break


if __name__ == '__main__':
    navigate()
    # drone_live_stream()


def drone_live_stream():
    drone.streamon()
    while True:
        image = drone.get_frame_read().frame
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

            center_x = x + w // 2
            center_y = y + h // 2
            center = (center_x, center_y)

            if show_box:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(image, center, 2, (255, 0, 0), -1)
                cv2.circle(image, centerIMG, 2, (255, 0, 0), -1)
                cv2.line(image, center, centerIMG, (255, 0, 0), 2)

            # Show the image
            cv2.imshow("Frame", image)
            # Exit if the user presses the "q" key
            if cv2.waitKey(1) == ord("q"):
                break
            time.sleep(0.1)

