import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import getpass

x0= 0
x1 = 1
xr = None
es = 0.01
imax = 10
fu= ""



def secante(funcion=None):
    global x0, x1, es, imax, fu, xr
    if not funcion:
        if not fu:
            fu = input("Ingrese la función con respecto a x: ")
        else:
            editar_funcion = input("¿Desea editar la función existente? (s): ")
            if editar_funcion.upper() == "S":
                fu = input("Ingrese la función con respecto a x: ")
        
        funcion = fu
    imprimir()
    v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
    if(v.upper()=="S"):
           editar_valores()
    imprimir()

    iter = 0
    xr = x1
    print("Iteración      x0          x1          xr         f(x0)        f(x1)       Ea%")
    co = True
    while co == True:
        xrold = xr
        if f(x1,funcion) - f(x0, funcion) == 0:
            print("Division by zero error!")
            co = False
        else:
            xr = x1 - f(x1,funcion) * (x1 - x0) / (f(x1,funcion) - f(x0, funcion))
            iter += 1
            if xr != 0:
                ea = abs((xr - xrold) / xr) * 100
            print("{:<12}{:<12.6f}{:<12.6f}{:<12.6f}{:<12.6f}{:<12.6f}{:<12.6f}".format(iter, x0, x1,xr, f(x0,funcion), f(x1, funcion), ea))
            if ea < es or iter >= imax:
                #break
                co = False

            x0, x1 = x1, xr
    #return xr, iter, ea
    print(f"\nRoot: {xr}")
    print(f"Iterations: {iter}")
    print(f"Final Approximate Error: {ea}%")

    limpiar_valores()
    getpass.getpass("Presione enter para continuar")

def imprimir():
    global x0, x1, es, imax 
    print("|------------------------------------------------|")
    print("|            MÉTODO DE LA SECANTE                |")
    print("|------------------------------------------------|")
    print(f"| x0 = {x0}{(50-2-6-len(str(x0)))*" "}|")
    print(f"| x1 = {x1}{(50-2-6-len(str(x1)))*" "}|")
    print(f"| Error = {es}{(50-2-9-len(str(es)))*" "}|")
    print(f"| Iteraciones maximas = {imax}{(50-2-23-len(str(imax)))*" "}|")
    print("|------------------------------------------------|")

def editar_valores():
    global x0, x1, es, imax
    temp = input("Ingrese el límite inferior o presione enter para dejarlo igual: ")
    x0 = float(temp) if temp else x0
    temp = input("Ingrese el límite superior o presione enter para dejarlo igual: ")
    x1 = float(temp) if temp else x1
    temp = input("Ingrese el error o presione enter para dejarlo igual: ")
    es = float(temp) if temp else es
    temp = input("Ingrese el número de iteraciones máximas o presione enter para dejarlo igual: ")
    imax = int(temp) if temp else imax

def limpiar_valores(funcion = None):
    global x0, x1, es, imax
    x0 = 0
    x1 = 1
    es = 0.01
    imax = 10


def f(x, funcion):
    # Define your function f(x) here
    return eval(funcion)  
        


def grafica(funcion=None):
    global x0, x1, es, imax, fu, xr
    if not funcion:
        if not fu:
            fu = input("Ingrese la función con respecto a x: ")
        funcion = fu


    x = np.linspace(x0-2, x1+2, 500)
    try:
        y = eval(funcion)
    except Exception as e:
        print(f"Error: La expresión ingresada no es válida. {e}")
        return
    
    plt.plot(x, y, label=funcion)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    if xr is not None:
        plt.scatter(xr, 0, color='green', zorder=5)
        plt.text(xr, 0, f'Root: {xr:.4f}', fontsize=9, verticalalignment='bottom', horizontalalignment='right')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de ' + funcion)    
    plt.legend()
    plt.grid(True)
    plt.show()

# Secant()
# grafica()
