import tkinter as tk
from tkinter import *
import serial
import threading
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Configuramos el puerto serie:
device = 'COM7'
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