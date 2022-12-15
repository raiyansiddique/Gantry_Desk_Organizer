#include <ezButton.h>

ezButton posX(5);  // create ezButton object that attach to pin 5;
ezButton negX(6);  // create ezButton object that attach to pin 6;
ezButton posY(7);  // create ezButton object that attach to pin 7;
ezButton negY(8);  // create ezButton object that attach to pin 8;
#define MAX_BUF               (64)                     // What is the longest message Arduino can store?
int steps;
const int stepPin = 3;
const int dirPin = 4;
const int stepPin1 = 10;
const int dirPin1 = 11;
char buffer[MAX_BUF];  // where we store the message until we get a new line
int sofar;  // how much is in the buffer
char state;
String temp;
void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);

  posX.setDebounceTime(50);
  negX.setDebounceTime(50);
  posY.setDebounceTime(50);
  negY.setDebounceTime(50);
  
  Serial.flush();
  Serial.begin(9600); // Serial communication begin to read data

}

void loop() {
    posX.loop();
    negX.loop();
    posY.loop();
    negY.loop();
  // listen to serial commands
  while (Serial.available() > 0) {
    steps = 0;
    char c = Serial.read();
    Serial.print(c); // Know that we got the message
    if (sofar < (MAX_BUF - 1)) {
      buffer[sofar++] = c;
    }
    if (c == '\n') {
      // entire message received
      buffer[sofar] = 0; // end the buffer so string functions work right
      state = buffer[0];

      temp = String(buffer);
      steps = temp.substring(1).toInt();
      buffer[0] = '\0';
      sofar = 0;
    }


    switch (state) {
      case 'a':
        //Stop running stepper motors
        digitalWrite(stepPin, LOW);
        digitalWrite(stepPin1, LOW);
        break;
      case 'b':
        //Forward Same Direction
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          posY.loop();
          if(posY.getState() == LOW){
            Serial.println("posY");
            state = 'a';
            break;
          }
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(700);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(700);
        }
        Serial.println("finished");
        break;
      case 'c':
        //Backward Same Direction
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          negY.loop();
          if(negY.getState() == LOW){
            Serial.println("negY");
            state = 'a';
            break;
          }
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(700);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(700);
        }
        Serial.println("finished");
        break;

      case 'd':
        //Diagonal_____ One Motor
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          posY.loop();
          if(posY.getState() == LOW){
            Serial.println("posY");
            state = 'l';
            break;
          }
          posX.loop();
          if(posX.getState() == LOW){
            Serial.println("posX");
            state = 'b';
            break;
          }
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(1000);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(1000);
        }
        Serial.println("finished");
        break;

      case 'e':
        //Diagonal ___ One Motor
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          posY.loop();
          if(posY.getState() == LOW){
            Serial.println("posY");
            state = 'm';
            break;
          }
          negX.loop();
          if(negX.getState() == LOW){
            Serial.println("negX");
            state = 'b';
            break;
          }
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(1000);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(1000);
        }
        Serial.println("finished");
        break;

      case 'f':
        //Diagonal ___ One Motor
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          negY.loop();
          if(negY.getState() == LOW){
            Serial.println("negY");
            state = 'l';
            break;
          }
          posX.loop();
          if(posX.getState() == LOW){
            Serial.println("posX");
            state = 'c';
            break;
          }
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(700);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(700);
        }
        Serial.println("finished");
        break;

      case 'g':
        //Diagnal ___ One Motor
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          negY.loop();
          if(negY.getState() == LOW){
            Serial.println("negY");
            state = 'm';
            break;
          }
          negX.loop();
          if(negX.getState() == LOW){
            Serial.println("negX");
            state = 'c';
            break;
          }
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(700);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(700);
        }
        Serial.println("finished");
        break;
      case 'h':
        //Gripper move stationary
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          posX.loop();
          if(posX.getState() == LOW){
            Serial.println("posX");
            state = 'a';
            break;
          }
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(700);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(700);
        }
        state = 'a';
        Serial.println("finished");
        break;

      case 'i':
        //Gripper move stationary
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          negX.loop();
          if(negX.getState() == LOW){
            Serial.println("negX");
            state = 'a';
            break;
          }
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(700);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(700);
        }
        state = 'a';
        Serial.println("finished");
        break;
      case 'j':
        //Forward Same Direction
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(1700);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(1700);
        }
        state = 'a';
        Serial.println("finished");
        break;
      case 'k':
        //Backward Same Direction
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(1700);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(1700);
        }
        state = 'a';
        Serial.println("finished");
        break;
      case 'l':
        //Gripper move stationary
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          posX.loop();
          if(posX.getState() == LOW){
            Serial.println("posX");
            state = 'a';
            break;
          }
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(1000);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(1000);
        }
        state = 'a';
        Serial.println("finished");
        break;

      case 'm':
        //Gripper move stationary
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          negX.loop();
          if(negX.getState() == LOW){
            Serial.println("negX");
            state = 'a';
            break;
          }
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(1000);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(1000);
        }
        state = 'a';
        Serial.println("finished");
        break;
      default:
        digitalWrite(stepPin, LOW);
        digitalWrite(stepPin1, LOW);
        state = state;

    }
  }

}
