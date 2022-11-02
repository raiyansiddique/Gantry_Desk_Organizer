#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
//create motorshield object and establish connection to motors
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *myMotor = AFMS.getMotor(1);

int x = 50;
void setup() {
    AFMS.begin();
    Serial.flush();//resets serial monitor
    Serial.begin(9600);   
    Serial.setTimeout(10);
    myMotor->setSpeed(50); //sets initial speed of motors
    myMotor->run(FORWARD);
}

void loop() {
  while (!Serial.available());
      x = Serial.readString().toInt();
      if (x < 0) {
        myMotor->run(BACKWARD);
      } else
      {
        myMotor->run(FORWARD);
      }
      myMotor->setSpeed(x);
}
