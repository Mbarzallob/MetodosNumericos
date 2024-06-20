import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import getpass
import os

x_data = [1, 2, 3, 4, 5]
y_data = [1, 4, 9, 16, 25]
interpolacion = [1, 2, 3, 4, 5]

def obtener_puntos():
    global x_data, y_data, interpolacion
    print("-------------------------------------------------")
    print("         Interpolación de Lagrange")
    print("-------------------------------------------------")
    print("Existen los siguientes valores de prueba")
    print("Datos del eje X:")
    imprimirArray(x_data)
    print("Datos del eje Y:")
    imprimirArray(y_data)
    print("Datos a interpolar:")
    imprimirArray(interpolacion)
    print("\n¿Desea cambiarlos?")
    respuesta = int(input("1. Sí\n2. No\n"))
    if respuesta == 1:
        x_data = list(map(float, input("Ingrese los valores de x separados por comas: ").split(',')))
        y_data = list(map(float, input("Ingrese los valores de y separados por comas: ").split(',')))
        interpolacion = list(map(float, input("Ingrese los valores de interpolar separados por comas: ").split(',')))
    else:
        print("Datos no cambiados...")
    os.system('cls' )

def lagrange_evaluar(x, puntos_x, puntos_y):
    suma = 0
    for i in range(len(puntos_x)):
        producto = puntos_y[i]
        for j in range(len(puntos_x)):
            if i != j:
                producto *= (x - puntos_x[j]) / (puntos_x[i] - puntos_x[j])
        suma += producto
    return suma

def grafica(f=None):
    global x_data, y_data, interpolacion
    x_fit = np.linspace(min(x_data), max(x_data), 500)
    y_fit = [lagrange_evaluar(x, x_data, y_data) for x in x_fit]
    
    plt.scatter(x_data, y_data, label='Datos')
    plt.plot(x_fit, y_fit, color='red', label='Interpolación de Lagrange')
    
    for i, txt in enumerate(y_data):
        plt.annotate(f'{txt:.2f}', (x_data[i], y_data[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    os.system('cls' )

def imprimirArray(array):
    print(", ".join(map(str, array)))

def imprimir_polinomio(polinomio):
    print("\nPolinomio de Lagrange:")
    print(f"P(x) = {polinomio}")

def lagrange(f=None):
    global x_data, y_data, interpolacion
    os.system("cls")
    obtener_puntos()

    print("\nPuntos dados:")
    print(tabulate(list(zip(x_data, y_data)), headers=['x', 'y'], tablefmt="grid"))

    n = len(x_data)
    polinomio = ""

    for i in range(n):
        L_i = f"L_{i}(x) = "
        numerador = ""
        denominador = ""
        for j in range(n):
            if i != j:
                numerador += f"(x - {x_data[j]})"
                denominador += f"({x_data[i]} - {x_data[j]})"
                if j != n - 1 and not (i == n - 2 and j == n - 1):
                    numerador += " * "
                    denominador += " * "
        L_i += f"{numerador} / {denominador}"
        print(L_i)

        if i < n - 1:
            polinomio += f"{y_data[i]} * ({numerador} / {denominador}) + "
        else:
            polinomio += f"{y_data[i]} * ({numerador} / {denominador})"
    
    imprimir_polinomio(polinomio)

    while True:
        x = input("\nIngrese un valor de x para evaluar el polinomio (o 'salir' para terminar): ")
        if x.lower() == 'salir':
            break
        try:
            x = float(x)
            y = lagrange_evaluar(x, x_data, y_data)
            print(f"P({x}) = {y}")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    os.system('cls' )