# Project Description: Autonomous System for Window Detection
## Student 1: Morsy Biadsy     ID:318241221
## Student 2: Muhammad Awawdi  ID:209319003


### Goal:
The goal of this project is to develop an autonomous system that can detect windows using a Tello drone and navigate through them using computer vision techniques. This system will utilize advanced image processing algorithms to identify windows in a variety of environments and autonomously guide the drone through them.

The primary objectives of this project include:

1. Developing a robust computer vision model for window detection and recognition.
2. Implementing a navigation system that allows the drone to autonomously navigate through detected windows in a safe and efficient manner.
3. Evaluating the system effectiveness in terms of accuracy, safety, and reliability. By achieving these objectives, we aim to provide a proof-of-concept for a new type of aerial inspection and maintenance system.

### Algorithm:
The system converts each frame of the video stream to grayscale and applies a threshold to it, which results in a binary image. The binary image is then used to find the largest contour, which represents the window in the frame. The system then draws a bounding box around the largest contour, and calculates its center.
then, the drone moves in the direction of the object by using the find_path() function, which compares the object's center with the center of the frame and sends commands to the drone accordingly and navigates it through the window.

##### Main functions:

- open_stream() is a thread function that reads frames from the stream and applies the image processing steps on each frame.
- navigate() function starts the thread for opening the video stream and then reads frames from it, applies the image processing steps, and moves the drone accordingly using find_path() function.
- find_path() function is responsible for controlling the drone's movement based on the position of the object being tracked in the video stream.

#### Challenges:

- Strong winds: We had difficulty flying the drone outdoors due to strong winds that kept moving the drone off course. We had to reschedule outdoor testing and find a more sheltered location for the testing.
- Low light conditions: The image processing algorithm requires good lighting conditions to accurately detect windows. In low light conditions, the accuracy of the system decreased, and we had to modify the algorithm to account for this.
- Unexpected drone behavior in dark places: The drone behaved unexpectedly when flown in dark places due to the sensors attached to it.
- Limited testing locations: We had to select a place with low windows to reduce the risk of the drone crashing and make it easier to retrieve the drone if necessary.

Overall, despite the challenges we faced, we were able to develop a functional system that demonstrates the potential for using drones for window detection. Future work could focus on addressing the challenges we faced, such as improving the systems ability to operate in low light conditions and developing strategies for flying in areas with strong winds.

#### Team Members:
The project team consisted of:
Muhammad Awawdi and Morsy Biadsy, Computer Science students at the University of Haifa. They collaborated on the design, implementation, and testing of the autonomous window detection and navigation system.

#### Project Sponsor:
The project was sponsored by Professor Dan Feldman, who provided guidance throughout the project's development. Professor Feldman is a faculty member at the University of Haifa.

##### Conclusion:
In conclusion, the autonomous window detection and navigation system developed by the project team achieved the primary objective of detecting and navigating through windows using a Tello drone and computer vision techniques. However, the project encountered several challenges, including strong winds, low light conditions, and unexpected behavior of the drone in dark places. The project team addressed these challenges through rescheduling outdoor testing, modifying the image processing algorithm to account for low light conditions, and selecting a testing location with low windows to minimize the risk of damaging the drone. Despite these challenges, the system demonstrated promising results.
The project team would like to thank Professor Dan Feldman for his support and guidance throughout the project.
