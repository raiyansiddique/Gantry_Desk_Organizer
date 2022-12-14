from math import isnan
import cv2 
import numpy as np
from serial import Serial
import time
class cvExpoMarker:

    def __init__(self):
        # self.P_COSNTANT = 1.65    # Proportional controller for Sprint1 motor speed
        self.found_object = False
        self.center_x = 0
        self.center_y = 0
        self.IMG_WIDTH = 640 + 45    # Image width given from the Microsoft USB camera
        self.IMG_HEIGHT = 480

    def color_detection(self, hue_bounds, sat_bounds, val_bounds, frame):
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

    def draw_contour(self, bin_img):
        """
        """
        kernel = np.ones((5,5),np.uint8)
        dilation = cv2.dilate(bin_img,kernel,iterations = 1)
        contours = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        return contours

    # def get_x_speed(self, bin_img):
    #     """
    #     Calculate the speed and direction to keep masked object in the center of the frame. 
    #     Args:
    #         bin_img: A Mat of a binary image.
    #     Returns:
    #         An int of the motor speed.
    #     """
    #     # Calculate the average x location of white pixels in the binary image
    #     avg_x = np.sum(np.where(bin_img==255)[1])/len(np.where(bin_img==255)[1])
    #     # By subtracting
    #     speed = ((self.IMG_WIDTH/2) - avg_x) / self.P_COSNTANT
    #     # If no white pixels are found, set speed to 0
    #     if isnan(speed):
    #         speed = 0
    #     print(speed)
    #     return int(speed)

    def nothing(x):
        pass

    def get_contours(self, contours , frame, color: str):
        for cntr in contours:
            x,y,w,h = cv2.boundingRect(cntr)
            # Set minimum bound box size
            if (w*h > 5000 and w*h < 9000):
                rect_x, rect_y = ((x+w/2), (y+h/2))
                rect_center = int(rect_x),int(rect_y)
                self.center_x = int(rect_x)
                self.center_y = int(rect_y)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(frame, color, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                cv2.circle(frame, (rect_center), 4, (0, 255, 0), 2)
                self.found_object = True
            elif self.found_object:
                self.found_object = False
    
    def center_gripper(self):
        if self.found_object == True:
            while (abs(self.center_x - self.IMG_WIDTH/2) > 100 and (abs(self.center_y - self.IMG_HEIGHT/2) > 100)):
                if(self.center_x - self.IMG_WIDTH/2 < 100):
                    # print("Move gripper left")
                    pass
                elif(self.center_x - self.IMG_WIDTH/2 > 100):
                    # print("Move gripper right")
                    pass
                elif(self.center_y - self.IMG_HEIGHT/2 < 100):
                    # print("Move toward steppers")
                    pass


# def getObject(serialPort):
#     gripperPort = Serial('/dev/ttyACM1', 9600, timeout=1)    # Establishes Serial connection 
#     xyPort = serialPort    # Establishes Serial connection 
#     time.sleep(5)
#     beam_state = gripperPort.readline().decode()
#     gripperPort.write(bytes(('e200' + '\n'), "utf8"))
#     time.sleep(2)
#     gripperPort.write(bytes(('c1500' + '\n'), "utf8"))
#     time.sleep(2)

#     xyPort.write(bytes(('b250' + '\n'), "utf8"))
#     gripperPort.write(bytes(('a' + '\n'), "utf8"))
#     output = xyPort.readline().decode()
#     beam_state = gripperPort.readline().decode()
#     while 'finished' not in output:
#         output = xyPort.readline().decode()
#         pass
#     gripperPort.write(bytes(('d100' + '\n'), "utf8"))
#     time.sleep(0.1)
#     gripperPort.write(bytes(('b1500' + '\n'), "utf8"))
#     time.sleep(4)
#     xyPort.write(bytes(('c10000' + '\n'), "utf8"))
#     time.sleep(5)
#     xyPort.write(bytes(('m10000' + '\n'), "utf8"))
#     time.sleep(4)
#     gripperPort.write(bytes(('c1500' + '\n'), "utf8"))
#     time.sleep(5)
#     gripperPort.write(bytes(('e200' + '\n'), "utf8"))

def main():
    """
    """
    visionSystem = cvExpoMarker()
    camera = cv2.VideoCapture(0)    # Start video capture. Index 2 is the USB camera


    cv2.namedWindow('controls')
    cv2.createTrackbar('hue lower bound', 'controls', 0, 179, visionSystem.nothing)
    cv2.createTrackbar('hue upper bound', 'controls', 0, 179, visionSystem.nothing)
    cv2.createTrackbar('sat lower bound', 'controls', 0, 255, visionSystem.nothing)
    cv2.createTrackbar('sat upper bound', 'controls', 0, 255, visionSystem.nothing)
    cv2.createTrackbar('val lower bound', 'controls', 0, 255, visionSystem.nothing)
    cv2.createTrackbar('val upper bound', 'controls', 0, 255, visionSystem.nothing)

    #serialPort = Serial('/dev/ttyACM0', 9600, timeout=1)    # Establishes Serial connection 
    #time.sleep(5)
    while(camera.isOpened()):
        

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
        g_hue_bounds = [50, 90]
        g_sat_bounds = [100, 255]
        g_val_bounds = [30, 255]



            
        ret, frame = camera.read()
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Create a binary image using the HSV bounds
        binary_image = visionSystem.color_detection(hue_bounds, sat_bounds, val_bounds, frame_HSV)
        #purple_binary_image = visionSystem.color_detection(p_hue_bounds, p_sat_bounds, p_val_bounds, frame_HSV)
        blue_binary_image = visionSystem.color_detection(b_hue_bounds, b_sat_bounds, b_val_bounds, frame_HSV)
        green_binary_image = visionSystem.color_detection(g_hue_bounds, g_sat_bounds, g_val_bounds, frame_HSV)
        #red_binary_image = visionSystem.color_detection(r_hue_bounds, r_sat_bounds, r_val_bounds, frame_HSV)


        # bin_image_list = [[binary_image, 'None'], [purple_binary_image, 'Purple'], [blue_binary_image, 'Blue'], [green_binary_image, 'Green'], [red_binary_image, 'Red']]
        
        visionSystem.get_contours(visionSystem.draw_contour(green_binary_image), frame, 'green')
        visionSystem.center_gripper()
        #visionSystem.get_contours(visionSystem.draw_contour(red_binary_image))
        # visionSystem.get_contours(visionSystem.draw_contour(blue_binary_image), frame, 'blue')
        #visionSystem.get_contours(visionSystem.draw_contour(purple_binary_image))  


        # serialPort.write(b'm200\n')
            

        # for bin in bin_image_list:
        #     visionSystem.get_contours(visionSystem.draw_contour(bin[0]), frame, bin[1])
        #     if visionSystem.found_object:
        #         print("Found")
        #         break
            
        cv2.imshow('frame', frame)
        cv2.imshow('bin', binary_image)
        # cv2.imshow('hsv', frame_HSV)
        # cv2.imshow('bin', binary_image)
        # Close window
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

main()