int x;
String temp = "0000";
int state = 1;
int steps = 1000;
const int stepPin = 3; 
const int dirPin = 4; 
const int stepPin1 = 10; 
const int dirPin1 = 11; 


void setup() {
    Serial.flush();//resets serial monitor
    Serial.begin(9600);   
    Serial.setTimeout(10);
    pinMode(stepPin,OUTPUT); 
    pinMode(dirPin,OUTPUT);
    pinMode(stepPin1,OUTPUT); 
    pinMode(dirPin1,OUTPUT);
}

void loop() {
  if (!Serial.available()){
      state = Serial.read();
      Serial.println(state);
  
  switch(state) {
    case 1:
    //Stop running stepper motors
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,LOW); 
          if (!Serial.available()){
           x = Serial.parseInt();
            Serial.println(x);
         }
    case 2:
    //Forward Same Direction
      digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
      digitalWrite(dirPin1,HIGH); // Enables the motor to move in a particular direction
      for(int x = 0; x < steps; x++) {
        digitalWrite(stepPin,HIGH); 
        digitalWrite(stepPin1,HIGH);
        delayMicroseconds(500); 
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,LOW); 
        delayMicroseconds(500); 
      }
    case 3:
    //Backward Same Direction
      digitalWrite(dirPin,LOW); // Enables the motor to move in a particular direction
      digitalWrite(dirPin1,LOW); // Enables the motor to move in a particular direction
      for(int x = 0; x < steps; x++) {
        digitalWrite(stepPin,HIGH); 
        digitalWrite(stepPin1,HIGH);
        delayMicroseconds(500); 
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,LOW); 
        delayMicroseconds(500); 
      }

    case 4:
    //Diagonal_____ One Motor
      digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
      digitalWrite(dirPin1,HIGH); // Enables the motor to move in a particular direction
      for(int x = 0; x < steps; x++) {
        digitalWrite(stepPin,HIGH); 
        digitalWrite(stepPin1,LOW);
        delayMicroseconds(500); 
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,LOW); 
        delayMicroseconds(500); 
      }

    case 5:
    //Diagonal ___ One Motor
       digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
      digitalWrite(dirPin1,HIGH); // Enables the motor to move in a particular direction
      for(int x = 0; x < steps; x++) {
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,HIGH);
        delayMicroseconds(500); 
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,LOW); 
        delayMicroseconds(500); 
      }

    case 6:
     //Diagonal ___ One Motor
      digitalWrite(dirPin,LOW); // Enables the motor to move in a particular direction
      digitalWrite(dirPin1,LOW); // Enables the motor to move in a particular direction
      for(int x = 0; x < steps; x++) {
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,HIGH);
        delayMicroseconds(500); 
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,LOW); 
        delayMicroseconds(500); 
      }

    case 7:
     //Diagnal ___ One Motor
      digitalWrite(dirPin,LOW); // Enables the motor to move in a particular direction
      digitalWrite(dirPin1,LOW); // Enables the motor to move in a particular direction
      for(int x = 0; x < steps; x++) {
        digitalWrite(stepPin,HIGH); 
        digitalWrite(stepPin1,LOW);
        delayMicroseconds(500); 
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,LOW); 
        delayMicroseconds(500); 
      }
    case 8:
    //Gripper move stationary
      digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
      digitalWrite(dirPin1,LOW); // Enables the motor to move in a particular direction
      for(int x = 0; x < steps; x++) {
        digitalWrite(stepPin,HIGH); 
        digitalWrite(stepPin1, HIGH);
        delayMicroseconds(500); 
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,LOW); 
        delayMicroseconds(500); 
      }

    case 9:
    //Gripper move stationary
      digitalWrite(dirPin,LOW); // Enables the motor to move in a particular direction
      digitalWrite(dirPin1,HIGH); // Enables the motor to move in a particular direction
      for(int x = 0; x < steps; x++) {
        digitalWrite(stepPin,HIGH); 
        digitalWrite(stepPin1,HIGH);
        delayMicroseconds(500); 
        digitalWrite(stepPin,LOW); 
        digitalWrite(stepPin1,LOW); 
        delayMicroseconds(500); 
      }
  }}

}
