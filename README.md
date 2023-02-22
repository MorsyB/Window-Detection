# Window-Detection
## Student 1: Morsy Biadsy     ID:318241221
## Student 2: Muhammad Awawdi  ID:209319003

# Goal:
The goal of this project is to develop an autonomous system that can detect windows using a Tello drone and navigate through them using computer vision techniques. This system will utilize advanced image processing algorithms to identify windows in a variety of environments and autonomously guide the drone through them. By achieving this goal, the system will contribute to the development of new technologies for aerial navigation, as well as provide a practical solution for inspecting and maintaining windows in buildings and other structures.

The primary objectives of this project include:

1. Developing a robust computer vision model for window detection and recognition.
2. Implementing a navigation system that allows the drone to autonomously navigate through detected windows in a safe and efficient manner.
3. Evaluating the system's effectiveness in terms of accuracy, safety, and reliability.
By achieving these objectives, we aim to provide a proof-of-concept for a new type of aerial inspection and maintenance system.

### Algorithm
The Algorithm uses the following steps:

1. Connect to the drone and take off.
2. Open the video stream from the drone and start reading frames.
3. For each frame, convert it to grayscale and threshold it.
4. Find the largest contour in the binary image.
5. Draw a bounding box around the largest contour, and calculate its center.
6. Move the drone in the direction of the object by using the find_path() function, which compares the object's center with the center of the frame, and sends commands to the drone accordingly.
7. After the drone reaches the object, it flies towards it by moving forward, then lands.
##### Main functions:

- get_img() function retrieves the image from the video stream.
- open_stream() is a thread function that reads frames from the stream, and applies the image processing steps on each frame.
- navigate() function starts the thread for opening the video stream, and then reads frames from it, applies the image processing steps and moves the drone accordingly using find_path() function.
- find_path() function is responsible for controlling the drone's movement based on the position of the object being tracked in the video stream.
