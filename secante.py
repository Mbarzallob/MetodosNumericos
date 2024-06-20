import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import getpass

x0= -2
x1 = 2
e = 0.01
N = 10
raiz = None
fu= ""

def f(x, funcion):
    return eval(funcion)


def imprimir():
    global x0, x1, e, N 
    print("|------------------------------------------------|")
    print("|            MÉTODO DE LA SECANTE                |")
    print("|------------------------------------------------|")
    print(f"| x0 = {x0}{(50-2-6-len(str(x0)))*" "}|")
    print(f"| x1 = {x1}{(50-2-6-len(str(x1)))*" "}|")
    print(f"| Error = {e}{(50-2-9-len(str(e)))*" "}|")
    print(f"| Iteraciones maximas = {N}{(50-2-23-len(str(N)))*" "}|")
    print("|------------------------------------------------|")

def editar_valores():
    global x0, x1, e, N
    temp = input("Ingrese el límite inferior o presione enter para dejarlo igual: ")
    x0 = float(temp) if temp else x0
    temp = input("Ingrese el límite superior o presione enter para dejarlo igual: ")
    x1 = float(temp) if temp else x1
    temp = input("Ingrese el error o presione enter para dejarlo igual: ")
    e = float(temp) if temp else e
    temp = input("Ingrese el número de iteraciones máximas o presione enter para dejarlo igual: ")
    N = int(temp) if temp else N



def secante(funcion=None):
    global x0, x1, e, N, fu, raiz
    if not funcion:
        if not fu:
            fu = input("Ingrese la función con respecto a x: ")
        funcion = fu
    imprimir()
    v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
    if(v.upper()=="S"):
           editar_valores()
    imprimir()

        # Encontrar la raíz en el intervalo [x0, x1]
    try:
        root = optimize.root_scalar(lambda x: f(x, funcion), bracket=[x0, x1], method='brentq')
    except Exception as ex:
        print (f"Error: {ex}")
        getpass.getpass("Presion enter para continuar")
    
    condition = True
    step = 1

    print("Iteración      x          f(x)        Et%")
    print("--------------------------------------------")
    print("{:<12}{:<12.6f}{:<12.6f}".format(-1, x0, f(x0,funcion)))
    print("{:<12}{:<12.6f}{:<12.6f}".format(0, x1, f(x1,funcion)))

    while condition:
        if f(x0, funcion) == f(x1, funcion):
            print('División por cero, error!')
            break
            
        x2 = x0 - (x1 - x0) * f(x0, funcion) / (f(x1, funcion) - f(x0, funcion)) 
            
        fx2 = f(x2, funcion)
            
        # Calcular el error absoluto aproximado

        et = abs(root.root - x2)

        etp = (et/root.root) *100

        print("{:<12}{:<12.6f}{:<12.6f}{:<12.6f}".format(step, x2, fx2, etp))

        x_old = x2
        x0 = x1
        x1 = x2
        step += 1
            
        if step > N:
            print('No Convergente!')
            break
            
        condition = etp> e  

    print('\n La raiz requerida es: %0.8f' % x2)

    raiz = x2

    getpass.getpass("Presione enter para continuar")
        




def grafica(funcion=None):
    global x0, x1, e, N, fu, raiz
    if not funcion:
        if not fu:
            fu = input("Ingrese la función con respecto a x: ")
        funcion = fu

    
    x = np.linspace(x0-2, x1+2, 500)
    try:
        y = eval(funcion)
    except:
        print("Error: La expresión ingresada no es válida.")
        return
    
    if raiz is not None:
        plt.scatter(raiz, 0, color='green', zorder=5)
        plt.text(raiz, 0, f'Root: {raiz:.4f}', fontsize=9, verticalalignment='bottom', horizontalalignment='right')

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de ' + funcion)    
    plt.grid(True)
    plt.show()

#secante()
#grafica()
