import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Datos de prueba
x_data = [1, 2, 3, 4, 5, 6, 7, 8]
y_data = [2.5, 7, 38, 55, 61, 122, 83, 145]
interpolacion = [1, 2, 3, 4, 5]

def grafica(f = None):
    global x_data, y_data, interpolacion

    x_fit = np.linspace(min(x_data), max(x_data), 100)
    a, b = coeficientes_AB_logaritmica(x_data, y_data)
    res = a + b * np.log(interpolacion)
    
    # Graficar los datos y la curva ajustada
    plt.scatter(interpolacion, res, label='Datos')
    plt.plot(x_fit, a + b * np.log(x_fit), color='red', label=f'Ajuste logarítmico: {a} + {b}ln(x)')
    
    # Agregar etiquetas a los puntos de datos
    for i, txt in enumerate(res):
        plt.annotate(f'{txt:.2f}', (interpolacion[i], res[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def logaritmica(f= None):
    global x_data, y_data, interpolacion
    pedir_datos()
    a, b = coeficientes_AB_logaritmica(x_data, y_data)
    imprimir_logaritmica(a, b)
    res_interpolacion = evaluar_logaritmica(a, b, interpolacion)
    imprimirInterpolacion(res_interpolacion)

def coeficientes_AB_logaritmica(x, y):
    X = np.log(x)
    n = len(x)
    
    sum_X = np.sum(X)
    sum_Y = np.sum(y)
    sum_XY = np.sum(X * y)
    sum_X2 = np.sum(X ** 2)
    
    b = (n * sum_XY - sum_X * sum_Y) / (n * sum_X2 - sum_X ** 2)
    a = (sum_Y - b * sum_X) / n
    return round(a, 4), round(b, 4)

def imprimir_logaritmica(a, b):
    print()
    print("-----------------------------------------------------")
    print("|                  FUNCION ENCONTRADA               |")
    print("-----------------------------------------------------")
    print(f"            f(x) = {a} + {b} * ln(x)")
    print("-----------------------------------------------------")
    print(f"     VALOR DE A = {a}, VALOR DE B = {b}")
    print("-----------------------------------------------------")

def imprimirInterpolacion(tabla):
    print("\nVALORES INTERPOLADOS")
    encabezado = [" (x) ", "RESULTADOS f(x)"]
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))

def evaluar_logaritmica(a, b, interpolar):
    resultados = np.round(a + b * np.log(interpolar), 6)
    return np.column_stack((interpolar, resultados))

def imprimirArray(array):
    print(", ".join(map(str, array)))

def pedir_datos():
    global x_data, y_data, interpolacion
    print("-------------------------------------------------")
    print("             Metodo Logaritmico")
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
        x_data, y_data, interpolacion = np.array(x_data), np.array(y_data), np.array(interpolacion)
    else:
        print("Datos no cambiados...")
        x_data, y_data, interpolacion = np.array(x_data), np.array(y_data), np.array(interpolacion)


#Llamada a la función pedir_datos para obtener los datos del usuario
#pedir_datos()

# Ejecución del método de regresión logarítmica
#logaritmica()
#grafica_logaritmica()