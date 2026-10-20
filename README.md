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
## PASO 9
Para hacer este paso tuvimos que simplificar la manera en la que el arduino satelite enviaba los datos al arduino tierra, ya que nuestro objetivo era crear una gráfica que mostrara los valores de humedad y temperatura dependiendo del tiempo, en el cual 0 se consideraba cuando empezaba el programa.
Para desarrollar este paso tuvimos que instalar la librería matplotlib. 
## PASO 10 y PASO 11
Para efectuar este paso tuvimos que usar la librería Tinker, la cual consistia en facilitar la interaccion del programa de Python y el usuario. 
Para hacerlo tuvimos que programar 3 botones con los que el usuario puede interactuar con la gràfica. En primer lugar aparece el botón de INICIAR, el cual el usuario tiene que clicar para que la gráfica se ponga en marcha. Para parar la gráfica y que deje de recopilar datos tuvimos que añadir el botón de PARAR. Finalmente, el botón REANUDAR se encargaba de volver a ejecutar la gráfica después de usar el botón de PARAR. El código usado para definir cada uno de los botones es el siguiente:
```C
#Asignamos cada botón de la interfaz:
AButton = Button(window, text="Iniciar", bg="#0AAE28", fg="white", font=("Arial", 10, "bold"), command=AClick)
AButton.grid(row=1, column=0, padx=10, pady=5, sticky=N + S + E + W)

BButton = Button(window, text="Parar", bg="#BC0C0C", fg="white", font=("Arial", 10, "bold"), command=BClick)
BButton.grid(row=2, column=0, padx=10, pady=5, sticky=N + S + E + W)

CButton = Button(window, text="Reanudar", bg='#818CF8', fg="white", font=("Arial", 10, "bold"), command=CClick)
CButton.grid(row=3, column=0, padx=10, pady=5, sticky=N + S + E + W)
```
## PASO 12
En este paso tuvimos que juntar la interfaz con la gráfica para que resultara más fácil de entender y tuviera más dinamismo. Para conseguir esto tuvimos que hacerlo de la siguiente manera:
```C
#Juntamos la gráfica y la interfaz:
canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=1, rowspan=3, padx=10, pady=10, sticky=N + S + E + W)
```
## PASO 13
El último paso consistía en añadir unas alarmas, es decir unos señales, que facilitaran información al usuario sobre cierros errores que se pudieran provocar al empezar el programa. En primer lugar añadimos al satelite tierra un led blanco y lo programamos para que se encendira cuando los datos que recibía eran nulos. Seguidamente, incorporamos también al satelite tierra un led azul que se encendía cada vez que se perdía la conexión entre el arduino satelite y el arduino tierra.
## RESUMEN Y VÍDEO
Aquí mostraremos el resultado final de la version 1 de nuestro proyecto. En primer lugar mencionar que finalizando el paso 13 (en concreto cuando estábamos definendo la led azul nos dimos cuenta de un error que cometimos y no tuvimos tiempo de arreglarlo. El problema se basaba en que la gráfica y la interfaz estaban vinculadoa al arduino satelite y, por lo tanto los datos que salían no se basaban en si el arduino tierra había recibido los datos correctamente, sino en si el arduino satelite los había enviado. Obviamente, al ser la versión 1, tenemos pensado correjir este error en la siguiente versión. Finalmente, aquí se muestran los códigos finales y el vídeo:

### CODIGO FINAL ARDUINO SATELITE
```C
//Definiciones necesarias:
#include <SoftwareSerial.h>
#include <DHT.h>
SoftwareSerial mySerial(10, 11); // RX, TX (azul, naranja)

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

//Definimos las variables que necesitaremos para nuestro transmisor:
const int ledVerdeSatelite = 4;// LED en el pin 13 (Amarillo)
const int ledErrorBlanco = 8;
const int ledErrorAzul = 7;
bool enviando = false;
unsigned long tiempoAnterior = 0;
unsigned long nextHT = 0;
bool esperandoTimeout = false;
unsigned long nextTimeoutHT = 0;
const long intervaloEnvio = 3000;
unsigned long ultimoMensajeRecibido = 0;
const long tiempoMaximoSinDatos = 5000;
bool arduinoConectado = false;

void setup() {
   mySerial.begin(9600);
   Serial.begin(9600);
   //Iniciamos el sensor de humedad y temperatura:
   pinMode(ledVerdeSatelite, OUTPUT);
   dht.begin();
}
void loop() {


   //Funciones de los tres botones de la interfaz en Pyhton:
if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    data.trim();
    
    if (data == "Inicio") { enviando = true; }
    if (data == "Parar") { enviando = false; }
    if (data == "Reanudar") { enviando = true; }
}

   //Recolectamos los datos de la temperatura y la humedad: 
   delay(3000);
   if(enviando==true){
   float h = dht.readHumidity();
   float t = dht.readTemperature();
      
      //Creamos una alarma que nos avisa cuando los datos sean nulos o incorrectos:
      if (isnan(h) || isnan(t)){
         Serial.println("Error al leer el sensor DHT11");
         digitalWrite(ledErrorBlanco, HIGH);
      }
      else {
          digitalWrite(ledErrorBlanco, LOW); 
      }
      //Creamos el código para la alarma que nos indica la desconexión entre los dos arduinos:
      if (mySerial.available() > 0) {
       String Comprobante=mySerial.readStringUntil('\n');
       Comprobante.trim();
       if (Comprobante=="Ok"){
       ultimoMensajeRecibido = millis();}
   }

   //Evitamos el envío de datos incorrectos y proporcionamos los datos ya verificados:
   if (digitalRead(ledErrorBlanco) == LOW && digitalRead(ledErrorAzul) == LOW) {
    mySerial.print("T: ");
    mySerial.print(t);
    mySerial.print(":H: ");
    mySerial.print(h);
    mySerial.print(":\n");

    
      digitalWrite(ledVerdeSatelite, HIGH);
        delay(100);
        digitalWrite(ledVerdeSatelite, LOW);

      Serial.print("T: ");
      Serial.print(t);
      Serial.print(":H: ");
      Serial.print(h);
      Serial.print("\n");
   }
   }
}
```
### CODIGO FINAL ARDUINO TIERRA
```C
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
```
### CODIGO FINAL PYHTON
```C
import tkinter as tk
from tkinter import *
import serial
import threading
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Configuramos el puerto serie:
device = 'COM3'
try:
    mySerial = serial.Serial(device, 9600)
except:
    mySerial = None  

#Creamos las variables para poder almacenar los datos de temperatura y humedad, así como el eje x para la gráfica:
temperaturas = []
humedad = []
eje_x = []
i = 0

def leer_datos():
    global i
    if mySerial and mySerial.is_open:
        if mySerial.in_waiting > 0:
            linea = mySerial.readline().decode('utf-8').rstrip()
            if linea:
                try:
                    trozos = linea.split(':')
                    #Extraemos los valores de temperatura y humedad:
                    temp_valor = float(trozos[1])
                    hum_valor = float(trozos[3])
                    
                    #Guardamos cada valor en su lista correspondiente:
                    eje_x.append(i)
                    temperaturas.append(temp_valor)
                    humedad.append(hum_valor)
                    
                    #Actualizamos los datos de la gráfica con los nuevos valores:
                    linea_temp.set_data(eje_x, temperaturas)
                    linea_hum.set_data(eje_x, humedad)
                    
                    #Creamos unos ejes que se adaptan a la gràfica según los valores que se van introduciendo:
                    ax.set_xlim(0, max(20, i + 5))
                    ax.set_ylim(0, 100)
                    
                    canvas.draw()
                    i += 1
                except Exception as e:
                    print(f"Error al procesar la línea: {e}")
                    
    
    window.after(500, leer_datos)
#Configuramos la interfaz y sus botones para poder iniciar, parar y reanudar la lectura de datos del puerto serie y hacemos que aparezcan en la parte superior de la interfaz:
def AClick():
    if mySerial and mySerial.is_open:
        mySerial.write("Inicio\n".encode('utf-8'))
    tituloLabel.config(text="Gráfica Iniciada")

def BClick():
    if mySerial and mySerial.is_open:
        mySerial.write("Parar\n".encode('utf-8'))
    tituloLabel.config(text="Gráfica Parada")

def CClick():
    if mySerial and mySerial.is_open:
        mySerial.write("Reanudar\n".encode('utf-8'))
    tituloLabel.config(text="Gráfica Reanudada")

#Configuramos la ventana de la interfaz (tamaño y título):
window = Tk()
window.title("Control y Monitorización Arduino")
window.geometry("850x500")

#Configuramos la cuadrícula:
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)  

#Etiqueta del estado de la gràfica (iniciada, parada o reanudada):
tituloLabel = Label(window, text="Pulsa Iniciar para empezar", font=("Courier", 10, "italic"))
tituloLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=N + S + E + W)

#Asignamos cada botón de la interfaz:
AButton = Button(window, text="Iniciar", bg="#0AAE28", fg="white", font=("Arial", 10, "bold"), command=AClick)
AButton.grid(row=1, column=0, padx=10, pady=5, sticky=N + S + E + W)

BButton = Button(window, text="Parar", bg="#BC0C0C", fg="white", font=("Arial", 10, "bold"), command=BClick)
BButton.grid(row=2, column=0, padx=10, pady=5, sticky=N + S + E + W)

CButton = Button(window, text="Reanudar", bg='#818CF8', fg="white", font=("Arial", 10, "bold"), command=CClick)
CButton.grid(row=3, column=0, padx=10, pady=5, sticky=N + S + E + W)

#Creamos la gràfica:
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

#Asignamos líneas vacías y las caracterizamos:
linea_temp, = ax.plot([], [], color='red', marker='o')
linea_hum, = ax.plot([], [], color='blue', marker='o')
ax.grid(True)

#Juntamos la gráfica y la interfaz:
canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=1, rowspan=3, padx=10, pady=10, sticky=N + S + E + W)


window.after(1000, leer_datos)


window.mainloop()
```
