import csv
import time
from itertools import combinations


def brute_force():
    """ algorithme brute force """

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

    # # Début de la mesure du temps
    # start_time = time.time()

    # budget_max = 500
    # # Chemin vers le fichier CSV
    # csv_file_path = 'data/action_bruteforce.csv'

    # # lecture des données du fichier csv
    # actions = []
    # with open(csv_file_path, newline='') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             # Convertir les valeurs de price et profit en entiers
    #             price = int(row['price'])
    #             profit = int(row['profit'])
    #             # # Calculer le ratio bénéfice/coût
    #             profit_ratio = profit / price
    #             actions.append({'name': row['name'], 'price': price, 'profit': profit, 'profit_ratio': profit_ratio})

    # # filtre des actions dont le cout est inférieur ou egale à la valeur max du client
    # max_price_action = [action for action in actions if action['price'] <= budget_max]

    # # trie des action en ration bénéfice/prix ordre décroissant
    # sorted_actions = sorted(max_price_action, key=lambda x: x['profit_ratio'], reverse=True)

    # # selection des actions
    # selected_actions = []
    # total_cost = 0

    # for action in sorted_actions:
    #     # verif si action est dans le budget
    #     if total_cost + action['price'] <= budget_max:
    #         # vérif si l'action est disponible
    #         if action not in selected_actions:
    #             selected_actions.append(action)
    #             total_cost += action['price']

    # # affichage des résultats
    # print("\nLes actions sélectionnées sont : ")
    # for action in selected_actions:
    #     print(f"Nom: {action['name']}, Coût: {action['price']} euros, Bénéfice: {action['profit']} %\n")

    # # calcul du profit des actions cumulés après 2 ans
    # total_price_action = sum(action['price'] for action in selected_actions)
    # total_profit = sum(action['price'] * (action['profit'] / 100) for action in selected_actions)
    # print(f"\nCoût total des actions : {total_price_action} euros\n")
    # print(f"\nProfit total après 2 ans : {total_profit} euros\n")

    # # Fin de la mesure du temps
    # end_time = time.time()

    # # Calcul du temps d'exécution
    # execution_time = end_time - start_time
    # print(f"\nTemps d'exécution : {execution_time:.4f} secondes\n")
