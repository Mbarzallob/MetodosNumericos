# Bibliotecas necesarias
import sympy as sp
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import getpass

funcion = 'x**3 - 2*x - 5'

a, b = 1, 10

def elegir_funcion():
    global funcion, a, b
    
    print("Funciones para Simpson 1/3: ")
    print(" 0. Ingresar función")
    print(" 1. sin(x)")
    print(" 2. ln(x)")
    print(" 3. x**3 - x - 2")
    print(" 4. Funcion por defecto: x**3 - 2*x - 5")
    
    respuesta = int(input("Ingrese una opción: "))
    
    if respuesta == 0:
        funcion = input("Ingrese la función (use 'x' como variable): ")
    elif respuesta == 1:
        funcion = 'sin(x)'
    elif respuesta == 2:
        funcion = 'ln(x)'
    elif respuesta == 3:
        funcion = 'x**3 - x - 2'
    else:
        funcion = 'x**3 - 2*x - 5'
    
    print("F(x)= ", funcion)

def simpson13(f = None):
    global funcion
    elegir_funcion()
    x = sp.Symbol('x')
    f = sp.sympify(funcion)
    
    # Convertimos la función a una función numérica
    f_num = sp.lambdify(x, f)
    
    # Ingresar valores por teclado
    a = float(input("Ingrese el valor inicial del intervalo: "))
    b = float(input("Ingrese el valor final del intervalo: "))
    n = int(input("Ingrese el número de subintervalos (debe ser par): "))
    
    # Validar que n sea par
    if n % 2 != 0:
        print("El número de subintervalos debe ser par.")
        return
    
    h = (b - a) / n
    integral = f_num(a) + f_num(b)
    
    for i in range(1, n):
        k = a + i*h
        if i % 2 == 0:
            integral += 2 * f_num(k)
        else:
            integral += 4 * f_num(k)
    
    integral *= h/3
    
    # Calcular el valor exacto de la integral si es posible
    integral_exacta = sp.integrate(f, (x, a, b))
    integral_exacta = integral_exacta.evalf()
    
    # Calcular errores
    error_absoluto = abs(integral_exacta - integral)
    error_porcentual = (error_absoluto / abs(integral_exacta)) * 100
    
    # Crear tabla de resultados
    tabla = []
    tabla.append([n, integral, integral_exacta, error_absoluto, str(round(error_porcentual, 5)) + '%'])
    
    encabezado = ["N", "Integral Aproximada", "Integral Exacta", "Error Absoulto", "Error Porcentual"]
    
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))
    getpass.getpass("Presione enter para continuar")

def grafica(f=None):
    global funcion, a, b
    
    # Convertir la cadena de texto en una expresión SymPy
    x = sp.symbols('x')
    f = sp.sympify(funcion)

    # Evaluar la función en puntos dentro del intervalo
    x_fill = np.linspace(a, b, 100)
    y_fill = np.array([float(f.subs(x, punto)) for punto in x_fill])
    
    # Graficar la función
    plt.plot(x_fill, y_fill, label='Función: ' + funcion)
    
    # Resaltar el área bajo la curva entre a y b
    plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.4, label='Área bajo la curva')
    
    # Marcar los límites de integración
    plt.axvline(x=a, color='red', linestyle='--', label=f'Límite inferior a = {a}')
    plt.axvline(x=b, color='green', linestyle='--', label=f'Límite superior b = {b}')
    
    # Configurar la leyenda y etiquetas
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función con S1/3')
    plt.legend()
    
    # Mostrar el gráfico
    plt.grid(True)
    plt.show()
