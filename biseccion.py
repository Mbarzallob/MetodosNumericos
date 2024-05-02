import matplotlib.pyplot as plt
import numpy as np
def grafica(f):
    x = np.linspace(-10, 10, 400)
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
    
def funcion(f,x):
    return eval(f)

def biseccion(f):
    xl = float(input("Ingrese el límite inferior: "))
    xu = float(input("Ingrese el límite superior: "))
    errorMax = float(input("Ingrese el error: "))
    iterMax = int(input("Ingrese el número de iteraciones máximas: "))
    iter = 0
    print("Iteración    xl         xu         xr         f(xl)      f(xu)      f(xr)      Error")
    print("------------------------------------------------------------------------------------")
    while iter < iterMax:
        xr = (xl + xu) / 2
        fr = funcion(f,xr)
        if funcion(f,xl) * fr < 0:
            xu = xr
        else:
            xl = xr
        error = abs((xu - xl) / xu) * 100
        iter += 1
        print(f"{iter:9d}  {xl:9.4f}  {xu:9.4f}  {xr:9.4f}  {funcion(f, xl):9.4f}  {funcion(f, xu):9.4f}  {fr:9.4f}  {error:9.4f}")
        if error < errorMax:
            break