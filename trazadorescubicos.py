import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from tabulate import tabulate

# Nuevos datos de prueba
x_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y_data = [0, 0.5, 2, 1.5, 0.5, 0, -0.5, -1.5, -2]
interpolacion = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]

MAX_NUMBERS = 100

def grafica(f=None):
    global x_data, y_data, interpolacion

    # Crear el modelo de trazadores cúbicos
    cs = CubicSpline(x_data, y_data)

    # Generar nuevos puntos para una curva suave
    x_fit = np.linspace(min(x_data), max(x_data), 100)
    y_fit = cs(x_fit)

    # Graficar los datos y la curva ajustada
    plt.scatter(x_data, y_data, label='Datos originales')
    plt.plot(x_fit, y_fit, color='red', label='Trazadores cúbicos')

    # Agregar etiquetas a los puntos de datos
    for i, txt in enumerate(y_data):
        plt.annotate(f'{txt:.2f}', (x_data[i], y_data[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def trazadoresCubicos(f=None):
    global x_data, y_data, interpolacion
    pedir_datos()
    cs = CubicSpline(x_data, y_data)
    res_interpolacion = evaluar_trazadoresCubicos(cs, interpolacion)
    imprimir_trazadoresCubicos(cs)
    imprimirInterpolacion(res_interpolacion)

def evaluar_trazadoresCubicos(cs, interpolar):
    resultados = np.round(cs(interpolar), 6)
    return np.column_stack((interpolar, resultados))

def imprimir_trazadoresCubicos(cs):
    print("\nTrazadores cúbicos generados:")
    for i in range(len(cs.c.T)):
        c = cs.c.T[i]
        print(f"Para el intervalo [{x_data[i]}, {x_data[i+1]}]:")
        print(f"Coeficientes: {c[0]} + {c[1]}*(x - {x_data[i]}) + {c[2]}*(x - {x_data[i]})^2 + {c[3]}*(x - {x_data[i]})^3")

def imprimirInterpolacion(tabla):
    print("\nVALORES INTERPOLADOS")
    encabezado = [" (x) ", "RESULTADOS f(x)"]
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))

def imprimirArray(array):
    print(", ".join(map(str, array)))

def pedir_datos():
    global x_data, y_data, interpolacion
    print("-------------------------------------------------")
    print("             Metodo de Trazadores Cubicos")
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
