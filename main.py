""" menu qui permet de choisir la version que l'on veut lancer """

from bruteforce import brute_force
from optimized import optimized

def main_menu() :
    """ Function to display the main menu """
    while True:
        print("\nSélectionnez l'algorithme de votre choix :\n")
        print("1 - Algorithme Force Brute")
        print("2 - Algorithme optimisé")

        choice = input("Choisissez une option : \n")
        if choice == '1':
            brute_force()
        elif choice == '2':
            optimized()
        else:
            print("Option invalide. Veuillez réessayer")

if __name__ == "__main__":
    main_menu()
