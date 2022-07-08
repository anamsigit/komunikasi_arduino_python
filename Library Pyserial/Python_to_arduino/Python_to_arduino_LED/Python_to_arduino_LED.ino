/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-serial-monitor
 */

int buzzer = 8;
int terimaserial = 0;

void setup() {
  Serial.begin(9600);
  pinMode(buzzer, OUTPUT); // set the digital pin as output:
}

void loop() {
  if(Serial.available()>0) {
    terimaserial = Serial.read();
    digitalWrite(buzzer, LOW);
  }
}
