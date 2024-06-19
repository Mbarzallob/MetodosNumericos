import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def grafica(x, y, interpolacion):
    x_fit = np.linspace(min(x), max(x), 100)
    a, b = coeficientes_AB(np.log(x), np.log(y))
    
    # Calcular los resultados ajustados para la curva
    res_fit = np.exp(a) * (x_fit ** b)
    
    # Calcular los resultados de la interpolación
    res_interpolacion = np.exp(a) * (interpolacion ** b)
    
    # Graficar los datos y la curva ajustada
    plt.scatter(x, y, label='Datos')
    plt.plot(x_fit, res_fit, color='red', label=f'Ajuste de potencia: {np.exp(a):.2f} * x^{b:.2f}')
    
    # Graficar los puntos de interpolación
    plt.scatter(interpolacion, res_interpolacion, color='green', label='Interpolación')
    
    # Agregar etiquetas a los puntos de interpolación
    for i, txt in enumerate(res_interpolacion):
        plt.annotate(f'{txt:.2f}', (interpolacion[i], res_interpolacion[i]), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xscale('log')  # Escala logarítmica para el eje x
    plt.yscale('log')  # Escala logarítmica para el eje y
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def potencias(x, y, interpolar):
    a, b = coeficientes_AB(np.log(x), np.log(y))
    a = np.exp(a)
    
    imprimir(a, b)
    res_interpolacion = evaluar(a, b, interpolar)
    imprimirInterpolacion(res_interpolacion)

def coeficientes_AB(x, y):
    n = len(x)
    sum_log_x = np.sum(x)
    sum_log_y = np.sum(y)
    sum_log_x_log_y = np.sum(x * y)
    sum_log_x_squared = np.sum(x ** 2)
    
    b = (n * sum_log_x_log_y - sum_log_x * sum_log_y) / (n * sum_log_x_squared - sum_log_x ** 2)
    a = (sum_log_y - b * sum_log_x) / n
    
    return a, b

def imprimir(a, b):
    print("-----------------------------------------------------")
    print("|                  FUNCION ENCONTRADA               |")
    print("-----------------------------------------------------")
    print(f"            f(x) = {a:.2f} * x^{b:.2f}")
    print("-----------------------------------------------------")
    print(f"     VALOR DE A = {a:.2f}, VALOR DE B = {b:.2f}")
    print("-----------------------------------------------------")

def imprimirInterpolacion(tabla):
    print("\nVALORES INTERPOLADOS")
    encabezado = [" (x) ", "RESULTADOS f(x)"]
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))

def evaluar(a, b, interpolar):
    resultados = np.round(a * (interpolar ** b), 6)
    return np.column_stack((interpolar, resultados))

# DATOS DE PRUEBA
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.5, 7, 38, 55, 61, 122, 83, 145])
interpolacion = np.array([1, 2, 3, 4, 5])

#potencias(x, y, interpolacion)

#grafica(x, y,interpolacion)