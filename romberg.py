import matplotlib.pyplot as plt
import numpy as np
import os
import getpass

a = 0  # límite inferior de integración
b = 1  # límite superior de integración
errorMax = 1e-6
iterMax = 10
f = ""

def grafica(funcion=None):
    global a, b, errorMax, iterMax, f
    if not funcion:
        if not f:
            f = input("Ingrese la función con respecto a x: ")
        funcion = f
    imprimir()
    v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
    if v.upper() == "S":
        editar_valores()
    x = np.linspace(a, b, 500)
    try:
        y = eval(funcion)
    except:
        print("Error: La expresión ingresada no es válida.")
        return
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de ' + funcion)
    plt.grid(True)
    plt.show()

def imprimir():
    global a, b, errorMax, iterMax
    print("|------------------------------------------------|")
    print("|                   Romberg                      |")
    print("|------------------------------------------------|")
    print(f"| a = {a}{' ' * (50 - 2 - 4 - len(str(a)))}|")
    print(f"| b = {b}{' ' * (50 - 2 - 4 - len(str(b)))}|")
    print(f"| Error = {errorMax}{' ' * (50 - 2 - 9 - len(str(errorMax)))}|")
    print(f"| Iteraciones máximas = {iterMax}{' ' * (50 - 2 - 23 - len(str(iterMax)))}|")
    print("|------------------------------------------------|")
    print()

def limpiar_valores():
    global a, b, errorMax, iterMax
    a = 0
    b = 1
    errorMax = 1e-6
    iterMax = 10

def editar_valores():
    global a, b, errorMax, iterMax
    temp = input("Ingrese el límite inferior o presione enter para dejarlo igual: ")
    a = float(temp) if temp else a
    temp = input("Ingrese el límite superior o presione enter para dejarlo igual: ")
    b = float(temp) if temp else b
    temp = input("Ingrese el error o presione enter para dejarlo igual: ")
    errorMax = float(temp) if temp else errorMax
    temp = input("Ingrese el número de iteraciones máximas o presione enter para dejarlo igual: ")
    iterMax = int(temp) if temp else iterMax

def romberg(funcion=None):
    global a, b, errorMax, iterMax, f
    if not funcion:
        if not f:
            f = input("Ingrese la función con respecto a x: ")
        funcion = f
    imprimir()
    v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
    if v.upper() == "S":
        editar_valores()
    imprimir()

    def romberg_integration(f, a, b, eps=errorMax, max_iter=iterMax):
        R = np.zeros((max_iter, max_iter), float)
        h = b - a
        R[0, 0] = 0.5 * h * (eval(f.replace("x", str(a))) + eval(f.replace("x", str(b))))
        iter = 0
        print(f"R[0, 0] = {R[0, 0]}")
        for i in range(1, max_iter):
            h /= 2
            sum = 0.0
            for k in range(1, 2**i, 2):
                sum += eval(f.replace("x", str(a + k * h)))
            R[i, 0] = 0.5 * R[i-1, 0] + sum * h
            print(f"R[{i}, 0] = {R[i, 0]}")
            for j in range(1, i+1):
                R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)
                print(f"R[{i}, {j}] = {R[i, j]}")
            iter += 1
            if abs(R[i, i] - R[i-1, i-1]) < eps:
                break
        print("\nTabla de Romberg:")
        for i in range(iter+1):
            for j in range(i+1):
                print(f"{R[i, j]:.6f}", end="\t")
            print()
        return R[i, i], iter

    resultado, iteraciones = romberg_integration(funcion, a, b, errorMax, iterMax)
    print(f"\nResultado de la integración: {resultado}")
    print(f"Iteraciones: {iteraciones}")
    getpass.getpass("Presione enter para continuar")
    limpiar_valores()
