import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
import math
import os

x0= 0
x1 = 1
e = 0.01
N = 10

def f(x, function):
    return eval(function)


def imprimir():
    print("|------------------------------------------------|")
    print("|            MÉTODO DE LA SECANTE                |")
    print("|------------------------------------------------|")
    print(f"| x0 = {x0}{(50-2-6-len(str(x0)))*" "}|")
    print(f"| x1 = {x1}{(50-2-6-len(str(x1)))*" "}|")
    print(f"| Error = {e}{(50-2-9-len(str(e)))*" "}|")
    print(f"| Iteraciones maximas = {N}{(50-2-23-len(str(N)))*" "}|")
    print("|------------------------------------------------|")

def secante(function):
        global x0, x1, e, N
        imprimir()
        v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
        if(v.upper()=="S"):
            os.system("cls")
            imprimir()
            x0 = float(input("Ingrese el límite inferior: "))
            os.system("cls")
            imprimir()
            x1 = float(input("Ingrese el límite superior: "))
            os.system("cls")
            imprimir()
            e = float(input("Ingrese el error: "))
            os.system("cls")
            imprimir()
            N = int(input("Ingrese el número de iteraciones máximas: "))
        os.system("cls")
        imprimir()

        # Encontrar la raíz en el intervalo [x0, x1]
        root = optimize.root_scalar(lambda x: f(x, function), bracket=[x0, x1], method='brentq')

        
        print("\n   Raíz exacta: ", root.root)
        print()

        condition = True
        step = 1

        print("Iteración      x          f(x)        Et%")
        print("--------------------------------------------")
        print("{:<12}{:<12.6f}{:<12.6f}".format(-1, x0, f(x0,function)))
        print("{:<12}{:<12.6f}{:<12.6f}".format(0, x1, f(x1,function)))

        while condition:
            if f(x0, function) == f(x1, function):
                print('División por cero, error!')
                break
            
            x2 = x0 - (x1 - x0) * f(x0, function) / (f(x1, function) - f(x0, function)) 
            
            fx2 = f(x2, function)
            

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
        




def grafica(f):
    global x0, x1, e, N
    print("Grafica")
    x = np.linspace(x0, x1, 500)
    try:
        y = eval(f)
    except:
        print("Error: La expresión ingresada no es válida.")
        exit()
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de ' + f)
    plt.grid(True)
    plt.show()