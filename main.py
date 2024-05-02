import biseccion as bis
import falsaPosicion as fp
import newtonRaphson as nr
import secante as sec
import matplotlib.pyplot as plt
import numpy as np
import os
import math


f = ""

def imprimirMetodos():
    print("\n|------------------------------------------------|")
    print(f"|               {opciones[opcion[0]]['submenus'][opcion[1]]['nombre']}|")
    print("|               ELIJA UNA OPCION:                |")
    print("|------------------------------------------------|\n")
    print(" 1. Grafica")
    print(" 2. Metodo")
    print(" 0. Salir")

def graficarFuncion(f):
    x = np.linspace(-10, 10, 400)
    try:
        y = eval(f)
    except:
        print("Error: La expresión ingresada no es válida.")
        exit()
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de ' + f)
    plt.grid(True)
    plt.show()

def editarFuncion():
    global f
    print("\n|------------------------------------------------|")
    print("|                      FUNCIÓN                   |")
    print("|------------------------------------------------|")
    f = input("\n Ingrese la funcion con respecto a x: ")
    os.system("cls")
    
opciones = {
    1: {
        "nombre": "Metodos abiertos",
        "submenus": {
            1: {
                "nombre": "Metodo de la bisección           ", 
                "funciones": {
                    1: bis.grafica,
                    2: bis.biseccion
                }
            },
            2: {
                "nombre": "Metodo de la falsa posición      ", 
                "funciones": {
                    1: fp.grafica,
                    2: fp.falsaPosicion
                }
            }
        }
    },
    2: {
        "nombre": "Metodos cerrados",
        "submenus": {
            1:{
                "nombre": "Metodo de Newton-Raphson         ", 
                "funciones": {
                    1: nr.grafica,
                    2: nr.newtonRaphson
                }
            },
            2: {
                "nombre": "Metodo de la secante             ", 
                "funciones": {
                    1: sec.grafica,
                    2: sec.secante
                }
            }
        }
    }
}
os.system("cls")
editarFuncion()
opcion = [-1, -1, -1]
while opcion[0] != 0:
    opcion[1] = -1
    opcion[2] = -1
    print("\n|------------------------------------------------|")
    print("|                Menu principal                  |".upper())
    print("|               ELIJA UNA OPCION:                |")
    print("|------------------------------------------------|")
    print(f"            FUNCIÓN: {f}\n")
    for i in opciones:
        print(" "+str(i) + ". " + opciones[i]["nombre"])
    print(" 3. Editar la funcion")
    print(" 4. Graficar la funcion")
    print(" 0. Salir")
    opcion[0] = int(input("\n Ingrese su eleccion: "))
    os.system("cls")
    if(opcion[0] == 3):
        editarFuncion()
    elif(opcion[0] ==0):
        break
    elif(opcion[0]==4):
        graficarFuncion(f)
    else:
        while opcion[1] != 0:
            opcion[2] = -1
            print("\n|------------------------------------------------|")
            print(f"|               {opciones[opcion[0]]['nombre']}                 |")
            print("|               ELIJA UNA OPCION:                |")
            print("|------------------------------------------------|\n")
            for i in opciones[opcion[0]]['submenus']:
                print(" "+str(i) + ". " + opciones[opcion[0]]['submenus'][i]['nombre'])
            print(" 0. Regresar")
            opcion[1] = int(input("\n Ingrese su eleccion: "))
            os.system('cls')
            if(opcion[1]==0):
                break
            while opcion[2]!=0:
                imprimirMetodos()
                opcion[2] = int(input("\n Ingrese su eleccion: "))
                os.system('cls')
                if(opcion[2]!=0 and opcion[2]!=3):
                    opciones[opcion[0]]['submenus'][opcion[1]]['funciones'][opcion[2]](f)
                elif(opcion[2] == 3):
                    editarFuncion()
                        
                        

