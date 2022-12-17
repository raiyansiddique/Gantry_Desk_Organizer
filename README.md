# Final Implementaton

## Description

For our final implmentation of our H-Bot Gantry system, 

## CV.py
This script establishes Serial connection to each Arduino used in our gantry system. Their is an Arduino that controls xy movement and an Arduino controlling the z axis and gripper servo.

This script also houses all computer vision code. For computer vision, we are completing color masking to locate Expo Markers in range of the gantry system.

## xy_gantry

In this folder, you will find the Arduino sketch for each directional case an H-Bot gantry can accomplish. Each case is mapped to a alphanumeric key and the number of steps you want to move in that direction.

## z_gripper

This folder has the Arduino sketch for control of the gripper mechanism on the xy gantry. Each case s mapped to a alphanumeric key and the number of steps you want to move in that direction.
