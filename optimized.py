import csv
import time
from rich import print

# ----- Pour lancer sans le fichier main, vous devez décommenter la ligne situé a la fin du fichier ----- #


def choice_csv():
    """ Permet à l'utilisateur de choisir un fichier CSV parmi une liste prédéfinie. """
    print("[cyan]Veuillez choisir le fichier CSV à analyser :[/cyan]")
    print("1. action_bruteforce.csv")
    print("2. data/dataset1_Python+P7.csv")
    print("3. data/dataset2_Python+P7.csv")
    choice = input("Entrez le numéro correspondant au fichier (1, 2 ou 3) : \n")

    if choice == '1':
        return 'data/action_bruteforce.csv'
    elif choice == '2':
        return 'data/dataset1_Python+P7.csv'
    elif choice == '3':
        return 'data/dataset2_Python+P7.csv'
    else:
        print("Choix invalide. Veuillez relancer le programme et choisir 1, 2 ou 3.")
        return


def read_csv(csv_file_path):
    """ Lit le fichier CSV et retourne une liste de dictionnaires représentant les actions."""
    actions = []
    with open(csv_file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cost = float(row['price'])
            profit = float(row['profit'])
            if cost > 0 and profit > 0:
                actions.append({
                    'name': row['name'],
                    'cost': cost,
                    'profit': profit,
                })
    return actions


def calculate_total_cost(selected_actions):
    """ Calcule le coût total des actions sélectionnées."""
    return sum(action['cost'] for action in selected_actions)


def calculate_total_profit(selected_actions):
    """ Calcule le profit total des actions sélectionnées après 2 ans."""
    return sum((action['profit'] * action['cost']) / 100 for action in selected_actions)


def select_actions(actions, max_budget):
    """ Sélectionne les actions à acheter en maximisant le profit tout en respectant le budget."""
    actions.sort(key=lambda d: d['profit'], reverse=True)
    selected_actions = []

    for action in actions:
        if calculate_total_cost(selected_actions) + action['cost'] <= max_budget:
            selected_actions.append(action)

    return selected_actions


def optimized():
    """ Exécute l'algorithme optimisé pour sélectionner les actions à acheter."""

    max_budget = 500

    csv_file_path = choice_csv()
    if not csv_file_path:
        return

    start_time = time.time()

    actions = read_csv(csv_file_path)
    if not actions:
        return

    selected_actions = select_actions(actions, max_budget)

    if not selected_actions:
        print("Pas de combinaison valide trouvée.")
    else:
        print("\n[cyan]Les actions sélectionnées sont :[/cyan]")
        for action in selected_actions:
            print(f"{action['name']} - Coût: {action['cost']}€, Profit: {action['profit']}%")

        total_cost = calculate_total_cost(selected_actions)
        total_profit = calculate_total_profit(selected_actions)

        print(f"\n[cyan]Coût total des actions : {total_cost:.3f} euros[/cyan]")
        print(f"[cyan]Profit total après 2 ans: {total_profit:.3f}€[/cyan]\n")

    end_time = time.time()
    print(f"Temps d'exécution : {end_time - start_time:.4f} secondes\n")

# # ------- décommanter la ligne ci dessous pour lancer sans le fichier main ------- #
# optimized()
