import csv
import time


def choice_csv():
    # choix du fichier csv a lire
    print("Veuillez choisir le fichier CSV à analyser :")
    print("1. action_bruteforce.csv")
    print("2. data/dataset1_Python+P7.csv")
    print("3. data/dataset2_Python+P7.csv")
    choice = input("Entrez le numéro correspondant au fichier (1, 2 ou 3) : ")

    if choice == '1':
        return 'data/action_bruteforce.csv'
    elif choice == '2':
        return 'data/dataset1_Python+P7.csv'
    elif choice == '3':
        return 'data/dataset2_Python+P7.csv'
    else:
        print("Choix invalide. Veuillez relancer le programme et choisir 1, 2 ou 3.")
        return

def optimized():
    """ algorithme optimisé """

    csv_file_path = choice_csv()

    # Début de la mesure du temps
    start_time = time.time()

    max_budget = 500

    # lecture des données du fichier csv
    actions = []
    with open(csv_file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cost = float(row['price'])
            profit = float(row['profit'])
            if cost > 0 and profit > 0:
                action = {
                    'name': row['name'],
                    'cost': cost,
                    'profit': profit,
                    'ratio': (profit/100)/cost
                }
                actions.append(action)

    # tri des actions par ratio cout/profit croissant
    actions.sort(key=lambda x: x['ratio'], reverse=True)

    # Initialise le tableau de programmation dynamique
    action_number = len(actions)
    dynamic_table = [[0] * (max_budget + 1) for _ in range(action_number + 1)]

    # Remplir le tableau
    # parcourt chaque action dispo
    for i in range(1, action_number + 1):
        # parcourt chaque budget possible
        for budget in range(max_budget + 1):
            # si cout action est inf a budget - dynamic_table[i]budget prend la valeur max
            if actions[i-1]['cost'] <= budget:
                # profit max = profit max sans action actuelle, cout profit actuel * %benef /100
                #  + profit max pour le budget restant avec action actuelle
                dynamic_table[i][budget] = max(
                    dynamic_table[i-1][budget],
                    actions[i-1]['cost'] * actions[i-1]['profit'] / 100 + dynamic_table[i-1][budget - int(actions[i-1]['cost'])])
            # si cout depasse budget on garde la valeur dynamic_table[i][budget]
            else:
                dynamic_table[i][budget] = dynamic_table[i-1][budget]

    # Reconstituer la meilleure combinaison avec le dynamic_table
    # on commence par budget max et on remonte en verif les actions incluses dans la combinaison optimale
    remaining_budget = max_budget
    best_combination = []
    # on parcourt les actions en sens inverse de n à 1 - n=nb total action
    for i in range(action_number, 0, -1):
        # verif si dynamic_table[remaining_budget] est différent de dynamic_table[i-1][remaining_budget] car i-1 a été inclu si oui donc ajout action a best_combination
        if dynamic_table[i][int(remaining_budget)] != dynamic_table[i-1][int(remaining_budget)]:
            best_combination.append(actions[i-1])
            # on reduit le remaining_budget de cost de l'action i-1
            remaining_budget -= actions[i-1]['cost']

    # Calculer le profit total de la meilleure combinaison
    best_profit = sum(action['cost'] * action['profit'] / 100 for action in best_combination)
    best_cost = sum(action['cost'] for action in best_combination)

    # Affichage des résultats
    if not best_combination:
        print("Pas de combinaison valide trouvée.")
    else:
        print("Les actions sélectionnées sont :")
        for action in best_combination:
            print(f"  {action['name']} - Coût: {action['cost']}€, Profit: {action['profit']}%")
        print(f"\nCoût total des actions : {best_cost} euros")
        print(f"Profit total après 2 ans: {best_profit:.2f}€\n")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nTemps d'exécution : {execution_time:.4f} secondes\n")

# # ------- décommanter la ligne ci dessous pour lancer sans le fichier main ------- # 
# # optimized()

