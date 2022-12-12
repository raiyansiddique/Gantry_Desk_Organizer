from math import isnan
import cv2 
import numpy as np
from serial import Serial

P_COSNTANT = 1.65    # Proportional controller for Sprint1 motor speed
IMG_WIDTH = 640     # Image width given from the Microsoft USB camera

def color_detection(hue_bounds, sat_bounds, val_bounds, frame):
    """
    Create a binary image given the RGB bounds of the specified object.
    Args:
        hue_bounds: A list of the lower and upper range of hue values. First index is lower, second index is upper.
        sat_bounds: A list of the lower and upper range of saturation values. First index is lower, second index is upper.
        val_bounds: A list of the lower and upper range of values. First index is lower, second index is upper.
        frame: The camera frame to be analyzed.
    Returns:
        A Mat of the newly formed binary image
    """
    # Create a binary image using the RGB bounds for the hue-orange test object
    binary_image = cv2.inRange(frame, (hue_bounds[0],sat_bounds[0],val_bounds[0]), (hue_bounds[1],sat_bounds[1],val_bounds[1]))
    return binary_image

def draw_contour(bin_img):
    """
    """
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(bin_img,kernel,iterations = 1)
    contours = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    return contours

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

def nothing(x):
    pass

def get_contours(contours, frame, color: str):
    for cntr in contours:
        x,y,w,h = cv2.boundingRect(cntr)
        # Set minimum bound box size
        if (w*h > 15000):
            rect_x, rect_y = ((x+w/2), (y+h/2))
            rect_center = int(rect_x),int(rect_y)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, color, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.circle(frame, (rect_center), 4, (0, 255, 0), 2)


def main():
    """
    """
    camera = cv2.VideoCapture(2)    # Start video capture. Index 2 is the USB camera

    cv2.namedWindow('controls')
    cv2.createTrackbar('hue lower bound', 'controls', 0, 179, nothing)
    cv2.createTrackbar('hue upper bound', 'controls', 0, 179, nothing)
    cv2.createTrackbar('sat lower bound', 'controls', 0, 255, nothing)
    cv2.createTrackbar('sat upper bound', 'controls', 0, 255, nothing)
    cv2.createTrackbar('val lower bound', 'controls', 0, 255, nothing)
    cv2.createTrackbar('val upper bound', 'controls', 0, 255, nothing)


    while(camera.isOpened()):
        ret, frame = camera.read()
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        hue_bounds = [int(cv2.getTrackbarPos('hue lower bound','controls')), int(cv2.getTrackbarPos('hue upper bound','controls'))]
        sat_bounds = [int(cv2.getTrackbarPos('sat lower bound','controls')), int(cv2.getTrackbarPos('sat upper bound','controls'))]
        val_bounds = [int(cv2.getTrackbarPos('val lower bound','controls')), int(cv2.getTrackbarPos('val upper bound','controls'))]

        # Blue HSV Bounds
        b_hue_bounds = [85, 120]
        b_sat_bounds = [115, 220]
        b_val_bounds = [125, 255]

        # Purple HSV Bounds
        p_hue_bounds = [115, 140]
        p_sat_bounds = [75, 150]
        p_val_bounds = [30, 150]

        # Red HSV Bounds
        r_hue_bounds = [0, 10]
        r_sat_bounds = [185, 240]
        r_val_bounds = [170, 255]

        # Green HSV Bounds
        g_hue_bounds = [0, 179]
        g_sat_bounds = [190, 255]
        g_val_bounds = [60, 175]


        bin_image_list = ()

        # Create a binary image using the HSV bounds for the hue-orange test object
        # binary_image = cv2.inRange(frame, (hue_bounds[0],sat_bounds[0],val_bounds[0]), (hue_bounds[1],sat_bounds[1],val_bounds[1]))
        binary_image = color_detection(hue_bounds, sat_bounds, val_bounds, frame_HSV)
        purple_binary_image = color_detection(p_hue_bounds, p_sat_bounds, p_val_bounds, frame_HSV)
        blue_binary_image = color_detection(b_hue_bounds, b_sat_bounds, b_val_bounds, frame_HSV)
        green_binary_image = color_detection(g_hue_bounds, g_sat_bounds, g_val_bounds, frame_HSV)
        # black_binary_image = color_detection(k_red_bounds, k_green_bounds, k_blue_bounds, frame)
        red_binary_image = color_detection(r_hue_bounds, r_sat_bounds, r_val_bounds, frame_HSV)
        blue_contours = draw_contour(blue_binary_image)
        purple_contours = draw_contour(purple_binary_image)
        red_contours = draw_contour(red_binary_image)
        green_contours = draw_contour(green_binary_image)
        get_contours(blue_contours, frame, 'Blue')
        get_contours(purple_contours, frame, 'Purple')
        get_contours(red_contours, frame, 'Red')
        get_contours(green_contours, frame, 'Green')
        cv2.imshow("Frame", frame)
        cv2.imshow('binary', binary_image)
        # Close window
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

main()