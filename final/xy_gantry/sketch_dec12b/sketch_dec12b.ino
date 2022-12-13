#define MAX_BUF               (64)                     // What is the longest message Arduino can store?
int steps;
const int stepPin = 3;
const int dirPin = 4;
const int stepPin1 = 10;
const int dirPin1 = 11;
char buffer[MAX_BUF];  // where we store the message until we get a ';'
int sofar;  // how much is in the buffer
char state;
String temp;
void setup() {
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
  pinMode(stepPin1,OUTPUT); 
  pinMode(dirPin1,OUTPUT);
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
        digitalWrite(stepPin1, LOW);
        break;
      case 'b':
        //Forward Same Direction
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;
      case 'c':
        //Backward Same Direction
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;

      case 'd':
        //Diagonal_____ One Motor
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;

      case 'e':
        //Diagonal ___ One Motor
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;

      case 'f':
        //Diagonal ___ One Motor
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;

      case 'g':
        //Diagnal ___ One Motor
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;
      case 'h':
        //Gripper move stationary
        digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, LOW); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;

      case 'i':
        //Gripper move stationary
        digitalWrite(dirPin, LOW); // Enables the motor to move in a particular direction
        digitalWrite(dirPin1, HIGH); // Enables the motor to move in a particular direction
        for (int x = 0; x < steps; x++) {
          digitalWrite(stepPin, HIGH);
          digitalWrite(stepPin1, HIGH);
          delayMicroseconds(500);
          digitalWrite(stepPin, LOW);
          digitalWrite(stepPin1, LOW);
          delayMicroseconds(500);
        }
        state = 'a';
        steps = 0;
        break;
      default:
        digitalWrite(stepPin, LOW);
        digitalWrite(stepPin1, LOW);

    }
  }

}
