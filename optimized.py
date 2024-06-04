import csv
import time
from itertools import combinations

def optimized():

    # Début de la mesure du temps
    start_time = time.time()

    max_budget = 500
    csv_file_path = 'data/action_bruteforce.csv'

    # lecture des données du fichier csv
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

    # cherche la meilleur combinaison
    # best_combination stocke la meilleur combinaison trouvé et best_profit stock le profit de cette combianison
    best_combination = None
    best_profit = 0
    # génère les combinaison d'action de la taille 1 à la taille de la liste d'action
    for i in range(1, len(actions) + 1):
        # pour chaque combinaison calcul le cout total et le profit total
        for combo in combinations(actions, i):
            total_price_action = sum(action['cost'] for action in combo)
            total_profit = sum(action['cost'] * action['profit'] / 100 for action in combo)
            # si cout total inférieu au budget et profit total est sup au meilleur profit met a jour la nouvelle combi
            if total_price_action <= max_budget and total_profit > best_profit:
                best_combination = combo
                best_profit = total_profit
                best_cost = total_price_action

    # Affichage des résultats
    if best_combination is None:
        print("Pas de combinaison valide trouvé.")
    else:
        print("Les actions sélectionnées sont : :")
        for action in best_combination:
            print(f"  {action['name']} - Cost: {action['cost']}€, Profit: {action['profit']}%")
        print(f"\nCoût total des actions : {best_cost} euros")
        print(f"Profit total après 2 ans: {best_profit:.2f}€\n")
        

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nExecution time: {execution_time:.4f} seconds\n")