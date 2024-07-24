import matplotlib.pyplot as plt
import numpy as np
import getpass

# Valores iniciales y función global
a = 0  
b = 1  
h = 0.1  
y0 = 1  
f = ""

def grafica(funcion=None):
    global a, b, h, y0, f
    if not funcion:
        if not f:
            f = input("Ingrese la función y' con respecto a x, en términos de y: ")
        funcion = f

    x = np.arange(a, b + h, h)
    y = np.zeros_like(x)
    y[0] = y0
    
    for i in range(1, len(x)):
        k1 = h * eval(funcion.replace("x", str(x[i-1])).replace("y", str(y[i-1])))
        k2 = h * eval(funcion.replace("x", str(x[i-1] + h / 2)).replace("y", str(y[i-1] + k1 / 2)))
        k3 = h * eval(funcion.replace("x", str(x[i-1] + h / 2)).replace("y", str(y[i-1] + k2 / 2)))
        k4 = h * eval(funcion.replace("x", str(x[i-1] + h)).replace("y", str(y[i-1] + k3)))
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    plt.plot(x, y, marker='o')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método de Runge-Kutta')
    plt.grid(True)
    plt.show()

def rungekutta(funcion=None):
    global a, b, h, y0, f
    if not funcion:
        if not f:
            f = input("Ingrese la función y' con respecto a x, en términos de y: ")
        funcion = f
    
    x = np.arange(a, b + h, h)
    y = np.zeros_like(x)
    y[0] = y0
    
    print("\nx\t\t y")
    print("-------------------------")
    print(f"{x[0]:.2f}\t {y0:.6f}")
    
    for i in range(1, len(x)):
        k1 = h * eval(funcion.replace("x", str(x[i-1])).replace("y", str(y[i-1])))
        k2 = h * eval(funcion.replace("x", str(x[i-1] + h / 2)).replace("y", str(y[i-1] + k1 / 2)))
        k3 = h * eval(funcion.replace("x", str(x[i-1] + h / 2)).replace("y", str(y[i-1] + k2 / 2)))
        k4 = h * eval(funcion.replace("x", str(x[i-1] + h)).replace("y", str(y[i-1] + k3)))
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
        
        print(f"{x[i]:.2f}\t {y[i]:.6f}")
    
    getpass.getpass("Presione enter para continuar")

def imprimir_valores():
    global a, b, h, y0, f
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"h = {h}")
    print(f"y0 = {y0}")
    print(f"f = {f}")

def editar_valores():
    global a, b, h, y0, f
    a = float(input(f"Ingrese el nuevo valor para a (actual: {a}): ") or a)
    b = float(input(f"Ingrese el nuevo valor para b (actual: {b}): ") or b)
    h = float(input(f"Ingrese el nuevo valor para h (actual: {h}): ") or h)
    y0 = float(input(f"Ingrese el nuevo valor para y0 (actual: {y0}): ") or y0)
    f = input(f"Ingrese la nueva función y' (actual: {f}): ") or f

def limpiar_valores():
    global a, b, h, y0, f
    a = 0
    b = 1
    h = 0.1
    y0 = 1
    f = ""
    print("Valores reiniciados a los valores por defecto.")
