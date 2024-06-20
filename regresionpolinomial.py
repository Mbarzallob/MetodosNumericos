import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])  
y = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1]) 
grado = 2  
ecuacion = ""
coeficientes = []

def editar_valores():
    global x, y, grado

    temp = input("Ingrese los valores de x separados por comas o presione enter para dejarlo igual: ")
    if temp:
        x = np.array([float(i) for i in temp.split(',')])
        
    temp = input("Ingrese los valores de y separados por comas o presione enter para dejarlo igual: ")
    if temp:
        y = np.array([float(i) for i in temp.split(',')])
    
    temp = input("Ingrese el grado de regresion o presione enter para dejarlo igual: ")
    if temp:
        grado = int(temp)

    print(f"Nuevos valores:\n x: {x}\n y: {y}\n grado: {grado}")


def grafica(f=None):
    global x, y, grado, ecuacion, coeficientes

    # Ejecutar la regresión polinomial para obtener los coeficientes y la ecuación
    regresionPolinomial()

    # Generar valores de x para la gráfica del polinomio
    x_plot = np.linspace(min(x), max(x), 100)
    y_plot = sum(coef * x_plot**i for i, coef in enumerate(coeficientes))

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='red', label='Datos originales')
    plt.plot(x_plot, y_plot, color='blue', label=f'Polinomio de grado {grado}')
    plt.title('Regresión Polinomial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def regresionPolinomial(f=None):
    global x, y, grado, ecuacion, coeficientes
    print(f"Valores:\n x: {x}\n y: {y}\n grado: {grado}")

    v = input("DESEA EDITAR LOS VALORES INICIALES (s): ")
    if(v.upper()=="S"):
           editar_valores()

    # Paso 1: Introduzca el grado del polinomio sujeto a ajuste, m.
    print(grado)
    m = grado
    
    # Paso 2: Introduzca el número de datos, n.
    n = len(x)
    
    # Paso 3: Verificar si n < m + 1
    if n < m + 1:
        print("Error: La regresión no es posible, n es menor que m + 1.")
        return
    
    # Inicialización de la matriz aumentada
    A = np.zeros((m+1, m+2))
    

    # Paso 4: Calcular los elementos de la ecuación normal en la forma de una matriz aumentada
    for i in range(m + 1):
        for j in range(i + 1):
            k = i + j
            suma = np.sum(x ** k)

            A[i, j] = suma
            A[j, i] = suma
        
        suma = np.sum(y * (x ** i))
        A[i, m+1] = suma
    
    A_imprmir = np.copy(A)

    # Paso 5: Usando la matriz aumentada determine los coeficientes a0, a1, a2,…, am, por medio de un método de eliminación.
    coeficientes = eliminacion_gaussiana(A)

    # Impresion datos 
    y_prom = np.mean(y)
    x_prom = np.mean(x)

    y2222 = ((y - y_prom)**2)
    y_y2 = np.sum(y2222)

    ycoeeeee = sum(coef * x**i for i, coef in enumerate(coeficientes))
    y1_coe = np.sum((y - ycoeeeee)**2)

    print("|------------------------------------------------------------|")
    print("|                     Regresión Polinomial                   |")
    print("|------------------------------------------------------------|")
    print(f"x prom: {x_prom}\t y prom:{y_prom:2f}\t m: {m}\t n: {n}")
    
    print("\nValores:")
    print("{:<15} {:<15} {:<15} {:<15}".format("x", "y", "(y-y_prom)^2", "(y-pred)^2"))
    print("------------------------------------------------------------")
    for i in range(len(x)):
        print("{:<15.2f} {:<15.2f} {:<15.4f} {:<15.4f}".format(x[i], y[i], y2222[i], ycoeeeee[i]))
    print('Sumatoria')
    print("{:<15.2f} {:<15.2f} {:<15.4f} {:<15.4f}".format(np.sum(x),np.sum(y), y_y2, y1_coe))

        
    print('\nMatriz aumentada a resolver: ')
    print(A_imprmir)
    print()
    

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


    syx = np.sqrt(y1_coe/(n-(m+1)))

    r2 = (y_y2-y1_coe)/(y_y2)

    r = np.sqrt(r2)

    print('\nERROR')
    print(f"S x/y: {syx:2f}\t r^2 : {r2:2f}\t r: {r:2f}")

    while True:
        x_punto = input("\nIngrese un valor de x para evaluar el polinomio (o 'salir' para terminar): ")
        if x_punto.lower() == 'salir':
            break
        try:
            x_punto = float(x_punto)
            resultado_evaluacion = eval(ecuacion.replace('x', f'*({x_punto})'))
            print(f"P({x_punto}) = {resultado_evaluacion}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Error al evaluar el polinomio: {str(e)}")



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



#regresionPolinomial(grado, x, y)
#grafica()


