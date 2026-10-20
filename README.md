# Version-1-Grupo-4
## PASO 1
Este paso fue el inicio de nuestro proyecto. Consistía en conectar una led roja para dejarla encendida. Luego también jugamos con los puntos de conexión de la led para poderla encender y apagar dependiendo del pin de salida al cual iba conectada.
En este caso, usamos el siguiente còdigo: 
```C
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
```
## PASO 2
El segundo paso también trataba sobre conectar leds pero con más complejidad que el primero. En primer lugar tuvimos que montar una led roja y una amarilla y crear un programa que hiciera que estas parpadeasen cada uno con un intervalo determinado. Para aconseguir esto usamos el siguiente código:
```C
//Definimos los leds (led 7 = rojo, led 8 = amarillo).
const int led1 = 7;
const int led2 = 8; 
//Asignamos el tiempo durante el cual se mantendrà cada led encendida. En nuestro caso, quisimos que fuesen intervalos de 1 segundo alternandose.
int nextMillis1;
int nextMillis2;
const long interval1 = 1000;
const long interval2 = 1000; 
//Como queremos que no esten nunca en el mismo estado, tenemos que hacer que empiezen en estados diferentes.
bool stateLed1 = HIGH;
bool stateLed2 = LOW;
void setup() {
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    //Dejamos constancia de cuando habrà que cambiar los primeros intervalos.
    nextMillis1 = millis() + interval1;
    nextMillis2 = millis() + interval2;
}
void loop() {
    //Control del led en el pin 7
    if (millis() >= nextMillis1) {
        //Asignamos el cambio.
        if (stateLed1 == HIGH)
             stateLed1 = LOW;
        else
             stateLed1 = LOW;
        digitalWrite(led1, stateLed1);
        //Dejamos contancia del siguiente instante en el cual habrà que cambiar.
        nextMillis1 = millis() + interval1;
    }
    //Control del led en el pin 8
    if (millis() >= nextMillis2) {
       if (stateLed2 == LOW)
             stateLed2 = HIGH;
        else
             stateLed2 = LOW;
        digitalWrite(led2, stateLed2);
        nextMillis2 = millis() + interval2;
    }
}
```
## PASO 3
El paso 3 era de gran importancia ya que tuvimos que asegurar que la comunicación entre nuestra placa Arduino y nuestrfo portátil fuese correcta. Para asegurarnos, tuvimos que usar como modelo el siguiente código:
```C
int i=0;
void setup() {
   Serial.begin(9600);
}
void loop() {
   Serial.println(i);
   i++;
   delay(1000);
}
```
Sin embargo, luego teníamos que modificar lo escrito para que se mande la señal de enviar 'Aun sigo aquí' cada 10 segundos, el resultado final fue:
```C
String i = "Aun sigo aquí";
void setup() {
   Serial.begin(9600);
}
void loop() {
   Serial.println(i);
   delay(1000);
}
```
## PASO 4
Para hacer este paso necesitamos incorporar un nuevo elemento en nuestra placa de leds y cables; un sensor de temperatura. Aunque luego tuvimos que añadir funciones más complejas, en el paso 4 solo tuvimos que comprobar que los datos recolectados por el sensor llegasen cada X timepo a nuestro ordenador. Para efectuar esto tuvimos que usar lo siguiente:
//Definiciones necesarias para usar el sensor de temperatura adecuadamente:
```C
#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
void setup() {
   Serial.begin(9600);
   //Iniciamos el sensor.
   dht.begin();
}
void loop() {
   delay(2000);
   float h = dht.readHumidity();
   float t = dht.readTemperature();
   //Creamos un código que muestre en la pantalla un error si los datos que està recolectando el sensor son nulos.
   if (isnan(h) || isnan(t))
      Serial.println("Error al leer el sensor DHT11");
   else {
      Serial.print("Humedad: ");
      Serial.print(h);
      Serial.print("%\t");
      Serial.print("Temperatura: ");
      Serial.print(t);
      Serial.println("°C");
   }
}
```
## PASO 5
El paso 5 consistía en crear un código que verificarà si el sensor de temperatura estaba captando datos correctamente. En este apartado, decicidmos crear una carpeta con los diferentes leds, sensor y otro material con el que habíamos trabajado para poder efectuar los códigos por separadado y, en caso de que uno falle poder detectar con inmediatez de cual se trataba.
## PASO 6
En este paso tuvimos que estblecer la conexión entre dos arduinos unidos por 3 cables. El objetivo era que uno de los arduinos fuese el transmisor de los datos mientras que el otro tuviera la fuanción de recibirlos e mostrarlos en el ordenador. Empezamos con crear un programa qaue conectase los dos arduinos con la finalidad que la frase 'Empezamos la recepción' passarà de la placa transmisora y se mostrara en el Serial Monitor de la placa receptora:
```C
//Incluimos librerías necesarias.
#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX (azul, naranja)
unsigned long nextMillis = 500;
//Asignamos la frase que deseamos que se muestre en el arduino receptor.
void setup() {
   Serial.begin(9600);
   Serial.println("Empezamos la recepción");
   mySerial.begin(9600);
}
void loop() {
   if (mySerial.available()) {
      String data = mySerial.readString();
      Serial.print(data);
   }
}
```
## PASO 7
Este paso consistía en asegurarse, no solamente de que nuestro arduino transmisor estuviera enviando datos sino que nuestro arduino receptos los estuviera captando correctamente. Para poder efectuar este paso necesitamos:
```C
//Le indicamos al programa que usando la placa identificada como COM3 nos envie repetidamente una verificación de que nuestros mensajes se envien correctamente a la placa receptor arduino.
import serial
device = 'COM3'
mySerial = serial.Serial(device, 9600)
while True:
   if mySerial.in_waiting > 0:
      linea = mySerial.readline().decode('utf-8').rstrip()
      print(linea)
```
Para poder usar "mySerial" nos tuvimos que instalar ciertas librerías.
## PASO 8
En este caso, una vez establecida la conexión entre arduinos, nos teníamos que plantear la situación que el arduino conectado al sensor era el satelite mientras que el otro arduino, el arduino tierra, recibia esos datos colectados cada 3 segundos. Además tuvimos que conectar una led verde a cada uno de los arduinos. El led verde conectado al arduino satelite tenía que encenderse brevemente cada vez que este enviara datos, mientras que el led verde tierra tenía que hacerlo cada vez que los recibía. 
(Afegir codi)
## PASO 9
Para hacer este paso tuvimos que simplificar la manera en la que el arduino satelite enviaba los datos al arduino tierra, ya que nuestro objetivo era crear una gráfica que mostrara los valores de humedad y temperatura dependiendo del tiempo, en el cual 0 se considerabq cuando empezaba el programa.
Para desarrollar este paso tuvimos que instalar la librería matplotlib. Este fue el resultado: 
(Afegir codi)
## PASO 10 y PASO 11
Para efectuar este paso tuvimos que usar la librería Tinker, la cual consistia en facilitar la interaccion del programa de Python y el usuario. Esto se hacía mediante el siguiente código:
(Afegir codi)
Como podemos ver desde aquí hemos programado 3 botones con los que el usuario puede interactuar con la gràfica. En primer lugar aparece el botón de INICIAR, el cual el usuario tiene que clicar para que la gráfica se ponga en marcha. Para parar la gráfica y que deje de recopilar datos tuvimos que añadir el botón de PARAR. Finalmente, el botón REANUDAR se encargaba de volver a ejecutar la gráfica después de usar el botón de PARAR. El código usado para definir cada uno de los botones es el siguiente:
(Afegir codi)
## PASO 12
En este paso tuvimos que juntar la interfaz con la gráfica para que resultara más fácil de entender y tuviera más dinamismo. Para conseguir esto tuvimos que hacerlo de la siguiente manera/
(Afegir codi)
## PASO 13
El último paso consistía en añadir unas alarmas, es decir unos señales, que facilitaran información al usuario sobre cierros errores que se pudieran provocar al empezar el programa. En primer lugar añadimos al satelite tierra un led blanco y lo programamos para que se encendira cuando los datos que recibía eran nulos. Seguidamente, incorporamos también al satelite tierra un led azul que se encendía cada vez que se perdía la conexión entre el arduino satelite y el arduino tierra. Esto lo efectuamos de la siguiente manera:
(Afegir codi)
## RESUMEN Y VÍDEO
Aquí mostraremos el resultado final de la version 1 de nuestro proyecto. En primer lugar mencionar que finalizando el paso 13 (en concreto cuando estábamos definendo la led azul nos dimos cuenta de un error que cometimos y no tuvimos tiempo de arreglarlo. El problema se basaba en que la gráfica y la interfaz estaban vinculadoa al arduino satelite y, por lo tanto los datos que salían no se basaban en si el arduino tierra había recibido los datos correctamente, sino en si el arduino satelite los había enviado. Obviamente, al ser la versión 1, tenemos pensado correjir este error en la siguiente versión. Finalmente, aquí se muestran los códigos finales y el vídeo:
