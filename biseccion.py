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
    
    
def biseccion(f):
    print("Biseccion")
