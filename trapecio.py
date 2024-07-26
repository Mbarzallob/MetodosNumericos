import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import getpass
import os

# Nuevos datos de prueba
a = 0
b = 1
n = 10

def funcion(x):
    # Ejemplo de una función a integrar: f(x) = x^2
    return x ** 2

def regla_trapecio(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral, x, y

def grafica(f=None):
    global a, b, n

    _, x, y = regla_trapecio(funcion, a, b, n)

    # Graficar los datos y la curva ajustada
    plt.plot(x, funcion(x), color='blue', label='f(x) = x^2')
    plt.fill_between(x, 0, funcion(x), color='skyblue', alpha=0.4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Regla del Trapecio')
    plt.show()

def trapecio(f=None):
    os.system("cls")
    global a, b, n
    pedir_datos()
    integral, x, y = regla_trapecio(funcion, a, b, n)
    imprimir_trapecio(integral, x, y)

def imprimir_trapecio(integral, x, y):
    os.system("cls")
    print("\nValores calculados con la regla del trapecio:")
    tabla = np.column_stack((x, y))
    encabezado = ["x", "f(x)"]
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))
    print(f"\nIntegral aproximada: {integral}")
    getpass.getpass("Presione enter para continuar con la gráfica:")
    grafica()

def pedir_datos():
    global a, b, n
    print("-------------------------------------------------")
    print("            Regla del Trapecio")
    print("-------------------------------------------------")
    print(f"Valores actuales:\n a: {a}, b: {b}, n: {n}")
    print("\n¿Qué desea hacer?")
    print("1. Cambiar los datos existentes")
    print("2. Volver a los datos originales")
    print("0. Salir")
    respuesta = int(input("Ingrese su elección: "))
    if respuesta == 1:
        while True:
            try:
                a = float(input("Ingrese el valor inicial de x (a): "))
                b = float(input("Ingrese el valor final de x (b): "))
                n = int(input("Ingrese el número de subintervalos (n): "))
                if n <= 0 or b <= a:
                    raise ValueError("El número de subintervalos debe ser positivo y b debe ser mayor que a.")
                break
            except ValueError as e:
                print(f"Error: {e}. Por favor, ingrese los valores nuevamente.")
    elif respuesta == 2:
        a = 0
        b = 1
        n = 10
        print("Datos originales restaurados.")
    else:
        print("Saliendo...")
        return
