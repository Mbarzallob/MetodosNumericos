import numpy as np
import matplotlib.pyplot as plt

def grafica():
    print()
    
def regresionPolinomial(grado, datos):
   # m= int(input('Ingrese el grado del polinomio'))

    # Paso 1: Introduzca el grado del polinomio sujeto a ajuste, m.
    m = grado
    
    # Paso 2: Introduzca el número de datos, n.
    n = len(datos)
    
    # Paso 3: Verificar si n < m + 1
    if n < m + 1:
        print("Error: La regresión no es posible, n es menor que m + 1.")
        return
    
    # Inicialización de la matriz aumentada
    A = np.zeros((m+1, m+2))
    

    # Extraer x e y de los datos
    x = np.array([dato[0] for dato in datos])
    y = np.array([dato[1] for dato in datos])
    
    # Paso 4: Calcular los elementos de la ecuación normal en la forma de una matriz aumentada
    for i in range(m + 1):
        for j in range(i + 1):
            k = i + j
            suma = np.sum(x ** k)
            A[i, j] = suma
            A[j, i] = suma
        
        suma = np.sum(y * (x ** i))
        A[i, m+1] = suma
    
    print('Matriz aumentada a resolver: ')
    print(A)
    print()

    
    # Paso 5: Usando la matriz aumentada determine los coeficientes a0, a1, a2,…, am, por medio de un método de eliminación.
    coeficientes = eliminacion_gaussiana(A)
    
    # Paso 6: Imprima los coeficientes.
    print("Coeficientes del polinomio:")
    ecuacion = ""
    for i in range(m + 1):
        print(f'a{i} = {coeficientes[i]}')
        if (i == 0):
            ecuacion+= str(round(coeficientes[i],4))
        elif (i == 1): 
            ecuacion+= " + "+str(round(coeficientes[i],4))+"x"
        else:
            ecuacion+= " + " +str(round(coeficientes[i],4)) +"x**"+str(i) 
    print('\n Ecuacion polinomial: ')
    print(ecuacion)

    graficar_polynomial(x, y, coeficientes, ecuacion)


def eliminacion_gaussiana(matriz_aumentada):
    n = len(matriz_aumentada)
    
    for i in range(n):
        max_el = abs(matriz_aumentada[i, i])
        max_row = i
        for k in range(i+1, n):
            if abs(matriz_aumentada[k, i]) > max_el:
                max_el = abs(matriz_aumentada[k, i])
                max_row = k
        
        matriz_aumentada[[i, max_row]] = matriz_aumentada[[max_row, i]]
        
        for k in range(i+1, n):
            c = -matriz_aumentada[k, i] / matriz_aumentada[i, i]
            matriz_aumentada[k, i:] += c * matriz_aumentada[i, i:]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = matriz_aumentada[i, n] / matriz_aumentada[i, i]
        for k in range(i-1, -1, -1):
            matriz_aumentada[k, n] -= matriz_aumentada[k, i] * x[i]
    
    return x


def graficar_polynomial(x, y, coeficientes, ecuacion):
    plt.scatter(x, y, color='blue', label='Datos originales')
    
    x_line = np.linspace(min(x), max(x), 500)
    y_line = np.zeros_like(x_line)
    for i in range(len(coeficientes)):
        y_line += coeficientes[i] * (x_line ** i)
    
    plt.plot(x_line, y_line, color='green', label=ecuacion)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Regresion polinomial')
    plt.legend()
    plt.show()

# Ejemplo de uso:
datos = [(-2, 3), (-1, 0), (0, 2), (1, 4), (2, 4)]  # Ejemplo de datos (x, y)
grado = 3  # Grado del polinomio

#regresionPolinomial(grado, datos)


