import cv2 
import numpy as np
def colorDetection():
    
def main():
    camera = cv2.VideoCapture(0)
    while camera.isOpened():
        ret, frame = camera.read()
        cv2.imshow("Frame", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

main()