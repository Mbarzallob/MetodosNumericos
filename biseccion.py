import matplotlib.pyplot as plt
import numpy as np
import os
import getpass


xl = 0.5
xu = 2.5
errorMax = 1
iterMax = 10

def grafica(f):
    global xl, xu, errorMax, iterMax
    x = np.linspace(xl, xu, 500)
    try:
        y = eval(f)
    except:
        print("Error: La expresión ingresada no es válida.")
        exit()
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de ' + f)
    
    # Realizar la bisección
    iteraciones = []
    while len(iteraciones) < iterMax:
        xr = (xl + xu) / 2
        iteraciones.append((xl, xu, xr))
        fr = funcion(f, xr)
        if funcion(f, xl) * fr < 0:
            xu = xr
        else:
            xl = xr
        error = abs((xu - xl) / xu) * 100
        if error < errorMax:
            break
    
    # Dibujar las líneas verticales para cada iteración
    for i, (xl_i, xu_i, xr_i) in enumerate(iteraciones):
        plt.axvline(x=xr_i, color='r', linestyle='--', label=f"Iteración {i+1}: xr={xr_i:.4f}")
    
    plt.grid(True)
    plt.legend()
    plt.show()
    
def funcion(f,x):
    return eval(f)

def imprimir():
    print("|------------------------------------------------|")
    print("|                   Bisección                    |")
    print("|------------------------------------------------|")
    print(f"| xl = {xl}{(50-2-6-len(str(xl)))*" "}|")
    print(f"| xu = {xu}{(50-2-6-len(str(xu)))*" "}|")
    print(f"| Error = {errorMax}{(50-2-9-len(str(errorMax)))*" "}|")
    print(f"| Iteraciones maximas = {iterMax}{(50-2-23-len(str(iterMax)))*" "}|")
    print("|------------------------------------------------|")
    print()
    
def limpiar_valores():
    global xl, xu, errorMax, iterMax
    xl = -10
    xu = 10
    errorMax = 1
    iterMax = 10
    
def biseccion(f):
    global xl, xu, errorMax, iterMax
    imprimir()
    v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
    if(v.upper()=="S"):
        os.system("cls")
        imprimir()
        xl = float(input("Ingrese el límite inferior: "))
        os.system("cls")
        imprimir()
        xu = float(input("Ingrese el límite superior: "))
        os.system("cls")
        imprimir()
        errorMax = float(input("Ingrese el error: "))
        os.system("cls")
        imprimir()
        iterMax = int(input("Ingrese el número de iteraciones máximas: "))
    os.system("cls")
    imprimir()
    iter = 0
    print("Iteración    xl         xu         xr         f(xl)      f(xu)      f(xr)      Error")
    print("------------------------------------------------------------------------------------")
    while iter < iterMax:
        xr = (xl + xu) / 2
        try:
            fr = funcion(f, xr)
        except ZeroDivisionError:
            break
        if funcion(f,xl) * fr < 0:
            xu = xr
        else:
            xl = xr
        error = abs((xu - xl) / xu) * 100
        iter += 1
        print(f"{iter:9d}  {xl:9.4f}  {xu:9.4f}  {xr:9.4f}  {funcion(f, xl):9.4f}  {funcion(f, xu):9.4f}  {fr:9.4f}  {error:9.4f}")
        if error < errorMax:
            break
    getpass.getpass("Presione enter para continuar")
    os.system("cls")
    limpiar_valores()