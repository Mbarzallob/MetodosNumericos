import biseccion as bis
import falsaPosicion as fp
import newtonRaphson as nr
import secante as sec
import regresionlineal as rl
import regresionpolinomial as rp
import logaritmico as l
import lagrange as lag
import polinomial as p
import trazadorescubicos as tc
import matplotlib.pyplot as plt
import numpy as np
import os
import math

# Global variable for the function
f = ""

def display_menu(title, options):
    os.system("cls")
    print("\n|------------------------------------------------|")
    print(f"|                {title}                 |")
    print("|               ELIJA UNA OPCION:                |")
    print("|------------------------------------------------|")
    for i, option in enumerate(options):
        print(f" {i + 1}. {option['nombre']}")
    print(" 0. Salir")
    while True:
        try:
            choice = int(input("\n Ingrese su eleccion: "))
            if 0 <= choice <= len(options):
                return choice
            else:
                print("Por favor, elija una opción válida.")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número.")

def graficarFuncion(f):
    x = np.linspace(-10, 10, 400)
    try:
        y = eval(f)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Gráfica de {f}')
        plt.grid(True)
        plt.show()
    except:
        print("Error: La expresión ingresada no es válida.")

def editarFuncion():
    global f
    os.system("cls")
    print("\n|------------------------------------------------|")
    print("|                      FUNCIÓN                   |")
    print("|------------------------------------------------|")
    f = input("\n Ingrese la funcion con respecto a x: ")
    os.system("cls")

def execute_option(option, submenu, f):
    while True:
        os.system("cls")
        print(f"\n|------------------------------------------------|")
        print(f"|               {submenu['nombre']}|")
        print("|               ELIJA UNA OPCION:                |")
        print("|------------------------------------------------|\n")
        print(" 1. Grafica")
        print(" 2. Metodo")
        print(" 0. Salir")
        choice = display_menu(submenu['nombre'], [{"nombre": "Grafica"}, {"nombre": "Metodo"}])
        if choice == 0:
            break
        submenu['funciones'][choice](f)

def main_menu(opciones):
    global f
    while True:
        os.system("cls")
        print("\n|------------------------------------------------|")
        print("|                Menu principal                  |".upper())
        print("|               ELIJA UNA OPCION:                |")
        print("|------------------------------------------------|")
        print(f"            FUNCIÓN: {f}\n")
        main_options = [{"nombre": "Editar la funcion"}, {"nombre": "Graficar la funcion"}] + [{"nombre": opciones[i]["nombre"]} for i in opciones]
        option = display_menu("Menu principal", main_options)

        if option == 0:
            break
        elif option == 1:
            editarFuncion()
        elif option == 2:
            graficarFuncion(f)
        else:
            submenu_index = option - 3
            if submenu_index < 0 or submenu_index >= len(opciones):
                continue
            selected_option = list(opciones.values())[submenu_index]
            while True:
                submenu_option = display_menu(selected_option["nombre"], [{"nombre": sub["nombre"]} for sub in selected_option["submenus"].values()])
                if submenu_option == 0:
                    break
                submenu = selected_option["submenus"][submenu_option]
                execute_option(option, submenu, f)

opciones = {
    1: {
        "nombre": "Metodos cerrados",
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
        "nombre": "Metodos abiertos",
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
    },
    3: {
        "nombre": "Interpolaciones",
        "submenus": {
            1:{
                "nombre": "Regresion lineal         ", 
                "funciones": {
                    1: rl.grafica,
                    2: rl.lineal
                }
            },
            2: {
                "nombre": "Regresion polinomica             ", 
                "funciones": {
                    1: rp.grafica,
                    2: rp.regresionPolinomial
                }
            },
            3: {
                "nombre": "Regresion de potencias             ", 
                "funciones": {
                    1: p.grafica,
                    2: p.polinomial
                }
            },
            4: {
                "nombre": "Regresion logaritmica             ", 
                "funciones": {
                    1: l.grafica,
                    2: l.logaritmico
                }
            },
            5: {
                "nombre": "Trazadores cubicos             ", 
                "funciones": {
                    1: tc.grafica,
                    2: tc.trazadoresCubicos
                }
            },
            6: {
                "nombre": "Lagrange             ", 
                "funciones": {
                    1: lag.grafica,
                    2: lag.lagrange
                }
            },
            
        }
    }
}

main_menu(opciones)
