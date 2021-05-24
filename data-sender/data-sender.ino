/*  Computer Hack! 
    Brightness Controller

    (C) License: GPL3-General Public License

    author: ashraf minhaj
    mail  : ashraf_minhaj@yahoo.com
*/

// define sensor pin (analog pin3)
int sensor_pin = A3;

void setup() {
  // set things here
  Serial.begin(9600);  // init serial communication at 9600 bps
}

void loop() {
  // mainloop
  int sensorValue = analogRead(sensor_pin); // read the input on analog pin A3:
  Serial.println(sensorValue);              // send data over serial
  
  delay(200);                               // a little delay to make things work better
}
