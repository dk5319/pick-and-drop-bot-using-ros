#include <Stepper.h>
const int stepsPerRevolution = 50;
const int rpm = 200;
Stepper myStepper = Stepper(stepsPerRevolution,4,5,6,7);
int pushButton = 12;
void rotate()
{  digitalWrite(24,HIGH);
  digitalWrite(22,HIGH);
  myStepper.step(4.2);
  delay(2000);
}
void setup(){
  myStepper.setSpeed(rpm);
  Serial.begin(9600);
  pinMode(22,OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(pushButton, INPUT_PULLUP);
  rotate();
}
void loop(){
    int buttonState = digitalRead(pushButton);
    Serial.println(buttonState);
    if (buttonState == 0){
      rotate();
    }
}
