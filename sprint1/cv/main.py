import cv2 
import numpy as np
def colorDetection(redBounds, greenBounds, blueBounds, frame):
    binary_image = cv2.inRange(frame, (blueBounds[0],greenBounds[0],redBounds[0]), (blueBounds[1],greenBounds[1],redBounds[1]))
    return binary_image
def main():
    camera = cv2.VideoCapture(0)
    while camera.isOpened():
        ret, frame = camera.read()
        cv2.imshow("Frame", frame)
        redBounds = [200, 255]
        greenBounds = [50, 100]
        blueBounds = [50, 150]
        cv2.imshow("binary", colorDetection(redBounds, greenBounds, blueBounds, frame))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

main()