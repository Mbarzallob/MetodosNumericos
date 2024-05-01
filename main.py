import biseccion as bis
import falsaPosicion as fp
import newtonRaphson as np
import secante as sec

def imprimirMetodos():
    print("1. Grafica")
    print("2. Metodo")
    print("0. Salir")
    
opciones = {
    1: {
        "nombre": "Metodos abiertos",
        "submenus": {
            1: {
                "nombre": "Metodo de la bisección",
                "funciones": {
                    1: bis.grafica,
                    2: bis.biseccion
                }
            },
            2: {
                "nombre": "Metodo de la falsa posición",
                "funciones": {
                    1: fp.grafica,
                    2: fp.falsaPosicion
                }
            }
        }
    },
    2: {
        "nombre": "Metodos cerrados",
        "submenus": {
            1:{
                "nombre": "Metodo de Newton-Raphson",
                "funciones": {
                    1: np.grafica,
                    2: np.newtonRaphson
                }
            },
            2: {
                "nombre": "Metodo de la secante",
                "funciones": {
                    1: sec.grafica,
                    2: sec.secante
                }
            }
        }
    }
}

opcion = [-1, -1, -1]
while opcion[0] != 0:
    print("ELIJA UNA OPCION:")
    for i in opciones:
        print(str(i) + ". " + opciones[i]["nombre"])
    print("0. Salir")
    opcion[0] = int(input())
    while opcion[1] != 0:
        print("ELIJA UN METODO:")
        for i in opciones[opcion[0]]['submenus']:
            print(str(i) + ". " + opciones[opcion[0]]['submenus'][i]['nombre']) 
        print("0. Regresar")
        opcion[1] = int(input())
        while opcion[2]!=0:
            imprimirMetodos()
            opcion[2] = int(input())
            if(opcion[2]!=0):
                f = input("Ingrese la función en términos de x: ")
                opciones[opcion[0]]['submenus'][opcion[1]]['funciones'][opcion[2]](f)

