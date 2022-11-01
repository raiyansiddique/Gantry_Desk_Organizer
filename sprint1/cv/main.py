from math import nan
import cv2 
import numpy as np

P_COSNTANT = 1.25
IMG_WIDTH = 640

def color_detection(redBounds, greenBounds, blueBounds, frame):
    binary_image = cv2.inRange(frame, (blueBounds[0],greenBounds[0],redBounds[0]), (blueBounds[1],greenBounds[1],redBounds[1]))
    return binary_image

def get_x_coord(bin_img):
    avg_x = np.sum(np.where(bin_img==255)[1])/len(np.where(bin_img==255)[1])
    speed = ((IMG_WIDTH/2) - avg_x) / P_COSNTANT
    print(speed)
    # return speed
    # TODO: Add motor control



def main():
    camera = cv2.VideoCapture(2)
    while camera.isOpened():
        ret, frame = camera.read()
        cv2.imshow("Frame", frame)
        redBounds = [200, 255]
        greenBounds = [50, 100]
        blueBounds = [50, 150]
        cv2.imshow("binary", color_detection(redBounds, greenBounds, blueBounds, frame))
        binary_image = color_detection(redBounds, greenBounds, blueBounds, frame)
        get_x_coord(binary_image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

main()