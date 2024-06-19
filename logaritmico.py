import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def grafica(x, y, interpolacion):
    x_fit = np.linspace(min(x), max(x), 100)
    a, b = coeficientes_AB(x, y)
    res = a + b * np.log(interpolacion)
    
    # Graficar los datos y la curva ajustada
    plt.scatter(interpolacion, res, label='Datos')
    plt.plot(x_fit, a + b * np.log(x_fit), color='red', label=f'Ajuste logarítmico: {b}ln(x) {a}')
    
    # Agregar etiquetas a los puntos de datos
    for i, txt in enumerate(res):
        plt.annotate(f'{txt:.2f}', (interpolacion[i], res[i]), textcoords="offset points", xytext=(0,10), ha='center')
    
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def logaritmico(x, y, interpolar):
    a, b = coeficientes_AB(x, y)
    imprimir(a, b)
    res_interpolacion = evaluar(a, b, interpolar)
    imprimirInterpolacion(res_interpolacion)

def coeficientes_AB(x, y):
    X = np.log(x)
    n = len(x)
    
    sum_X = np.sum(X)
    sum_Y = np.sum(y)
    sum_XY = np.sum(X * y)
    sum_X2 = np.sum(X ** 2)
    
    b = (n * sum_XY - sum_X * sum_Y) / (n * sum_X2 - sum_X ** 2)
    a = (sum_Y - b * sum_X) / n
    return round(a, 4), round(b, 4)

def imprimir(a, b):
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

def evaluar(a, b, interpolar):
    resultados = np.round(a + b * np.log(interpolar), 6)
    return np.column_stack((interpolar, resultados))

# DATOS DE PRUEBA
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y_data = np.array([2.5, 7, 38, 55, 61, 122, 83, 145])
interpolacion = np.array([1, 2, 3, 4, 5])

logaritmico(x_data, y_data, interpolacion)
grafica(x_data, y_data, interpolacion)
