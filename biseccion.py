import matplotlib.pyplot as plt
import numpy as np
import os
import getpass

xl = -10
xu = 10
errorMax = 1
iterMax = 10
f = ""

def grafica(funcion=None):
    global xl, xu, errorMax, iterMax, f
    if not funcion:
        if not f:
            f = input("Ingrese la función con respecto a x: ")
        funcion = f
    imprimir()
    v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
    if v.upper() == "S":
        editar_valores()
    x = np.linspace(xl, xu, 500)
    try:
        y = eval(funcion)
    except:
        print("Error: La expresión ingresada no es válida.")
        return
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de ' + funcion)
    
    iteraciones = []
    while len(iteraciones) < iterMax:
        xr = (xl + xu) / 2
        iteraciones.append((xl, xu, xr))
        try:
            fr = eval(funcion.replace("x", str(xr)))
        except ZeroDivisionError:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!!!!!!!!!! División por cero !!!!!!!!!!!!!!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            break
        if eval(funcion.replace("x", str(xl))) * fr < 0:
            xu = xr
        else:
            xl = xr
        error = abs((xu - xl) / xu) * 100
        if error < errorMax:
            break
    
    for i, (xl_i, xu_i, xr_i) in enumerate(iteraciones):
        plt.axvline(x=xr_i, color='r', linestyle='--', label=f"Iteración {i+1}: xr={xr_i:.4f}")
    
    plt.grid(True)
    plt.legend()
    plt.show()

def imprimir():
    global xl, xu, errorMax, iterMax
    print("|------------------------------------------------|")
    print("|                   Bisección                    |")
    print("|------------------------------------------------|")
    print(f"| xl = {xl}{' ' * (50 - 2 - 6 - len(str(xl)))}|")
    print(f"| xu = {xu}{' ' * (50 - 2 - 6 - len(str(xu)))}|")
    print(f"| Error = {errorMax}{' ' * (50 - 2 - 9 - len(str(errorMax)))}|")
    print(f"| Iteraciones máximas = {iterMax}{' ' * (50 - 2 - 23 - len(str(iterMax)))}|")
    print("|------------------------------------------------|")
    print()

def limpiar_valores():
    global xl, xu, errorMax, iterMax
    xl = -10
    xu = 10
    errorMax = 1
    iterMax = 10

def editar_valores():
    global xl, xu, errorMax, iterMax
    temp = input("Ingrese el límite inferior o presione enter para dejarlo igual: ")
    xl = float(temp) if temp else xl
    temp = input("Ingrese el límite superior o presione enter para dejarlo igual: ")
    xu = float(temp) if temp else xu
    temp = input("Ingrese el error o presione enter para dejarlo igual: ")
    errorMax = float(temp) if temp else errorMax
    temp = input("Ingrese el número de iteraciones máximas o presione enter para dejarlo igual: ")
    iterMax = int(temp) if temp else iterMax

def biseccion(funcion=None):
    global xl, xu, errorMax, iterMax, f
    if not funcion:
        if not f:
            f = input("Ingrese la función con respecto a x: ")
        funcion = f
    imprimir()
    v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
    if v.upper() == "S":
        editar_valores()
    imprimir()
    iter = 0
    print("Iteración    xl         xu         xr         f(xl)      f(xu)      f(xr)      Error")
    print("------------------------------------------------------------------------------------")
    while iter < iterMax:
        xr = (xl + xu) / 2
        try:
            fr = eval(funcion.replace("x", str(xr)))
        except ZeroDivisionError:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!!!!!!!!!! División por cero !!!!!!!!!!!!!!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            break
        if eval(funcion.replace("x", str(xl))) * fr < 0:
            xu = xr
        else:
            xl = xr
        error = abs((xu - xl) / xu) * 100
        iter += 1
        print(f"{iter:9d}  {xl:9.4f}  {xu:9.4f}  {xr:9.4f}  {eval(funcion.replace('x', str(xl))):9.4f}  {eval(funcion.replace('x', str(xu))):9.4f}  {fr:9.4f}  {error:9.4f}")
        if error < errorMax:
            break
    getpass.getpass("Presione enter para continuar")
    limpiar_valores()
