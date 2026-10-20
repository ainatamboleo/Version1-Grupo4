#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); 
unsigned long nextMillis = 500;
const int ledVerdeTierra = 13;
void setup() {
   Serial.begin(9600);
   //Empieza la recepción de los datos:
   mySerial.begin(9600);
   pinMode(ledVerdeTierra, OUTPUT);
}
void loop() {
   //Creamos un código para comprobar que recibe correctamente los datos proporcionados:
   if (mySerial.available()) {
      String data = mySerial.readString();
      digitalWrite(ledVerdeTierra, HIGH);
      delay(100);
      digitalWrite(ledVerdeTierra, LOW);
      Serial.print(data);
      mySerial.println("Ok");
   }
  
   //Cogemos la orden dada desde los botones en la interfaz de Python y la enviamos al Arduino transmisor:
   if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n'); 
    data.trim(); 

    if (data == "Parar" || data == "Reanudar" || data == "Inicio") {
      mySerial.println(data);
}
   }
}
