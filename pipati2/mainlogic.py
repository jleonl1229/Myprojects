import random
import sys

def miturno(mycounter, opponent, contmax):
    while mycounter <= contmax or opponent <= contmax:
        if opponent == contmax:
            print("\n\t\t\t\t=============")
            print("\t\t\t\t  GAME OVER  ")
            print("\t\t\t\t=============")
            sys.exit(0)
        elif mycounter == contmax:
            print("\n\t\t\t\t=============")
            print("\t\t\t\t   YOU WIN   ")
            print("\t\t\t\t=============")
            sys.exit(0)
        try:    
            opcion = input("Introduce one of those options: Rock, paper, or scissors\n>")
            opcion = opcion.lower()
            if opcion == "rock" or opcion == "paper" or opcion == "scissors":
                lista = ["rock", "paper", "scissors"]
                movement = random.choice(lista)
                if opcion == movement:
                    print("My points: {}\t The opponent's points: {}\n".format(mycounter, opponent))
                    print("\nYour opponent choosed {}, so you TIE :|".format(movement))
                elif (opcion == "rock" and movement == "paper") or (opcion == "paper" and movement == "scissors") or (opcion == "scissors" and movement == "rock"):
                    opponent = opponent + 1
                    print("My points: {}\t The opponent's points: {}\n".format(mycounter, opponent))
                    print("\nYour opponent choosed {}, so you LOOSE :(".format(movement))
                elif (opcion == "rock" and movement == "scissors") or (opcion == "paper" and movement == "rock") or (opcion == "scissors" and movement == "paper"):
                    mycounter = mycounter + 1
                    print("My points: {}\t The opponent's points: {}\n".format(mycounter, opponent))
                    print("\nYour opponent choosed {}, so you WIN :)".format(movement))
            else:
                print("Invalid option :(")
                print("End of the game :P")
                sys.exit(1)
        except KeyboardInterrupt:
            print("\nLeaving the program...")
            sys.exit(1)

def main():
    mycounter = 0
    opponent = 0
    try:
        contmax = int(input("\nTo how many points do you wanna play: "))
    except ValueError:
        print("You haven't entered an integer")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nLeaving the program...")
        sys.exit(1)
    if contmax > 0:
        miturno(mycounter, opponent, contmax)
    else:
        print("Introduce a number greater than zero")

if __name__ == '__main__':
    main()