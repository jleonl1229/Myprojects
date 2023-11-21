import random
import sys

def miturno(micontador, lamaquina, contmax):
    while micontador <= contmax or lamaquina <= contmax:
        if micontador == contmax or lamaquina == contmax:
            print("\n\t\t\t\t=============")
            print("\t\t\t\tFIN DEL JUEGO")
            print("\t\t\t\t=============")
            sys.exit(0)
        opcion = input("Introduce una de las siguientes opciones: Piedra, papel, o tijera\n>")
        opcion = opcion.lower()
        if opcion == "piedra" or opcion == "papel" or opcion == "tijera":
            lista = ["piedra", "papel", "tijera"]
            movement = random.choice(lista)
            if opcion == movement:
                print("Mis puntos: {}\t Los puntos de la maquina: {}\n".format(micontador, lamaquina))
                print("\nTu rival ha sacado {}, por lo tanto EMPATAS :|".format(movement))
            elif (opcion == "piedra" and movement == "papel") or (opcion == "papel" and movement == "tijera") or (opcion == "tijera" and movement == "piedra"):
                lamaquina = lamaquina + 1
                print("Mis puntos: {}\t Los puntos de la maquina: {}\n".format(micontador, lamaquina))
                print("\nTu rival ha sacado {}, por lo tanto PIERDES :(".format(movement))
            elif (opcion == "piedra" and movement == "tijera") or (opcion == "papel" and movement == "piedra") or (opcion == "tijera" and movement == "papel"):
                micontador = micontador + 1
                print("Mis puntos: {}\t Los puntos de la maquina: {}\n".format(micontador, lamaquina))
                print("\nTu rival ha sacado {}, por lo tanto GANAS :)".format(movement))
        else:
            print("No has introducido ninguna opcion valida :(")
            print("Fin del juego :P")
            sys.exit(1)

def main():
    micontador = 0
    lamaquina = 0
    try:
        contmax = int(input("\nA cuantos puntos quieres hechar la partida: "))
    except ValueError:
        print("No has ingresado un numero entero")
        sys.exit(1)
    miturno(micontador, lamaquina, contmax)

if __name__ == '__main__':
    main()