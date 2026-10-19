void setup () {
  //Definimos la led que usaremos, la cual estarà conectada al pin de salida correspondiente el número 13
  pinMode(13, OUTPUT);
}
void loop(){
  //Indicamos el bucle que seguirà la led, el cual consistirà en encenderse y apagarse alternativamente por intervales de 1 segundo.
  digitalWrite(13,HIGH);
  delay(1000);
  digitalWrite(13,LOW);
  delay(1000);
}