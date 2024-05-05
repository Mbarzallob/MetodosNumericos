import matplotlib.pyplot as plt
import numpy as np
import os

xl = -10
xu = 10
errorMax = 1
iterMax = 10
editado = False

def grafica(f):
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
    plt.grid(True)
    plt.show()

def funcion(f, x):
    return eval(f)

def imprimir():
    print("|------------------------------------------------|")
    print("|               Falsa Posición                   |")
    print("|------------------------------------------------|")
    print(f"| xl = {xl}{(50-2-6-len(str(xl)))*' '}|")
    print(f"| xu = {xu}{(50-2-6-len(str(xu)))*' '}|")
    print(f"| Error = {errorMax}{(50-2-9-len(str(errorMax)))*' '}|")
    print(f"| Iteraciones máximas = {iterMax}{(50-2-23-len(str(iterMax)))*' '}|")
    print("|------------------------------------------------|")
    print()

def falsaPosicion(f):
    global xl, xu, errorMax, iterMax
    imprimir()
    v = input("¿DESEA EDITAR LOS VALORES INICIALES? (s): ")
    if v.upper() == "S":
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
        xr = xl - (funcion(f, xl) * (xu - xl)) / (funcion(f, xu) - funcion(f, xl))
        fr = funcion(f, xr)
        if funcion(f, xl) * fr < 0:
            xu = xr
        else:
            xl = xr
        error = abs((xu - xl) / xu) * 100
        iter += 1
        print(f"{iter:9d}  {xl:9.4f}  {xu:9.4f}  {xr:9.4f}  {funcion(f, xl):9.4f}  {funcion(f, xu):9.4f}  {fr:9.4f}  {error:9.4f}")
        if error < errorMax:
            break
    input("Presione enter para continuar")
    os.system("cls")
