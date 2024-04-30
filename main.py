def biseccion():
    print("Metodo de la biseccion...")
    
def falsaPosicion():
    print("Metodo de la falsa posicion...")

def newtonRaphson():
    print("Metodo de newton raphson...")

def secante():
    print("Metodo de la secante...")

opciones = {
    1: {
        "nombre": "Metodos abiertos",
        "submenus": {
            1: {
                "nombre": "Metodo de la bisección",
                "funcion": biseccion
            },
            2: {
                "nombre": "Metodo de la falsa posición",
                "funcion": falsaPosicion
            }
        }
    },
    2: {
        "nombre": "Metodos cerrados",
        "submenus": {
            1:{
                "nombre": "Metodo de Newton-Raphson",
                "funcion": newtonRaphson
            },
            2: {
                "nombre": "Metodo de la secante",
                "funcion": secante
            }
        }
    }
}

opcion = [-1, -1]
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
        if(opcion[1] != 0):
            opciones[opcion[0]]['submenus'][opcion[1]]['funcion']()
