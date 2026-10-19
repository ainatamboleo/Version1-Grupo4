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

## PASO 6
## PASO 7
## PASO 8
## PASO 9
## PASO 10
## PASO 11
## PASO 12
## PASO 13
