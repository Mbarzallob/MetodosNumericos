import numpy as np
import matplotlib.pyplot as plt

def obtener_puntos():
    puntos_x = []
    puntos_y = []
    print("Ingrese los puntos para la interpolación. Escriba 'done' cuando termine.")
    while True:
        x = input("x: ")
        if x.lower() == 'done':
            break
        y = input("y: ")
        if y.lower() == 'done':
            break
        try:
            puntos_x.append(float(x))
            puntos_y.append(float(y))
        except ValueError:
            print("Por favor, ingrese valores numéricos.")
    return puntos_x, puntos_y

def grafica(f):

    puntos_x, puntos_y = obtener_puntos()

    plt.scatter(puntos_x, puntos_y, color='red')
    x = np.linspace(min(puntos_x), max(puntos_x), 500)
    y = [lagrange_evaluar(p, puntos_x, puntos_y) for p in x]
    plt.plot(x, y, label='Polinomio de Lagrange')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación de Lagrange')
    plt.legend()
    plt.grid(True)
    plt.show()

def lagrange_evaluar(x, puntos_x, puntos_y):
    suma = 0
    for i in range(len(puntos_x)):
        producto = puntos_y[i]
        for j in range(len(puntos_x)):
            if i != j:
                producto *= (x - puntos_x[j]) / (puntos_x[i] - puntos_x[j])
        suma += producto
    return suma

def lagrange(f):
    print("Seleccione el método de interpolación de Lagrange:")
    print("1. Normal")
    print("2. Inverso")
    metodo = input("Opción: ")

    if metodo not in ['1', '2']:
        print("Opción no válida.")
        return

    puntos_x, puntos_y = obtener_puntos()


    print("Puntos dados:")
    for i in range(len(puntos_x)):
        print(f"({puntos_x[i]}, {puntos_y[i]})")

    n = len(puntos_x)
    polinomio = ""

    if metodo == '1':  
        for i in range(n):
            L_i = f"L_{i}(x) = "
            numerador = ""
            denominador = ""
            for j in range(n):
                if i != j:
                    numerador += f"(x - {puntos_x[j]})"
                    denominador += f"({puntos_x[i]} - {puntos_x[j]})"
                    if j != n - 1 and not (i == n - 2 and j == n - 1):
                        numerador += " * "
                        denominador += " * "
            L_i += f"{numerador} / {denominador}"
            print(L_i)

            if i < n - 1:
                polinomio += f"{puntos_y[i]} * {numerador} / {denominador} + "
            else:
                polinomio += f"{puntos_y[i]} * {numerador} / {denominador}"
    else:  
        for i in range(n):
            L_i = f"L_{i}(x) = "
            numerador = ""
            denominador = ""
            for j in range(n):
                if i != j:
                    numerador += f"(x - {puntos_y[j]})"
                    denominador += f"({puntos_y[i]} - {puntos_y[j]})"
                    if j != n - 1 and not (i == n - 2 and j == n - 1):
                        numerador += " * "
                        denominador += " * "
            L_i += f"{numerador} / {denominador}"
            print(L_i)

            if i < n - 1:
                polinomio += f"{puntos_x[i]} * {numerador} / {denominador} + "
            else:
                polinomio += f"{puntos_x[i]} * {numerador} / {denominador}"

    print("\nPolinomio de Lagrange:")
    print(f"P(x) = {polinomio}")

    while True:
        x = input("\nIngrese un valor de x para evaluar el polinomio (o 'salir' para terminar): ")
        if x.lower() == 'salir':
            break
        try:
            x = float(x)
            y = lagrange_evaluar(x, puntos_x, puntos_y)
            print(f"P({x}) = {y}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
