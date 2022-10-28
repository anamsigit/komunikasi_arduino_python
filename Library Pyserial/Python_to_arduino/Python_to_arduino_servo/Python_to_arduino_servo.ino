#include <Servo.h>
Servo motorServo; 
int x;
void setup()
{
   motorServo.attach(11); // servo Pada Pin digital 10, coklat = GND, kuning data, merah = 5v
   Serial.begin(250000);
//   Serial.begin(9600);
   Serial.setTimeout(1);
}

void loop()
//{
//   while (!Serial.available());
//     x = Serial.readString().toInt();
//     if (x > 20 && x < 160){
//      motorServo.write(x);
//     }  
//}

{
   while (!Serial.available());
     x = Serial.readString().toInt();
     motorServo.write(x);     
}


//void loop() {
//  if(Serial.available() > 0) {
//    char data = Serial.read();
//    char str[2];
//    str[0] = data;
//    str[1] = '\0';
//    x = int(data);
//    motorServo.write(x);
//  }
//}
