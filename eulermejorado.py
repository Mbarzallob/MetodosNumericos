import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import getpass
import os

# Nuevos datos de prueba
x0 = 0
y0 = 1
xf = 5
h = 0.1

def metodo_euler_mejorado(f, x0, y0, xf, h):
    n = int((xf - x0) / h)
    x = np.linspace(x0, xf, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h, y[i] + h * k1)
        y[i + 1] = y[i] + (h / 2) * (k1 + k2)
    return x, y

def funcion_diferencial(x, y):
    # Ejemplo de una ecuación diferencial: dy/dx = -2xy
    return -2 * x * y

def grafica(f=None):
    global x0, y0, xf, h

    x, y = metodo_euler_mejorado(funcion_diferencial, x0, y0, xf, h)

    # Graficar los datos y la curva ajustada
    plt.plot(x, y, color='blue', label='Solución por método de Euler mejorado')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Método de Euler Mejorado')
    plt.show()

def eulermejorado(f=None):
    os.system("cls")
    global x0, y0, xf, h
    pedir_datos()
    x, y = metodo_euler_mejorado(funcion_diferencial, x0, y0, xf, h)
    imprimirEulerMejorado(x, y)

def imprimirEulerMejorado(x, y):
    os.system("cls")
    print("\nValores calculados con el método de Euler Mejorado:")
    tabla = np.column_stack((x, y))
    encabezado = ["x", "y"]
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))
    getpass.getpass("Presione enter para continuar con la gráfica:")
    grafica()

def pedir_datos():
    global x0, y0, xf, h
    print("-------------------------------------------------")
    print("            Método de Euler Mejorado")
    print("-------------------------------------------------")
    print(f"Valores actuales:\n x0: {x0}, y0: {y0}, xf: {xf}, h: {h}")
    print("\n¿Qué desea hacer?")
    print("1. Cambiar los datos existentes")
    print("2. Volver a los datos originales")
    print("0. Salir")
    respuesta = int(input("Ingrese su elección: "))
    if respuesta == 1:
        while True:
            try:
                x0 = float(input("Ingrese el valor inicial de x (x0): "))
                y0 = float(input("Ingrese el valor inicial de y (y0): "))
                xf = float(input("Ingrese el valor final de x (xf): "))
                h = float(input("Ingrese el tamaño del paso (h): "))
                if h <= 0 or xf <= x0:
                    raise ValueError("El tamaño del paso debe ser positivo y xf debe ser mayor que x0.")
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor, ingrese los valores nuevamente.")
    elif respuesta == 2:
        x0 = 0
        y0 = 1
        xf = 5
        h = 0.1
        print("Datos originales restaurados.")
    else:
        print("Saliendo...")
        return
