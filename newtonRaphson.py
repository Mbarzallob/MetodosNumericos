# Bibliotecas nescesarias
import sympy as sp
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt

funcion = 'x**3-2*x-5'

def elegir_funcion():
    global funcion
    
    print("Funciones para Newton Raphson: ")
    print(" 0. Ingresar función")
    print(" 1. sin(x) - x/2")
    print(" 2. ln(x) - 1")
    print(" 3. x**3 - x - 2")
    print(" 4. Funcion por defecto: x**3 - 2*x - 5")
    
    respuesta = int(input("Ingrese una opción: "))
    
    if respuesta == 0:
        funcion = input("Ingrese la función (use 'x' como variable): ")
    elif respuesta == 1:
        funcion = 'sin(x) - x/2'
    elif respuesta == 2:
        funcion = 'ln(x) - 1'
    elif respuesta == 3:
        funcion = 'x**3 - x - 2'
    else:
        funcion = 'x**3 - 2*x - 5'
    
    print("F(x)= ", funcion)



# Metodo de Newton Raphson
def newtonRaphson(f =None):
    global funcion
    elegir_funcion()
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
    
    iteracion =1 
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



def grafica(f = None):
    global funcion
    
    # Convertir la cadena de texto en una expresión SymPy
    x = sp.symbols('x')
    f = sp.sympify(funcion)
    
    # Solicitar al usuario que ingrese el valor cercano a la raíz
    valor = float(input("Ingrese el valor cercano a la raíz: "))
    
    # Evaluar la función en puntos cercanos al valor específico
    puntos_x = np.linspace(valor - 5, valor + 5, 100)
    puntos_y = np.array([sp.N(f.subs(x, punto)) for punto in puntos_x])
    
    # Graficar la función
    plt.plot(puntos_x, puntos_y, label='Función: ' + funcion)
    
    # Marcar el punto específico
    plt.scatter([valor], [float(f.subs(x, valor))], color='red', label='Punto específico')
    
    # Configurar la leyenda y etiquetas
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función alrededor del punto dado')
    plt.legend()
    
    # Mostrar el gráfico
    plt.grid(True)
    plt.show()
