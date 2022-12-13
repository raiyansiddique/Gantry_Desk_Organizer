#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

#define MAX_BUF               (64)                     // What is the longest message Arduino can store?
int steps;
const int stepPin = 10;
const int dirPin = 11;
char buffer[MAX_BUF];  // where we store the message until we get a ';'
int sofar;  // how much is in the buffer
char state;
String temp;
int pos = 0;    // variable to store the servo position
void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.flush();
  Serial.begin(9600); // Serial communication begin to read data

}

void loop() {
  // listen to serial commands
  while (Serial.available() > 0) {
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
        break;
      case 'b':
        //Forward Same Direction
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;
      case 'c':
        //Backward Same Direction
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;

      case 'd':
        //Diagonal_____ One Motor
        for (pos = 180; pos >= 95; pos -= 1) { // goes from 180 degrees to 0 degrees
          myservo.write(pos);              // tell servo to go to position in variable 'pos'
          delay(15);                       // waits 15 ms for the servo to reach the position
        }
        state = 'a';
        steps = 0;
        break;
      case 'e':
        for (pos = 95; pos <= 180; pos += 1) { // goes from 180 degrees to 0 degrees
          myservo.write(pos);              // tell servo to go to position in variable 'pos'
          delay(15);                       // waits 15 ms for the servo to reach the position
        }
        state = 'a';
        steps = 0;
        break;
      default:
        digitalWrite(stepPin, LOW);
    }
  }

}
