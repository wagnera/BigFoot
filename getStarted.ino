 #include <DFRobotDFPlayerMini.h>

#include "Arduino.h"
#include "SoftwareSerial.h"

void play();
const int receive_pin = 8;
int val=0;

SoftwareSerial mySoftwareSerial(10, 11); // RX, TX
DFRobotDFPlayerMini myDFPlayer;


void setup()
{
  delay(20);
  mySoftwareSerial.begin(9600);
  delay(20);
  Serial.begin(115200);
  
  Serial.println();
  Serial.println(F("DFRobot DFPlayer Mini Demo"));
  Serial.println(F("Initializing DFPlayer ... (May take 3~5 seconds)"));
  
  if (!myDFPlayer.begin(mySoftwareSerial)) {  //Use softwareSerial to communicate with mp3.
    Serial.println(F("Unable to begin:"));
    Serial.println(F("1.Please recheck the connection!"));
    Serial.println(F("2.Please insert the SD card!"));
    //while(true);
  }
  Serial.println(F("DFPlayer Mini online."));
  delay(20);
  Serial.println("Setup Virtual wire");
  delay(100);
  //play();
  pinMode(8, INPUT);
  //attachInterrupt(digitalPinToInterrupt(8), play, CHANGE);
}

  
void loop()
{

   val = digitalRead(8);
   Serial.println(val);
   if (val == 1){
    play();
    delay(10000);
   }
   else{
    delay(100);
   }
}


void play(){
  myDFPlayer.volume(4);  //Set volume value. From 0 to 30
  myDFPlayer.play(1);  //Play the first mp3
  Serial.println("Playing");
}
