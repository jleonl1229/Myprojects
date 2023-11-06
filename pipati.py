import random
import sys

def IA(opcion, micontador, lamaquina):
    lista = ["piedra", "papel", "tijera"]
    movement = random.choice(lista)
    if opcion == movement:
        print("Mis puntos: {}\t Los puntos de la maquina: {}\n".format(micontador, lamaquina))
        print("\nEl enemigo ha sacado {}, por lo tanto EMPATAS :|".format(movement))
    elif (opcion == "piedra" and movement == "papel") or (opcion == "papel" and movement == "tijera") or (opcion == "tijera" and movement == "piedra"):
        lamaquina = lamaquina + 1
        print("Mis puntos: {}\t Los puntos de la maquina: {}\n".format(micontador, lamaquina))
        print("\nEl enemigo ha sacado {}, por lo tanto PIERDES :(".format(movement))
    elif (opcion == "piedra" and movement == "tijera") or (opcion == "papel" and movement == "piedra") or (opcion == "tijera" and movement == "papel"):
        micontador = micontador + 1
        print("Mis puntos: {}\t Los puntos de la maquina: {}\n".format(micontador, lamaquina))
        print("\nEl enemigo ha sacado {}, por lo tanto GANAS :)".format(movement))
    
    if micontador == 3 or lamaquina == 3:
            print("\n\t\t\t\t=============")
            print("\t\t\t\tFIN DEL JUEGO")
            print("\t\t\t\t=============")
            sys.exit(0)
    miturno(micontador, lamaquina)

def miturno(micontador, lamaquina):
    opcion = input("Introduce una de las siguientes opciones: Piedra, papel, o tijera\n>")
    opcion = opcion.lower()
    if opcion == "piedra" or opcion == "papel" or opcion == "tijera":
        IA(opcion, micontador, lamaquina)
    else:
        print("No has introducido ninguna opcion valida :(")
        print("Fin del juego :P")
        sys.exit(1)

def main():
    micontador = 0
    lamaquina = 0
    miturno(micontador, lamaquina)

main()