import sympy as sp
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import getpass

funcion = 'x**3 - 2*x - 5'
n = 2
a, b = 10, 15

def elegir_funcion():
    global funcion, n, a, b
    
    print("Funciones para Cuadratura de Gauss: ")
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
    
    n = int(input("Ingrese el valor de n (2, 3, 4 o 5) para la cuadratura de Gauss: "))
    a = float(input("Ingrese el valor inicial del intervalo: "))
    b = float(input("Ingrese el valor final del intervalo: "))
    print("================== FUNCION ==================")
    print("F(x)= ", funcion)
    print(f"Intevalo Inferior: {a}, Intervalo Superior: {b}\n")

def cuadraturagauss(f=None):
    global funcion, n, a, b
    elegir_funcion()
    x = sp.Symbol('x')
    f = sp.sympify(funcion)
    
    # Convertimos la función a una función numérica
    f_num = sp.lambdify(x, f)
    
    # Nodos y pesos para n = 2, 3, 4 y 5
    if n == 2:
        nodos = [-1/np.sqrt(3), 1/np.sqrt(3)]
        pesos = [1, 1]
    elif n == 3:
        nodos = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
        pesos = [5/9, 8/9, 5/9]
    elif n == 4:
        nodos = [-np.sqrt((3 - 2*np.sqrt(6/5))/7), -np.sqrt((3 + 2*np.sqrt(6/5))/7), np.sqrt((3 + 2*np.sqrt(6/5))/7), np.sqrt((3 - 2*np.sqrt(6/5))/7)]
        pesos = [(18 + np.sqrt(30))/36, (18 - np.sqrt(30))/36, (18 - np.sqrt(30))/36, (18 + np.sqrt(30))/36]
    elif n == 5:
        nodos = [-np.sqrt(5 + 2 * np.sqrt(10/7))/3, -np.sqrt(5 - 2 * np.sqrt(10/7))/3, 0, np.sqrt(5 - 2 * np.sqrt(10/7))/3, np.sqrt(5 + 2 * np.sqrt(10/7))/3]
        pesos = [(322 - 13 * np.sqrt(70))/900, (322 + 13 * np.sqrt(70))/900, 128/225, (322 + 13 * np.sqrt(70))/900, (322 - 13 * np.sqrt(70))/900]
    else:
        print("Solo se soportan n = 2, 3, 4 y 5")
        return
    
    # Transformar nodos al intervalo [a, b]
    nodos_transformados = [(b - a) / 2 * nodo + (b + a) / 2 for nodo in nodos]
    
    # Calcular la integral aproximada
    integral_cg = 0
    for i in range(n):
        integral_cg += pesos[i] * f_num(nodos_transformados[i])
    integral_cg *= (b - a) / 2
    
    # Calcular el valor exacto de la integral si es posible
    integral_exacta = sp.integrate(f, (x, a, b))
    integral_exacta = integral_exacta.evalf()
    
    # Calcular errores
    error_absoluto = abs(integral_exacta - integral_cg)
    error_porcentual = (error_absoluto / abs(integral_exacta)) * 100
    
    # Crear tabla de resultados
    tabla = []
    tabla.append([n, integral_cg, integral_exacta, error_absoluto, str(round(error_porcentual, 5)) + '%'])
    
    encabezado = ["N", "Integral Cuadratura", "Integral Exacta", "Error Absoluto", "Error Porcentual"]
    
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))
    getpass.getpass("Presione enter para continuar")

def grafica(f=None):
    global funcion, a, b, n
    
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
    plt.title('Gráfico de la función en el intervalo dado')
    plt.legend()
    
    # Mostrar el gráfico
    plt.grid(True)
    plt.show()