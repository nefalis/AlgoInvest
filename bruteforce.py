import csv
import time
from rich import print
from itertools import combinations

# ----- Pour lancer sans le fichier main, vous devez décommenter la ligne situé a la fin du fichier ----- #


def brute_force():
    """
    Algorithme brute force
    Ce programme parcourt toutes les combinaisons possibles d'actions et
    sélectionne celle qui maximise le profit tout en respectant le budget.
    """

    # Début de la mesure du temps
    start_time = time.time()

    max_budget = 500
    csv_file_path = 'data/action_bruteforce.csv'

    # Lecture des données du fichier csv
    actions = []
    with open(csv_file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            action = {
                'name': row['name'],
                'cost': int(row['price']),
                'profit': float(row['profit'])
            }
            actions.append(action)

    # Recherche de la meilleure combinaison
    best_combination = None
    best_profit = 0

    # Génère toutes les combinaison d'action de la taille 1 à la taille de la liste d'action
    for i in range(1, len(actions) + 1):
        for combo in combinations(actions, i):
            total_price_action = sum(action['cost'] for action in combo)
            total_profit = sum(action['cost'] * action['profit'] / 100 for action in combo)
            # Si le coût total inférieur au budget et profit total est supérieur au meilleur profit
            # met a jour la nouvelle combinaison optimale
            if total_price_action <= max_budget and total_profit > best_profit:
                best_combination = combo
                best_profit = total_profit
                best_cost = total_price_action

    # Affichage des résultats
    if best_combination is None:
        print("Pas de combinaison valide trouvé.")
    else:
        print("\n[cyan]Les actions sélectionnées sont :[/cyan]")
        for action in best_combination:
            print(f"  {action['name']} - Cost: {action['cost']}€, Profit: {action['profit']}%")
        print(f"\n[cyan]Coût total des actions : {best_cost:.3f} euros[/cyan]")
        print(f"[cyan]Profit total après 2 ans: {best_profit:.3f}€[/cyan]\n")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nExecution time: {execution_time:.4f} seconds\n")

# ------- décommanter la ligne ci dessous pour lancer sans le fichier main ------- #
# brute_force()
