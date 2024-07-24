from sympy import symbols, diff, sympify
from tabulate import tabulate

import numpy as np
import matplotlib.pyplot as plt
import getpass

# Variables globales
x_val = 0
h = 0.01
method = "centrada"
fu = "exp(-2*x) - x"

def richardson(funcion=None):
    global x_val, h, fu
    if not funcion:
        if not fu:
            fu = input("Ingrese la función f(x): ")
        else:
            editar_funcion = input("¿Desea editar la función existente? (s): ")
            if editar_funcion.upper() == "S":
                fu = input("Ingrese la función f(x): ")
        
        funcion = fu.replace("^", "**")  # Reemplazar ^ con **
    imprimir()
    v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
    if(v.upper()=="S"):
           editar_valores()
    imprimir()

    # Calcular derivadas hacia adelante, atrás y centrada con h y h/2
    D1 = (f(x_val + h, funcion) - f(x_val - h, funcion)) / (2 * h)
    D2 = (f(x_val + h/2, funcion) - f(x_val - h/2, funcion)) / h

    # Aplicar el método de Richardson para mejorar la precisión
    derivative_richardson = (4 * D2 - D1) / 3
    
    real = derivada_de_funcion(funcion, x_val)[1]

    error_porcentual = abs(real - derivative_richardson) * 100

    tabla = []
    tabla.append([x_val, derivative_richardson, real, str(round(error_porcentual, 5)) + '%'])
    
    encabezado = ["x", "Derivada Aproximada", "Derivida Exacta", "Error Porcentual"]
    
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))

    


    print(f"La derivada aproximada de f(x) en x = {x_val} usando el método de Richardson es {derivative_richardson}")
    
    limpiar_valores()
    getpass.getpass("Presione enter para continuar")

def imprimir():
    global x_val, h, method
    print("|------------------------------------------------|")
    print("|            MÉTODO DE RICHARDSON                |")
    print("|------------------------------------------------|")
    print(f"| x_val = {x_val}{(50-2-9-len(str(x_val)))*' '}|")
    print(f"| h = {h}{(50-2-5-len(str(h)))*' '}|")
    print("|------------------------------------------------|")

def editar_valores():
    global x_val, h, method
    temp = input("Ingrese el valor de x o presione enter para dejarlo igual: ")
    x_val = float(temp) if temp else x_val
    temp = input("Ingrese el tamaño del paso (h) o presione enter para dejarlo igual: ")
    h = float(temp) if temp else h

def limpiar_valores():
    global x_val, h, method
    x_val = 0
    h = 0.01

def f(valor_x, funcion_s):
    # Define your function f(x) here
    x = symbols('x')
    funcion = sympify(funcion_s)
    resultado = funcion.subs(symbols('x'), valor_x)

    return resultado.evalf()


def derivada_de_funcion(funcion_str, valor_x):
    # Definir la variable simbólica
    x = symbols('x')
    # Convertir la cadena a una expresión simbólica
    funcion = sympify(funcion_str)
    # Calcular la derivada
    derivada = diff(funcion, x)
    resultado = derivada.subs(symbols('x'), valor_x)
    resultado_num = resultado.evalf()

    return  derivada,resultado_num


def grafica(funcion=None):
    global x_val, h, fu
    if not funcion:
        if not fu:
            fu = input("Ingrese la función f(x): ")
        funcion = fu.replace("^", "**")  # Reemplazar ^ con **

    # x_vals = np.linspace(x_val-2, x_val+2, 500)
    # y_vals = [f(val, funcion) for val in x_vals]

    # plt.plot(x_vals, y_vals, label=funcion)
    # plt.axhline(0, color='black', linewidth=0.5)
    # plt.axvline(0, color='black', linewidth=0.5)

    D1 = (f(x_val + h, funcion) - f(x_val - h, funcion)) / (2 * h)
    D2 = (f(x_val + h/2, funcion) - f(x_val - h/2, funcion)) / h
    derivative_richardson = (4 * D2 - D1) / 3

    derivacionV = derivada_de_funcion(funcion, x_val)
    funcionDerivada = derivacionV[0]

    puntoD = derivacionV[1]

    x_val_derivada = np.linspace(x_val - 1, x_val + 1, 500)
    y_vals_derivada = [funcionDerivada.subs(symbols('x'), val) for val in x_val_derivada]


    # plt.scatter(x_val, f(x_val, funcion), color='red', zorder=5)
    # plt.text(x_val, f(x_val, funcion), f'({x_val}, {f(x_val, funcion):.4f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')

    plt.plot(x_val_derivada, y_vals_derivada, label='Derivada')
    plt.axhline(0, color='blue', zorder=5)
    plt.axvline(x_val, color='blue', zorder=5)

    plt.scatter(x_val, derivative_richardson, color='green', zorder=5)
    plt.text(x_val, derivative_richardson, f'({x_val}, {derivative_richardson:.4f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')
    plt.scatter(x_val, puntoD, color='orange', zorder=5)
    plt.text(x_val, puntoD, f'({x_val}, {puntoD:.4f})', fontsize=9, verticalalignment='bottom', horizontalalignment='right')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de ' + funcion)    
    plt.legend()
    plt.grid(True)
    plt.show()

# Llamada a la función
# richardson()
# grafica()
