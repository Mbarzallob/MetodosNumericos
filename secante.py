import scipy.optimize as optimize
import numpy as np
import math


def f(x, function):
    return eval(function)

def secante(function):

    x0 = float(input('Ingrese el primer número del intervalo: '))
    x1 = float(input('Ingrese el segundo número del intervalo: '))
    e = float(input('Máximo Error Tolerable: '))
    N = int(input('Máximo Paso: '))
    step_size = float(input('Tamaño de Paso: '))



    # Encontrar la raíz en el intervalo [x0, x1]
    root = optimize.root_scalar(lambda x: f(x, function), bracket=[x0, x1], method='brentq')

    print("\n   Raíz exacta:", round(root.root, 3))

    print('\n\n*** METODO SECANTE ***')
    condition = True
    step = 1
    while condition:
        if f(x0, function) == f(x1, function):
            print('División por cero, error!')
            break
        
        x2 = x0 - (x1 - x0) * f(x0, function) / (f(x1, function) - f(x0, function)) 
        
        fx2 = f(x2, function)
        print('\n Iteración %d, x2 = %0.6f, f(x2) = %0.6f' % (step, x2, fx2), end=" ")

        # Calcular el error absoluto aproximado
        if step > 1:
            error_abs = abs(x2 - x_old)
            et = (abs(root.root - x_old))/root.root

            # Calcular el error aproximado porcentual (Et %)
            error_aprox_porcentual = (error_abs / abs(x2)) * 100
            print('Et:', et , end=" ")
            print('Ea%:', round(error_aprox_porcentual, 6), end=" ")

            if error_aprox_porcentual < e:
                print('Convergencia alcanzada!')
                break

        x_old = x2
        x0 = x1
        x1 = x2
        step += 1
        
        if step > N:
            print('No Convergente!')
            break
        
        condition = abs(f(x2, function)) > e
    print('\n La raiz requerida es: %0.8f' % x2)




def grafica(f):
    print("Grafica")