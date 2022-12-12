from math import isnan
import cv2 
import numpy as np
from serial import Serial

P_COSNTANT = 1.65    # Proportional controller for Sprint1 motor speed
IMG_WIDTH = 640     # Image width given from the Microsoft USB camera

def color_detection(red_bounds, green_bounds, blue_bounds, frame):
    """
    Create a binary image given the RGB bounds of the specified object.
    Args:
        red_bounds: A list of the lower and upper range of red values. First index is lower, second index is upper.
        green_bounds: A list of the lower and upper range of green values. First index is lower, second index is upper.
        blue_bounds: A list of the lower and upper range of blue values. First index is lower, second index is upper.
        frame: The camera frame to be analyzed.
    Returns:
        A Mat of the newly formed binary image
    """
    # Create a binary image using the RGB bounds for the red-orange test object
    binary_image = cv2.inRange(frame, (blue_bounds[0],green_bounds[0],red_bounds[0]), (blue_bounds[1],green_bounds[1],red_bounds[1]))
    return binary_image

def get_x_speed(bin_img):
    """
    Calculate the speed and direction to keep masked object in the center of the frame. 
    Args:
        bin_img: A Mat of a binary image.
    Returns:
        An int of the motor speed.
    """
    # Calculate the average x location of white pixels in the binary image
    avg_x = np.sum(np.where(bin_img==255)[1])/len(np.where(bin_img==255)[1])
    # By subtracting
    speed = ((IMG_WIDTH/2) - avg_x) / P_COSNTANT
    # If no white pixels are found, set speed to 0
    if isnan(speed):
        speed = 0
    print(speed)
    return int(speed)

def write_serial(info):
    """
    """
    serialPort = Serial('/dev/ttyACM0', 9600, timeout=1)    # Establishes Serial connection
    serialPort.write(bytes(str(info), 'utf8'))              # Writes String over Serial to Arduino

def main():
    """
    """
    camera = cv2.VideoCapture(2)    # Start video capture. Index 2 is the USB camera
    while camera.isOpened():
        ret, frame = camera.read()
        cv2.imshow("Frame", frame)
        red_bounds = [200, 255]
        green_bounds = [50, 100]
        blue_bounds = [50, 150]
        cv2.imshow("binary", color_detection(red_bounds, green_bounds, blue_bounds, frame))
        # Create a binary image using the RGB bounds for the red-orange test object
        binary_image = color_detection(red_bounds, green_bounds, blue_bounds, frame)
        # write_serial(get_x_speed(binary_image))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

main()