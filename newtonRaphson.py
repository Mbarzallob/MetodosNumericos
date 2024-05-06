# Bibliotecas nescesarias
import sympy as sp
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt


# Metodo de Newton Raphson
def newtonRaphson(funcion):
    x = sp.Symbol('x')
    f = sp.sympify(funcion)
    f_derivada = sp.diff(f, x)

    # Ingresar valores por tecledo
    valor_inicial= float(input("Ingrese el valor inicial aproximado: "))
    tol= float(input("Ingrese la tolerancia deseada: "))
    max_iter=  int(input("Ingrese el numero de iteraciones: "))
    
    # Convertimos la función y su derivada 
    f_num = sp.lambdify(x, f)
    f_derivada_num = sp.lambdify(x, f_derivada)
    
    tabla = []  # Lista para almacenar los datos de cada iteración
    
    iteracion = 0
    x_actual = valor_inicial
    
    while iteracion < max_iter:
        # Calcular valores de f(x) y f'(x)
        fx = f_num(x_actual)
        dfx = f_derivada_num(x_actual)
        
        # Calcular el siguiente valor de x
        x_siguiente = x_actual - fx / dfx
        
        # Calcular valor aproximado porcentual
        if x_actual != 0:
            if iteracion != 0:
                error = abs((x_siguiente - x_actual) / x_actual) 
                error_porcentual = error * 100
            else:
                error = "none"
                error_porcentual = "none"
        else:
            error = float('inf')
            error_porcentual = float('inf')
        
        # Agregar datos a la tabla
        tabla.append([iteracion + 1,x_actual, fx, dfx, error ,error_porcentual])
        
        # Comprobar si se alcanza la tolerancia
        if abs(x_siguiente - x_actual) < tol:
            print("+-------------------------------------------------------------------------------------------------+")
            print("|                               SE ALCANZÓ LA TOLERANCIA INDICADA                                 |")
            
            break
        
        # Actualizar x_actual para la próxima iteración
        x_actual = x_siguiente
        iteracion += 1

    if(max_iter == iteracion):
            print("+-------------------------------------------------------------------------------------------------+")
            print("|                              SE ALCANZÓ EL NUMERO DE ITEREACIONES                               |")
            

    encabezado = ["ITERACION",  "VALOR APROXIMADO"," f(x) ", "df(x)", "ERROR APROXIMADO", "ERROR APROXIMADO %"]
    
    print(tabulate(tabla, headers=encabezado, tablefmt="grid"))


def grafica(f):
    # Convertir la cadena de texto en una expresión SymPy
    x = sp.symbols('x')
    funcion = sp.sympify(f)
    valor = float(input("Ingrese el valor cercano a la raíz: "))

    # Evaluar la función en puntos cercanos al valor específico
    puntos_x = np.linspace(valor - 5, valor + 5, 100)
    puntos_y = [sp.N(funcion.subs(x, punto)) for punto in puntos_x]

    # Convertir los resultados a arrays de numpy para graficar
    puntos_x = np.array(puntos_x)
    puntos_y = np.array(puntos_y)

    # Graficar la función
    plt.plot(puntos_x, puntos_y, label='Función: ' + f)

    # Marcar el punto específico
    plt.scatter([valor], [funcion.subs(x, valor)], color='red', label='Punto específico')

    # Configurar la leyenda y etiquetas
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función alrededor del punto dado')
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)
    plt.show()