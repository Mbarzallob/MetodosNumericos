import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Nuevos datos de prueba
x_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y_data = [0, 0.5, 2, 1.5, 0.5, 0, -0.5, -1.5, -2]
interpolacion = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]

MAX_NUMBERS = 100

def grafica(f=None):
    global x_data, y_data, interpolacion

    # Calcular los coeficientes de regresión lineal
    a, b = coeficientes_AB_lineal(x_data, y_data)
    y_fit = a + b * np.array(x_data)

    # Generar nuevos puntos para la curva ajustada
    x_fit = np.linspace(min(x_data), max(x_data), 100)
    y_fit_smooth = a + b * x_fit

    # Graficar los datos y la curva ajustada
    plt.scatter(x_data, y_fit, label='Datos originales')
    plt.plot(x_fit, y_fit_smooth, color='red', label=f'Regresión lineal: {a} + {b}x')

    # Agregar etiquetas a los puntos de datos
    for i, txt in enumerate(y_fit):
        plt.annotate(f'{txt:.2f}', (x_data[i], y_fit[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def lineal(f=None):
    global x_data, y_data, interpolacion
    pedir_datos()
    a, b = coeficientes_AB_lineal(x_data, y_data)
    imprimir_lineal(a, b)
    res_interpolacion = evaluar_lineal(a, b, interpolacion)
    imprimirInterpolacion(res_interpolacion)

def coeficientes_AB_lineal(x, y):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    
    sum_X = np.sum(x)
    sum_Y = np.sum(y)
    sum_XY = np.sum(x * y)
    sum_X2 = np.sum(x ** 2)
    
    b = (n * sum_XY - sum_X * sum_Y) / (n * sum_X2 - sum_X ** 2)
    a = (sum_Y - b * sum_X) / n
    return round(a, 4), round(b, 4)

def imprimir_lineal(a, b):
    print()
    print("-----------------------------------------------------")
    print("|                  FUNCION ENCONTRADA               |")
    print("-----------------------------------------------------")
    print(f"            f(x) = {a} + {b}x")
    print("-----------------------------------------------------")
    print(f"     VALOR DE A = {a}, VALOR DE B = {b}")
    print("-----------------------------------------------------")

def imprimirInterpolacion(tabla):
    print("\nVALORES INTERPOLADOS")
    encabezado = [" (x) ", "RESULTADOS f(x)"]
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))

def evaluar_lineal(a, b, interpolar):
    interpolar = np.array(interpolar)
    resultados = np.round(a + b * interpolar, 6)
    return np.column_stack((interpolar, resultados))

def imprimirArray(array):
    print(", ".join(map(str, array)))

def pedir_datos():
    global x_data, y_data, interpolacion
    print("-------------------------------------------------")
    print("             Metodo de Regresion Lineal")
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
        if len(x_data) > MAX_NUMBERS or len(y_data) > MAX_NUMBERS or len(interpolacion) > MAX_NUMBERS:
            print(f"El número máximo de entradas permitidas es {MAX_NUMBERS}. Por favor, intente de nuevo con menos datos.")
            return
        x_data, y_data, interpolacion = np.array(x_data), np.array(y_data), np.array(interpolacion)
    else:
        print("Datos no cambiados...")
        x_data, y_data, interpolacion = np.array(x_data), np.array(y_data), np.array(interpolacion)
