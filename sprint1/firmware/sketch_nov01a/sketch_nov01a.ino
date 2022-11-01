#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
//create motorshield object and establish connection to motors
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *myMotor = AFMS.getMotor(3);

int tuneSpeed, tempSpeed = 0;
void setup() {
    AFMS.begin();
    Serial.flush();//resets serial monitor
    Serial.begin(9600);   
    myMotor->setSpeed(0); //sets initial speed of motors
    myMotor->run(FORWARD);
}

void loop() {
    if(Serial.available()){
        tempSpeed = Serial.parseInt();
        if (tempSpeed != 0) {
          tuneSpeed = tempSpeed;
        }
    }
    myMotor->setSpeed(tuneSpeed);
}
