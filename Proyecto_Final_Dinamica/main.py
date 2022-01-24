# Creado por: Jose Javier Fernández González
# Parte del Primer Poryecto de Dinámica
# Segundo Semestre 2021
# Validación del Problema 16-62 del Libro de Dinámica de Hibbeler.
# Grupo 01 - Carnet 2020425930

from decimal import *
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from PIL import ImageTk,Image
import math

root = Tk()
root.title("Solucionador en Python")
getcontext().prec = 5


        
        #FUNC
def validateNum(num):
    try:
        float(num)
        return "✔"
    except:
        return "✖️"


def solve(distanciaBC = Decimal(15), graph=False):
    #Declaración de variables y asignación de valores
    global velocidadAngularBC
    global velocidadAngularD
    global distanciaD

    velocidadAngularBC= Decimal(inicialBC)
    velocidadAngularD= Decimal(inicialD)
    
    distanciaD = Decimal(20)


    #Velocidad de B
    global velocidadB
    velocidadB = velocidadAngularBC * distanciaBC

    #Velocidad de D
    global velocidadD
    velocidadD = velocidadAngularD * distanciaD

    #Velocidad Angular A
    global velocidadAngularA
    velocidadAngularA = (velocidadD-velocidadB)/(distanciaD-distanciaBC)
    if graph==False:
        #Presentar los Resultados
        return "    Velocidad tangencial de B: "+str(velocidadB)+" rad/s i+ \n    Velocidad tangencial de D: "+str(velocidadD)+" rad/s i+ \n    Velocidad angular de A: "+str(velocidadAngularA)+" rad/s k+ \n"
    else:
        return velocidadAngularA



def resultados():
    resultados = solve()
    Label(root, text=resultados, justify="left",bg='white', font=instruText, fg=col3).grid(row=9, columnspan=3,rowspan=2, sticky="nw")
    


#Graficar La velocidad alcanzada con respecto al radio del engranaje A
def graf():
    radios=[]
    velocidades=[]
    i=1
    while i<=distanciaD:
        radios.append(i)
        i+=1
    for j in radios:
        distanciaBC = Decimal(20-j)
        velA=solve(distanciaBC, True)
        velocidades.append(velA)
    
    
    fig = Figure(figsize = (6, 5),dpi = 80)
    plt=fig.add_subplot(111, xlabel="Radio del engranaje A [in]", ylabel="Velocidad Angular del Engranaje [rad/s]", title="Velocidad Angular de A dependiendo de su Radio")
    plt.plot(radios,velocidades)
    canvas = FigureCanvasTkAgg(fig, master = root)  
    canvas.draw()
    canvas.get_tk_widget().grid(row=8,column=4, rowspan=5)



#INTERFAZ GRÁFICA

def submitBC():
    global inicialBC
    inicialBC = entryBC.get()
    Label(root, text= validateNum(inicialBC), wraplength=50, bg='white', font=tituloText, fg=col2).grid(row=3, column=2)
    valorInicial = Label(root, text="Valor ingresado: "+ inicialBC +" rad/s k+",bg='white',fg=col3,font=avisoText)
    valorInicial.grid(row=4, column=0)

def submitD():
    global inicialD
    inicialD = entryD.get()
    Label(root, text= validateNum(inicialD), wraplength=50, bg='white', font=tituloText, fg=col2).grid(row=6, column=2)
    valorInicial = Label(root, text="Valor ingresado: "+ inicialD +" rad/s k+",bg='white',fg=col3,font=avisoText)
    valorInicial.grid(row=7, column=0)



        #GUI
#Espacios Vacios
Label(root, text="", height=2, width=2, bg='white').grid(row=0, column=2)
Label(root, text="", height=2, width=2, bg='white').grid(row=100, column=100)
Label(root, text="", height=2,width=2, bg='white').grid(row=4, column=0)
Label(root, text="", height=2, bg='white').grid(row=7, column=0)
Label(root, text="", height=15 , bg='white').grid(row=12, column=0)

#Estética
##Colores
col1="#3C4F76"
col2="#AEC5EB"
col3="#982649"

root.configure(bg='white')
tituloText = ("Helvetica",18,"bold")
subtituloText = ("Helvetica",16,"bold")
instruText = ("Helvetica",12)
avisoText = ("Helvetica",11,"bold")
botonText = ("Helvetica",11,"bold")


#Título
titulo = Label(root, text="Validación del Problema 16-62 \n\n Jose Javier Fernández González\n 2020425930 \n Dinámica - Proyecto 2 \n ITCR\n\n", height=8, bg='white',font=tituloText, fg=col1)
titulo.grid(row=1, columnspan=2)



#Barra BC
Label(root, text="Inserte la Velocidad Angular de BC en k :", wraplength=150, width= 20, bg='white',font=instruText).grid(row=2, column=0)

entryBC = Entry(root, width=15)
entryBC.grid(row=3, column=0)

buttonBC = Button(root, width=10, text="Ingresar.", bg='white', font=botonText , activebackground=col2 , command=submitBC)
buttonBC.grid(row=3, column=1)


#Engranaje D
Label(root, text="\nInserte la Velocidad Angular del Engranaje D en k: ", wraplength=150, width= 20, bg='white',font=instruText).grid(row=5, column=0)

entryD = Entry(root, width=15)
entryD.grid(row=6, column=0)

buttonD = Button(root, width=10, text="Ingresar.", bg='white', font=botonText , activebackground=col2 , command=submitD)
buttonD.grid(row=6, column=1)


#Resultados
Label(root, text="  Resultados...", height=5, justify="left", bg='white', font=subtituloText).grid(row=8, columnspan=2, sticky="nw")

#Botón Solución
buttonS = Button(root, width=10,height=2, text="Solucionar", bg='white',activebackground=col2, font=botonText, command=resultados)
buttonS.grid(row=9, column=2)

#Botón Graficar
buttonG = Button(root, width=10,height=2, text="Graficar", bg='white',activebackground=col2, font=botonText, command=graf)
buttonG.grid(row=11, column=2)

#Ilustración del Problema
problema = ImageTk.PhotoImage(Image.open("./imgs/Fig1-Program.png"))
Label(root,text="           ",bg='white').grid(row=0, column=3)
Label(image=problema, bg='white').grid(row=1, column=4, rowspan=7)

#Gráfica

root.mainloop()
